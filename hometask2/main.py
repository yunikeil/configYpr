import asyncio

async def main():
    print('hello')
    await asyncio.sleep(10)
    print('world')

async def main1():
    print('Hello World')


asyncio.run(main())
asyncio.run(main1())

