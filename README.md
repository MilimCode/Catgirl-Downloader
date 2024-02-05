# Catgirl-Downloader
This downloads Catgirls


This Python script asynchronously downloads catgirl images from the nekos.best API. It utilizes aiohttp for asynchronous HTTP requests, aiofiles for asynchronous file operations, and tqdm for progress bars. The script supports concurrent downloads and allows users to specify the number of images to download. It handles interruptions gracefully, ensuring that downloads can be stopped without losing progress.

# Features
Asynchronous downloading of images.
Progress bar for each download.
Concurrent downloads with a customizable limit.
Handles interruptions and errors gracefully.
Clears console upon completion for a clean user experience.
Prerequisites
Before running this script, ensure you have Python 3.7 or later installed on your system. This script uses asyncio, which requires Python 3.7 or higher for optimal performance.

# Dependencies
aiohttp
aiofiles
tqdm
asyncio
aioconsole
These dependencies are required to run the script. You can install them using pip:

pip install aiohttp aiofiles tqdm asyncio aioconsole



# Installation
Clone the repository or download the script to your local machine.
Open your terminal and navigate to the script's directory.
Install the required dependencies as mentioned above.
Usage
To run the script, use the following command in the terminal:

