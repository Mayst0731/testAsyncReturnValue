import time
import asyncio
import aiohttp

async def start_crawl():
    session = aiohttp.ClientSession()
    category_list = await asyncio.sleep(1)
    course_list = await asyncio.sleep(1)
    detail_list = await asyncio.sleep(1)
    await session.close()
    return {"categories":1,
            "courses":2,
            "details":3}

def handler(event, context):
    results = asyncio.run(start_crawl())
    print(results)
    return results

handler("","")