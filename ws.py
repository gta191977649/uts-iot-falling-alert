
# WS server example

import asyncio
import websockets

async def hello(websocket, path):

    greeting = f"Hello !"

    await websocket.send(greeting)
    print(f"> {greeting}")

start_server = websockets.serve(hello, "127.0.0.1", 5432)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()