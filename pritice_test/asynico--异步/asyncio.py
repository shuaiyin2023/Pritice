import asyncio


async def hello():
    print('hello')
    await asyncio.sleep(1)
    print('world')

    return "done"


result = hello()
print(result)
