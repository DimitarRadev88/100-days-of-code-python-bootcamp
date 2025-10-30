file = open("my_file.txt")
content = file.read()

print(content)
file.close()

with open("my_file.txt", mode="w") as file:
    file.write("New text.")

with open("my_file.txt", mode="a") as file:
    file.write("More text.")

with open("my_file.txt") as file:
    content = file.read()
    print(content)

with open("/home/dimitar-radev/Desktop/new_file.txt", mode="w") as file:
    file.write("new file")

with open("../../../../dimitar-radev/Desktop/new_file.txt") as file:
    content = file.read()
    print(content)