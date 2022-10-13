class AccountInformation:
    def __init__(self,dataAccount) :
        

        self.totalInitialMargin = float(dataAccount['totalInitialMargin'])
        self.totalMaintMargin = float(dataAccount['totalMaintMargin'])
        self.totalWalletBalance = float(dataAccount['totalWalletBalance'])
        self.totalUnrealizedProfit = float(dataAccount['totalUnrealizedProfit'])
        

class OrderStatus:
    def __init__(self, dataOrder):
        
        self.orderId = dataOrder['orderId']
        self.side = dataOrder['side']
        self.status = dataOrder['status']
        self.avgPrice = float(dataOrder['avgPrice'])
        

class KlineCandlestickData:
    def __init__(self,candleData):
        self.opentime = candleData[0]
        self.openCandle = float(candleData[1])
        self.highCandle = float(candleData[2])
        self.lowCandle = float(candleData[3])
        self.closeCandle = float(candleData[4])
        self.volumeCandle = float(candleData[5])

class ExchangeInformation:
    def __init__(self, dataContract):
    
        self.symbol = dataContract['symbol']
        self.baseAsset = dataContract['baseAsset']
        self.quoteAsset = dataContract['quoteAsset']
        self.pricePrecission = dataContract['pricePrecision']
        self.quantityPrecission = dataContract['quantityPrecision']


        