from email import header
import hashlib
import hmac
import logging
import os
from time import time
from urllib.parse import urlencode
import requests
logger = logging.getLogger()

class BinanceConnector:
    def __init__(self) :
        self._api_key = os.environ['BNB_APIKEY']
        self._secret_key = os.environ['BNB_SECRETKEY']
        self._base_url = "https://testnet.binancefuture.com"
        self._header = {"X-MBX-APIKEY":self._api_key}
        self._prices = dict()

    def _getTimestamp(self):
        return int(time()*1000)

    def _generateSignature(self,data=None):
        data['timestamp'] = self._getTimestamp()
        return hmac.new(self._secret_key.encode(),urlencode(data).encode(),hashlib.sha256).hexdigest()

    def _makeGET(self,endpoint=None,data=None):
        response = requests.get(self._base_url+endpoint,params=data,headers=self._header)
        
        try:
            logger.info("Connection established!")
            return response.json()
        except Exception as e :
            logger.error("Cannot establish connection ",e)

    def _makePOST(self,endpoint=None,data=None):
        response = requests.post(self._base_url+endpoint,params=data,headers=self._header)
        
        try:
            logger.info("Connection established!")
            return response.json()
        except Exception as e :
            logger.error("Cannot establish connection ",e)

    def _makeDELETE(self,endpoint=None,data=None):
        response = requests.delete(self._base_url+endpoint,params=data,headers=self._header)
        
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

    def klineCandlestickData(self,symbol=None,interval="1h"):

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
    
    def symbolOrderBooklTicker(self,symbol=None):
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

    def accountInformation(self):
        endpoint = "/fapi/v2/account"
        data = dict()
        data['signature'] = self._generateSignature(data)
        
        dataAccount = self._makeGET(endpoint,data)
        accountInformation = dict()
        for data in dataAccount['assets']:
            accountInformation[data['asset']] = data
        return accountInformation

    def createOrder(self,symbol : str,side : str,type : str,timeInForce : str,quantity : float,price : float ):
        endpoint = "/fapi/v1/order"
        data = dict()
        data['symbol'] = symbol
        data['side'] = side
        data['type'] = type
        data['timeInForce'] = timeInForce
        data['quantity'] = float(quantity)
        data['price'] = float(price)

        data['signature'] = self._generateSignature(data)
        newOrder = self._makePOST(endpoint,data)
        
        logger.info("Order successfully created: %s STATUS: %s",newOrder['orderId'], newOrder['status'])
        
    
    def cancelOrder(self, symbol, orderId ):
        endpoint = "/fapi/v1/order"
        data = dict()
        data['symbol'] = symbol
        data['orderId'] = orderId
        data['signature'] = self._generateSignature(data)

        cancelOrder = self._makeDELETE(endpoint,data)
        logger.info("Order successfully canceled: %s STATUS: %s",cancelOrder['orderId'], cancelOrder['status'])


