import logging
import os
from typing import Dict,List


from requests import delete, get, post

from testingModels.models import *

logger = logging.getLogger()


class BinanceConnector():
    def __init__(self):
        self._base_url = "https://testnet.binancefuture.com"
        self._api_key = os.environ['BNB_APIKEY']
        self._secret_key = os.environ['BNB_SECRETKEY']
        self._header = {'X-MBX-APIKEY':self._api_key}
        
    def _makeGET(self,endpoint :str,data :Dict):
        endpoint = self._base_url + endpoint
        
        try:
            response = get(endpoint,params=data,headers=self._header)
            return response.json()
        except Exception as e:
            logger.error("CRITICAL ERROR :: %s",e)

    def _makePOST(self,endpoint :str,data :Dict):
        endpoint = self._base_url + data
        
        try:
            response = post(endpoint,params=data,headers=self._header)
            return response.json()
        except Exception as e:
            logger.error("CRITICAL ERROR :: %s",e)
    
    def _makeDELETE(self,endpoint :str,data :Dict):
        endpoint = self._base_url + data
        
        try:
            response = delete(endpoint,params=data,headers=self._header)
            return response.json()
        except Exception as e:
            logger.error("CRITICAL ERROR :: %s",e)

    def exchangeInformation(self) -> Dict["str",ExchangeInformation]:
        endpoint = "/fapi/v1/exchangeInfo"    
        exchangeData = self._makeGET(endpoint,dict())
        exchangeInformation = dict()
        for data in exchangeData['symbols']:
            exchangeInformation[data['pair']] = ExchangeInformation(data)
        
        return exchangeInformation
    
    def klineCandlestickData(self,symbol :str, interval :str="1h") -> List[KlineCandlestickData]:
        data = dict()
        data['symbol'] = symbol
        data['interval'] = interval
        data['limit'] = 1000
        candleInfo = self._makeGET("/fapi/v1/klines",data)
        candleData = []
        
        for candle in candleInfo:
            candleData.append(KlineCandlestickData(candle))
        return candleData

