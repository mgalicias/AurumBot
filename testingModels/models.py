from typing import Dict

class ExchangeInformation:
    def __init__(self,data :Dict):
        self.pair = data['pair']
        self.baseAsset = data['baseAsset']
        self.quoteAsset = data['quoteAsset']
        self.pricePrecision = data['pricePrecision']
        self.quantityPrecision = data['quantityPrecision']
        self.filters = data['filters']
        
        