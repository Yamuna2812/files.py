with open("example.txt", "r") as file:
    text = file.read()
    words = text.split()
    print("Word count:", len(words))
