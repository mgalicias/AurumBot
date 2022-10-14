class IndicesInformation:
    def __init__(self,dataIndices):
        self.symbol = dataIndices['symbol']
        self.askPrice = float(dataIndices['askPrice'])
        self.bidPrice = float(dataIndices['bidPrice'])
        self.lastPrice = float(dataIndices['lastPrice'])
