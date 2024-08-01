import asyncio
import json
import websockets
from vars import symbol_subscriptions, clients


async def register(websocket):
    try:
        message = await websocket.recv()
        params = json.loads(message)
        symbol = params.get("symbol")
        if symbol:
            if symbol not in symbol_subscriptions:
                symbol_subscriptions[symbol] = set()
            symbol_subscriptions[symbol].add(websocket)
            clients[websocket] = symbol
            await websocket.send(json.dumps({"status": "subscribed", "symbol": symbol}))
        await websocket.wait_closed()
    finally:
        if websocket in clients:
            symbol = clients[websocket]
            symbol_subscriptions[symbol].remove(websocket)
            del clients[websocket]


async def broadcast(symbol ,message):
    if symbol in symbol_subscriptions:
        await asyncio.wait([client.send(message) for client in symbol_subscriptions[symbol]])


async def start_server():
    server = await websockets.serve(register, "localhost", 6789)
    await server.wait_closed()