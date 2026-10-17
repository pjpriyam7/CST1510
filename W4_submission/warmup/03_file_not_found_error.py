# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.
try:
    with open("records.txt") as f:
        print(f.read())
except FileNotFoundError:
    print(f"Error file does not exist")
