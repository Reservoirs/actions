import sys
import urllib.request
from pathlib import Path
import re

if len(sys.argv) < 2:
    print("No URLs provided")
    sys.exit(1)

urls = [u.strip() for u in sys.argv[1].split(",") if u.strip()]

if not urls:
    print("No valid URLs")
    sys.exit(1)

# Get filenames
filenames = [
    url.rstrip("/").split("/")[-1]
    for url in urls
]

print("Files:")
for filename in filenames:
    print(f"  {filename}")

# Extract number from the first filename
match = re.match(r"(\d+)", filenames[0])

if not match:
    print(f"Could not find a number at the beginning of: {filenames[0]}")
    sys.exit(1)

number = match.group(1)

branch_name = f"branch_{number}"

# Save branch name for GitHub Actions
with open("branch_name.txt", "w") as f:
    f.write(branch_name)

print(f"Branch name: {branch_name}")

# Download files
for i, url in enumerate(urls, 1):
    filename = url.rstrip("/").split("/")[-1]

    print(f"\n[{i}/{len(urls)}] Downloading:")
    print(url)
    print(f"Saving as: {filename}")

    urllib.request.urlretrieve(url, filename)

    size = Path(filename).stat().st_size / (1024 * 1024)

    print(f"Downloaded: {filename} ({size:.2f} MB)")

print("\nAll files downloaded successfully.")

