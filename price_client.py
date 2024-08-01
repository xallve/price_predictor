import websockets
import pandas as pd


class PriceClient:
    def __init__(self, symbol):
        self.symbol = symbol

    async def connect(self):
        # Get price data and convert it to df to feed to predictor
        # maybe just download small amount of historical data and
        # receive data via own wss and transform it to feed to predictor
        # Dummy
        yield [1,2,3,4]
