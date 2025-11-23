import asyncio
async def cpu_bound_task():
    total = 0
    times = 1_000_000_000 # increase this number if the other thread has no starvation.

    for i in range(times):
        total += i * i   # cpu-bound operation，no await, will block the event loop
        if i % 1_000_000 == 0:
            await asyncio.sleep(0)    
    print("Finished")
    return total

async def heartbeat():
    while True:
        print("Still alive!")
        await asyncio.sleep(1)

async def main():
    task = asyncio.create_task(cpu_bound_task())
    await heartbeat()
    await task

if __name__ == "__main__":
    asyncio.run(main())