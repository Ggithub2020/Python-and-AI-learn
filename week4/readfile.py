import os
# Check if the file exists
if os .path.exists("data.txt"):
    print("File exists.")
with open("data.txt", "r") as f:
    content = f.read()
    print(content)
