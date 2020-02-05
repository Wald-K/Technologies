import asyncio


async def say(what, when):
    await asyncio.sleep(when)
    print(what)

loop = asyncio.get_event_loop()

loop.create_task(say('Hello first', 3))
loop.create_task(say('Hello second', 1))

# loop.run_forever()
loop.close()