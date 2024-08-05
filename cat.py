import os, aiohttp, aiofiles, asyncio
from urllib.parse import urlparse
from tqdm.asyncio import tqdm_asyncio
from aioconsole import ainput

async def downloadImage(session, folder, stopEvent, semaphore, downloaded):
    try:
        async with session.get("https://nekos.best/api/v2/neko") as resp:
            imageUrl = (await resp.json())["results"][0]["url"]
            filePath = os.path.join(folder, os.path.basename(urlparse(imageUrl).path))
            if filePath in downloaded: return
            async with semaphore, session.get(imageUrl) as imgResp, aiofiles.open(filePath, 'wb') as file:
                bar = tqdm_asyncio(total=int(imgResp.headers.get('content-length', 0)), unit='B', unit_scale=True, unit_divisor=1024, desc=f"Downloading {os.path.basename(filePath)}")
                async for chunk in imgResp.content.iter_any():
                    bar.update(len(chunk)), await file.write(chunk)
                    if stopEvent.is_set(): break
                bar.close(), downloaded.add(filePath)
                if not stopEvent.is_set(): print(f"\n\033[92mImage downloaded to {filePath}\033[0m")
    except Exception as e: print(f"Error: {e}")

async def main():
    folder, stopEvent, downloaded = "Catgirls", asyncio.Event(), set()
    os.makedirs(folder, exist_ok=True)
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                sem = asyncio.Semaphore(10)
                await asyncio.gather(*(downloadImage(session, folder, stopEvent, sem, downloaded) for _ in range(int(await ainput("How many catgirl images would you like to download? ")))))
            os.system('cls' if os.name == 'nt' else 'clear')
        except (KeyboardInterrupt, ValueError): stopEvent.set(), print("\nCtrl+C pressed. Stopping download..." if isinstance(_, KeyboardInterrupt) else "Please enter a valid number.")

if __name__ == "__main__":
    asyncio.run(main())
