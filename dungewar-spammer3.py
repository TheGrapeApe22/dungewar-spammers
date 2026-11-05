import asyncio
import websockets
import json
import random
import socket

messages = "hi olgierd, hello olgierd, cheese, cheese beryllium, cheesy beryllium, beryl, hi dungewar, thegrapeape22 is cool, cheeeese, 🧀, thegrapeape22 is awesome, skissue".split(', ')

local_ips = ["192.168.1.101", "192.168.1.102"]  # Your local IPs

async def send_messages(local_ip):
    url = "wss://dungewar.com/ws"

    # Create a custom socket and bind it to the local IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((local_ip, 0))  # Port 0 = OS chooses free port

    # Connect WebSocket using this bound socket
    async with websockets.connect(url, sock=sock) as ws:
        for i in range(1):
            message_data = {
                "message": random.choice(messages),
                "messageCount": 15
            }
            await ws.send(json.dumps(message_data))
            print(f"Sent via {local_ip}: {message_data}")
            await asyncio.sleep(0.5)

async def main():
    tasks = []
    for ip in local_ips:
        tasks.append(asyncio.create_task(send_messages(ip)))

    await asyncio.gather(*tasks)

asyncio.run(main())
