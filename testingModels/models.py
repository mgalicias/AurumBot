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
    

class KlineCandlestickData:
    def __init__(self,data :List):
        self._openTime = data[0]
        self._open = data[1]
        self._high = data[2]
        self._low = data[3]
        self._close = data[4]
        self._volume = data[5]

    def getOpenTime(self): return self._openTime
    def getOpen(self): return  self._open
    def getHigh(self): return  self._high
    def getLow(self): return  self._low
    def getClose(self): return self._close
    def getVolume(self): return  self._volume


class PriceTicker:
    def __init__(self,data :Dict):
        self._symbol = data['symbol']
        self._price = data['price']
    
    def getSymbol(self): return self._symbol
    def getPrice(self): return self._price
 