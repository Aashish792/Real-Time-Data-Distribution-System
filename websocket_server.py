import asyncio
import websockets

connected_clients = set()

async def register(websocket):
    connected_clients.add(websocket)
    print(f"Registered new client: {websocket.remote_address}")

async def unregister(websocket):
    connected_clients.remove(websocket)
    print(f"Unregistered client: {websocket.remote_address}")

async def handle_websocket(websocket, path):
    await register(websocket)
    try:
        async for message in websocket:
            # Echo message back to all connected clients
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    except websockets.exceptions.ConnectionClosed:
        print("Connection closed")
    finally:
        await unregister(websocket)

start_server = websockets.serve(handle_websocket, "localhost", 8765)

print("WebSocket server started on ws://localhost:8765/")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
