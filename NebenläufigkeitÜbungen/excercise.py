import asyncio
import time


async def sleeper():
    print("vor dem Warten ", time.strftime("%d.%m.%Y %H:%M:%S"))
    await asyncio.sleep(2)
    print("nach dem Warten ", time.strftime("%d.%m.%Y %H:%M:%S"))
    return

async def main():
    await asyncio.gather(sleeper(), sleeper(),sleeper())


if __name__ == '__main__':
    asyncio.run(main())
