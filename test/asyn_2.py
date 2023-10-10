import asyncio
import time


async def display(num):
    await asyncio.sleep(1)
    # time.sleep(1)
    print(num)


def main():
    start = time.time()
    objs = [display(i) for i in range(1, 4)]
    for obj in objs:
        asyncio.run(obj)
    end = time.time()
    print(f'{end - start:.3f}秒')

if __name__ == '__main__':
    main()