import asyncio
import requests
import time
async def fetch_data():
    await asyncio.sleep(1)
    return "data"

async def forget_await():
    result = fetch_data()  # forget await！
    print("Result:", result)  # the result is a coroutine object!

async def block_task():
    print("Start sleeping...")
    time.sleep(2)  # it will block the event loop!
    # requests.get("https://www.baidu.com") # it will block the event loop!
    print("Done")

async def entry_point_for_block_task():
    await asyncio.gather(block_task(), block_task(), block_task())

async def busy_loop():
    total = 0
    for i in range(10_000_000):
        total += i
    print("Loop done")

async def watcher():
    for _ in range(5):
        print("Still alive...")
        await asyncio.sleep(0.5)

async def entry_point_for_busy_loop():
    await asyncio.gather(busy_loop(), watcher())

if __name__ == "__main__":
    # asyncio.run(forget_await())
    # asyncio.run(entry_point_for_block_task())
    asyncio.run(entry_point_for_busy_loop())