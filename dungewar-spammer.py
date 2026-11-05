# kill $(jobs -p)

import asyncio
import websockets
import json
import random

messages = "hi olgierd, hello olgierd, cheese, cheese beryllium, cheesy beryllium, beryl, hi dungewar, thegrapeape22 is cool, cheeeese, 🧀, thegrapeape22 is awesome, skissue".split(', ')

# messages = ["⢰⣶⣾⢃⠉⢀⣀⣀⣴⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣷⣿⣆⢈⣋⣹⣿⣷⢩\n⣾⣷⣿⣻⡠⣤⣿⣽⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣿⣏⣙⣿⣿⣯⣷\n⡽⣻⢟⣯⢯⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⢟⣿⣿⣿⣿⣿⣿⣿⣿⣽⡿\n⣯⣿⣫⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⢿⣿⣿⣿⣿⣿⣾⢇\n⣿⣛⣿⣷⣿⣿⣿⣿⣿⡿⢿⢻⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢗\n⢿⣿⣿⣿⣿⣿⣿⣿⢯⣠⣘⣸⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⢾\n⣶⣿⣿⣿⣿⣿⣯⣿⣌⣾⣿⣿⣿⡟⢹⣿⢿⣷⣿⣿⡿⠨⣿⣿⣿⣿⣿⣿\n⠙⣿⣿⣿⣿⡿⢟⣽⣿⣿⣿⠟⠛⠃⣀⣺⢿⣯⣯⣭⣥⠀⣿⣿⣿⣿⣿⣿\n⠀⣿⣻⣂⣄⡄⠀⠀⠀⠈⢣⡠⠬⣉⠟⠉⠉⠉⠉⠙⠈⠹⣿⣿⣿⣿⣿⣿\n⠛⠹⠷⣿⣿⠀⠾⠾⠿⠿⠲⠇⠀⢻⡄⠰⠿⠭⠿⠶⡄⠀⢿⣿⣿⣿⣿⣿\n⣀⣀⠀⢏⣀⠀⠀⠀⠀⠀⠘⠀⠀⠘⠏⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿\n⢿⣍⡽⢟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿\n⣷⠚⠒⢒⡇⠀⠀⠀⠀⠰⠆⠠⢤⡶⣄⠇⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿\n⣻⡰⠀⠈⠄⠀⠀⠀⠀⢀⠞⠢⠤⠉⠀⠀⠀⠀⠀⠀⠀⠀⣼⡿⣽⣿⣿⣿\n⡝⢪⠿⣾⣗⠀⠀⠀⣴⣯⡦⠤⠤⣔⣄⠀⠀⠀⠀⠀⠀⢠⣾⡏⣻⣿⣿⣿\n⡠⢤⣄⣏⣊⠂⠀⠀⠉⠉⠒⠖⠒⠚⠛⠂⠀⠀⠀⠀⠀⣸⡟⢱⣿⣿⡿⣿\n⡆⢵⡒⠶⢮⣥⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⣰⢻⣀⣸⣿⣿⣳⡋\n⡇⠙⠤⠤⢀⠉⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠟⡏⠄⠈⣿⣿⣿⡯\n⠀⢑⠀⣀⡘⠀⢳⣦⠀⠀⠀⠀⠀⠀⠀⠀⣄⣠⣶⠋⠀⠑⠋⠤⠚⣿⣿⡇\n⣴⣷⣿⠁⠀⠀⠀⠻⣷⣀⡀⠀⠠⣠⣫⣴⣼⠟⠁⠀⠐⣷⣀⠀⡉⠀⡟⡇\n⣿⣿⣿⡄⠀⠀⠀⠀⠀⠉⠙⠲⠫⠴⠛⠋⠁⠀⠀⠀⠀⣿⣿⣮⣍⡀⢹⠁"]

async def main():
    async with websockets.connect("wss://dungewar.com/ws?token=9bdff71f-6698-486b-a7df-dc9475b54290") as ws:
        while True:
            await ws.send(json.dumps({
                "message": random.choice(messages),
                "messageCount": 15
            }))
            await asyncio.sleep(.1)

asyncio.run(main())
