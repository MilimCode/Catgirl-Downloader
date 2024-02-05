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
https://www.python.org/downloads/



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

python cat.py

or open the Start.bat file

After running the command, you will be prompted to enter the number of catgirl images you wish to download. The script will then begin downloading the images to a folder named Catgirls in the script's directory.

# Handling Interruptions
If you need to stop the download process, simply press Ctrl+C. The script will gracefully handle the interruption and stop further downloads.

# Notes
The script creates a folder named Catgirls in its directory to store downloaded images.
Ensure you have a stable internet connection to avoid download interruptions or errors.
The script limits the number of concurrent downloads to 10 to avoid overwhelming the server or your network connection. You can adjust this limit in the script if necessary.

