import os
import aiohttp
import aiofiles
import asyncio
from urllib.parse import urlparse
from tqdm import tqdm
from tqdm.asyncio import tqdm_asyncio
from aioconsole import ainput

# ANSI escape codes for colors
GREEN = "\033[92m"
RESET = "\033[0m"

def clear_console():
    # Clear console command for Windows and other platforms
    os.system('cls' if os.name == 'nt' else 'clear')

async def download_image(session, folder_name, stop_event, semaphore, downloaded_files):
    try:
        async with session.get("https://nekos.best/api/v2/neko") as resp:
            resp.raise_for_status()  # Raise an HTTPError for bad requests
            data = await resp.json()
            image_url = data["results"][0]["url"]

            # Extract the filename from the URL
            file_name = os.path.join(folder_name, os.path.basename(urlparse(image_url).path))

            # Skip download if the file has already been downloaded
            if file_name in downloaded_files:
                return

            # Download the image with a progress bar
            async with semaphore, session.get(image_url) as response, aiofiles.open(file_name, 'wb') as file:
                response.raise_for_status()  # Raise an HTTPError for bad requests

                # Get the content length for tqdm progress bar
                total_size = int(response.headers.get('content-length', 0))

                # Create tqdm manually
                bar = tqdm_asyncio(total=total_size, unit='B', unit_scale=True, unit_divisor=1024,
                                   desc=f"Downloading {os.path.basename(file_name)}")

                async for data in response.content.iter_any():  # Use iter_any without arguments
                    bar.update(len(data))
                    await file.write(data)

                    # Check if the stop event is set (Ctrl+C pressed)
                    if stop_event.is_set():
                        break

                bar.close()

                if stop_event.is_set():
                    tqdm.write(f"\nDownload interrupted. Returning to prompt.")
                else:
                    downloaded_files.add(file_name)  # Add the file to the set of downloaded files
                    tqdm.write(f"\n{GREEN}Image downloaded to {file_name}{RESET}")

    except aiohttp.ClientError as e:
        tqdm.write(f"Error during the request: {e}")
    except (KeyError, IndexError) as e:
        tqdm.write(f"Error in processing API response: {e}")
    except Exception as e:
        tqdm.write(f"An unexpected error occurred: {e}")

async def main():
    while True:
        # Ensure the folder exists
        folder_name = "Catgirls"
        os.makedirs(folder_name, exist_ok=True)

        # Create an event to signal when to stop downloading
        stop_event = asyncio.Event()

        # Initialize the set of downloaded files
        downloaded_files = set()

        try:
            # Prompt user for the number of images to download
            num_images = int(await ainput("How many catgirl images would you like to download? "))

            # Handle Ctrl+C to stop the download
            async with aiohttp.ClientSession() as session:
                semaphore = asyncio.Semaphore(10)  # Limit to 10 concurrent downloads
                tasks = [download_image(session, folder_name, stop_event, semaphore, downloaded_files) for _ in range(num_images)]

                # Run download tasks concurrently
                await asyncio.gather(*tasks)

                # Clear the console when download is complete
                clear_console()

        except KeyboardInterrupt:
            # Ctrl+C pressed, set the stop event
            tqdm.write("\nCtrl+C pressed. Stopping download...")
            stop_event.set()
            continue
        except ValueError:
            tqdm.write("Please enter a valid number.")
            continue

if __name__ == "__main__":
    asyncio.run(main())
