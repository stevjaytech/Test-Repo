stuff = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

count = dict()

for lines in stuff:
    words = lines.split()

    for word in words:
        count[word] = count.get(word, 0)+1

# print(count)

big_word = None
big_count = None

for k, w in count.items().__reversed__():
    if big_word is None or w > big_count:
        big_count = w
        big_word = k

print("{}: {}".format(big_word, big_count))
