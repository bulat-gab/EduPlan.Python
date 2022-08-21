import signal

import aiohttp
import asyncio


async def check(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"{url}: status -> {response.status}")
            html = await response.text()
            print(f"{url}: type -> {html[:17].strip()}")

async def main():
    await asyncio.gather(
        check("https://realpython.com"),
        check("https://pycoders.com"),
    )

# asyncio.run(main())

# asyncio.get_event_loop().run_until_complete(main())

# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# loop.run_until_complete(main())



async def stop(*args):
    await asyncio.sleep(1)
    asyncio.get_running_loop().stop()

def signal_handler(*args):
    # logger.info("Disconnecting...")
    # asyncio.create_task(nc.close())
    asyncio.create_task(stop())

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(main())
        loop.run_forever()
    finally:
        loop.close()
