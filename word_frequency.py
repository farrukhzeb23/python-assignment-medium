from collections import Counter

try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        words = content.split()
        print(dict(Counter(words)))
except FileNotFoundError as error:
    print(error)
