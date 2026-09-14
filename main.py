import sys
import urllib.request
from pathlib import Path

url = sys.argv[1]

filename = url.split("/")[-1].split("?")[0]

if not filename:
    filename = "downloaded_file"

print(f"Downloading: {url}")
print(f"Filename: {filename}")

urllib.request.urlretrieve(url, filename)

print(f"Downloaded successfully: {filename}")
