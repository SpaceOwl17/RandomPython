
words = []
highlow = []
numright = 0
with open("adventofcode/day02.txt") as inpt:
    for line in inpt:
        words = line.split(" ")
        highlow = words[0].split("-")

        lowestnumletters = int(highlow[0])
        highestnumletters = int(highlow[1])

        letters = words[1]
        letter = letters[0]

        numletters = 0
        for char in (words[2]):
            if char == letter:
                numletters += 1
        
        if numletters <= highestnumletters and numletters >= lowestnumletters:
            numright += 1

print(numright)