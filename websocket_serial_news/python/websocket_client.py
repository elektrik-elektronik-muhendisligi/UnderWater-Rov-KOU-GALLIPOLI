import asyncio
import  websockets

async def message():
    async with websockets.connect("ws://0489ca63-40e7-41f7-b324-d61027b121d5.local:80") as socket:
        msg=input("mesage ilet")
        await socket.send(msg)
        print(await socket.recv())

asyncio.get_event_loop().run_until_complete(message())
#asyncio.get_event_loop().run_forever()