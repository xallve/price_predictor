import asyncio
from threading import Thread
from prediction_service import PredictionService
from websocket_server import start_server

if __name__ == "__main__":
    symbols = ["BTC-USD", "ETH-USD"]  # Add the symbols you want to support
    service = PredictionService("path_to_your_model")
    Thread(target=service.start, args=(symbols,)).start()
    asyncio.run(start_server())
