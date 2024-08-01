from predictor import Predictor
from price_client import PriceClient
import asyncio
import json
from datetime import datetime, timedelta
from websocket_server import broadcast


class PredictionService:
    def __init__(self, path_to_model):
        self.predictor = Predictor(path_to_model)

    async def fetch_data_and_predict(self, symbol):
        client = PriceClient(symbol)
        data = []
        async for collectable in client.connect():
            data.append(collectable)
            if len(data) >= 60:  # Assume we want to use the last 60 data points for prediction
                data = data[-60:]
                predictions = self.predictor.predict(data)
                await broadcast(symbol, json.dumps(predictions))
                await asyncio.sleep(60 - datetime.utcnow().second)  # Wait for the next minute

    def start(self, symbols):
        loop = asyncio.get_event_loop()
        for symbol in symbols:
            loop.create_task(self.fetch_data_and_predict(symbol))
        loop.run_forever()
