from typing import Dict,List 

class ExchangeInformation:
    def __init__(self,data :Dict):
        self._pair = data['pair']
        self._baseAsset = data['baseAsset']
        self._quoteAsset = data['quoteAsset']
        self._pricePrecision = data['pricePrecision']
        self._quantityPrecision = data['quantityPrecision']
       
    
    def getPair(self): return self._pair
    def getBaseAsset(self): return self._baseAsset
    def getQuoteAsset(self): return self._quoteAsset
    def getPricePrecision(self): return self._pricePrecision
    def getQuantityPrecision(self): return self._quantityPrecision
    

class Kline:
    def __init__(self,data :List) -> None:
        self._open = data[0]