from email import header
import logging
import os
import requests
logger = logging.getLogger()

class BinanceConnector:
    def __init__(self) :
        self._api_key = os.environ['BNB_APIKEY']
        self._secret_key = os.environ['BNB_SECRETKEY']
        self._base_url = "https://testnet.binancefuture.com"
        self._header = {"X-MBX-APIKEY":self._api_key}
        self._prices = dict()

    def _makeGET(self,endpoint,data=None):
        response = requests.get(self._base_url+endpoint,params=data,headers=self._header)
        
        try:
            logger.info("Connection established!")
            return response.json()
        except Exception as e :
            logger.error("Cannot establish connection ",e)

    def exchangeInfo(self):
        endpoint = "/fapi/v1/exchangeInfo"
        exchange_information = self._makeGET(endpoint)
        pairs = dict()
        for asset in exchange_information['symbols']:
            pairs[asset['pair']] = asset
        return pairs

    def klineCandlestickData(self,symbol,interval="1h"):

        data = dict()
        data['symbol'] = symbol
        data['interval'] = interval
        data['limit'] = 1000

        endpoint = "/fapi/v1/klines"

        candleData = self._makeGET(endpoint,data)

        candles = []

        for candle in candleData:
            candles.append([candle[0],candle[1],candle[2],candle[3],candle[4],candle[5]])

        return candles
    
    def symbolOrderBooklTicker(self,symbol):
        endpoint = "/fapi/v1/ticker/bookTicker"
        data = dict()
        data['symbol'] = symbol
        price = self._makeGET(endpoint,data)

        
        if symbol not in self._prices:
            self._prices[symbol] = {'bid':float(price['bidPrice']),'ask':float(price['askPrice'])}
        else:
            self._prices[symbol]['bid'] = float(price['bidPrice'])
            self._prices[symbol]['ask'] = float(price['askPrice'])

        return self._prices




