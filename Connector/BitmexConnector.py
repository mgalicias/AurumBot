import logging
import os
from typing import Dict,List

from requests import get,post,delete

from BitmexModels import IndicesInformation

logger = logging.getLogger()


class BitmexConnector:
    def __init__(self) :
        self._base_url = "https://testnet.bitmex.com/api/v1"
        self._secret_key = os.environ['BITMEX_SECRETKEY']
        self._api_key = os.environ['BITMEX_APIKEY']
    
    def _makeGET(self,endpoint,data=None)  :
        endpoint = self._base_url + endpoint
        try:
            response = get(endpoint,params=data)
            return response.json()
        except Exception as e:
            logger.error("Connection not established :: %s",e)
    
    def getIndices(self) -> List[IndicesInformation] :

        response = self._makeGET("/instrument/indices")
        print(response.len())
        index = []
        
        for i in response:
            index.append(IndicesInformation(i))
        
        return index

        