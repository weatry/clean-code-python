import asyncio
import logging

logger = logging.getLogger(__name__)

q = asyncio.Queue(maxsize=3)
async def producer():
    for i in range(5):
        item = f"item-{i}"
        await q.put(item)
        logger.info("produced %s", item)
        await asyncio.sleep(0.1)

async def consumer(name):
    while True:
        try:
            item = await asyncio.wait_for(q.get(), timeout=2) # wait for 2 seconds
            logger.info("%s got %s", name, item)
            q.task_done()
        except asyncio.TimeoutError:
            logger.info("%s timeout", name)
            break

async def main():
    await asyncio.gather(
        producer(),
        consumer("C1"),
        consumer("C2")
    )

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, 
        format="%(asctime)s %(filename)s %(levelname)s:%(message)s"
    )

    asyncio.run(main())