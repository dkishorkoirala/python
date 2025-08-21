with open("fl2.png", "rb") as src:
    content = src.read()

with open("copy.png", "wb") as dest:
    dest.write(content)

print("Image copied successfully!!!")