import sys
import urllib.request
from pathlib import Path

if len(sys.argv) < 2:
    print("No URLs provided")
    sys.exit(1)

urls = sys.argv[1].split(",")

for i, url in enumerate(urls, 1):
    url = url.strip()

    if not url:
        continue

    filename = url.rstrip("/").split("/")[-1]

    print(f"[{i}/{len(urls)}] Downloading:")
    print(url)
    print(f"Saving as: {filename}")

    urllib.request.urlretrieve(url, filename)

    size = Path(filename).stat().st_size / (1024 * 1024)

    print(f"Downloaded: {filename} ({size:.2f} MB)")
    print("-" * 50)
