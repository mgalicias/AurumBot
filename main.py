from asyncio.log import logger
import logging
from pprint import pprint

from Connector.BinanceConnector import BinanceConnector

logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter(" %(asctime)s %(levelname)s :: %(message)s ")

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler("/data/log/AurumBot.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

if __name__ == '__main__':
    logger.info("Starting application")
    bnb = BinanceConnector()
    #pprint(bnb.klineCandlestickData("BTCUSDT","15m"))
    #pprint(bnb.symbolOrderBooklTicker("BTCUSDT"))
    #pprint(bnb.accountInformation())
    #bnb.createOrder("BTCUSDT","BUY","LIMIT","GTC",0.005,19000)
    #bnb.cancelOrder("BTCUSDT",3236457696)
    #bnb.queryOrder("BTCUSDT",3236457696)