from email import header
import logging
import os
import requests
logger = logging.getLogger()

class BinanceConnector:
    def __init__(self) :
        self.api_key = os.environ['BNB_APIKEY']
        self.secret_key = os.environ['BNB_SECRETKEY']
        self.base_url = "https://testnet.binancefuture.com"
        self.header = {"X-MBX-APIKEY":self.api_key}

    def makeGET(self,endpoint,data=None):
        response = requests.get(self.base_url+endpoint,params=data,headers=self.header)
        
        if response.status_code == 200:
            logger.info("Connection established!")
            return response.json()
        else:
            logger.error("Cannot establish connection!")

    def exchangeInfo(self):
        endpoint = "/fapi/v1/exchangeInfo"
        exchange_information = self.makeGET(endpoint)
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

        candleData = self.makeGET(endpoint,data)

        candles = []

        for candle in candleData:
            candles.append([candle[0],candle[1],candle[2],candle[3],candle[4],candle[5]])

        return candles
        