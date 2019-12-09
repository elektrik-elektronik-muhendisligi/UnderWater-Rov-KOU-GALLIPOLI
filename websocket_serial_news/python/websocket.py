import asyncio
import  websockets

async def response(websocket,path):

    message=await websocket.recv()
    print("message : {}".format(message))
    await websocket.send("Benim mesajım")

start_server=websockets.serve(response,"0489ca63-40e7-41f7-b324-d61027b121d5.local",port=80)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()