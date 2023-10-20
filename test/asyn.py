import asyncio
import time

now = lambda : time.time()

async def dosomething(num):
    print(f'第{num}任务，第一步')
    await asyncio.sleep(2)
    print(f'第{num}任务，第二步')

if __name__ == '__main__':
    start = now()
    tasks = [dosomething(i) for i in range(5)]
    asyncio.run(asyncio.wait(tasks))
    print('Time: ', now() - start)

