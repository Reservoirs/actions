import sys

number = sys.argv[1]

with open("result.txt", "w") as f:
    f.write(f"Entered number: {number}\n")

print(f"Saved result: {number}")
