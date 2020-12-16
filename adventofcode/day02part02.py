words = []
firstsecchar = []
numright = 0
with open("adventofcode/day02.txt") as inpt:
    for line in inpt:
        words = line.split(" ")
        password = words[2]
        firstsecchar = words[0].split("-")

        firstnumletters = int(firstsecchar[0]) - 1
        secondnumletters = int(firstsecchar[1]) - 1

        letters = words[1]
        letter = letters[0]

        numletters = 0
        numtimes = 0
        while numtimes <= 1:
            firstright = 0
            secondright = 0
            if numtimes == 0:
                if password[firstnumletters] == letter:
                    firstright = 1
            if numtimes == 1:
                if password[secondnumletters] == letter:
                    secondright = 1
                    numtimes = 0
            
            if firstright == 1 and secondright == 1:
                numright += 1
                numtimes += 1


print(numright)