# kill $(jobs -p)

import asyncio
import websockets
import json
import random

messages = "olgierd, rohan, qinzhao li, anuraag, ming, max, mitul, calvin, dungewar, thegrapeape22".split(', ')

async def main():
    async with websockets.connect("wss://dungewar.com/ws") as ws:
        while True:
            await ws.send(json.dumps({
                # "message": "%s [%s]" % (random.choice(messages), asyncio.get_event_loop().time()),
                "message": "%s is gay" % random.choice(messages),
                "messageCount": 15
            }))
            await asyncio.sleep(.2)

asyncio.run(main())
