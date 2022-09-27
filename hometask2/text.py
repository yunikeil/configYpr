"""import gevent.monkey

from urllib.request import urlopen

gevent.monkey.patch_all()

urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']


def print_head(url):
    print('Starting {}'.format(url))

    data = urlopen(url).read()

    print('{}: {} bytes: {}'.format(url, len(data), data))


jobs = [gevent.spawn(print_head, _url) for _url in urls]

gevent.wait(jobs)"""




"""import asyncio
import time


async def fun1(x):
    print(x**2)
    await asyncio.sleep(3)
    print('fun1 завершена')


async def fun2(x):
    print(x**0.5)
    await asyncio.sleep(3)
    print('fun2 завершена')


async def main():
    task1 = asyncio.create_task(fun1(4))
    task2 = asyncio.create_task(fun2(4))

    await task1
    await task2


print(time.strftime('%X'))

asyncio.run(main())

print(time.strftime('%X'))"""





