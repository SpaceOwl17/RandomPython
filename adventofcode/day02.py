
words = []

with open("adventofcode/day02.txt") as inpt:
    for line in inpt:
        words = inpt.split(": ")
        print(words)