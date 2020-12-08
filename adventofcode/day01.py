
lines = []
product = []

with open("adventofcode/day01.txt") as inpt:
    for line in inpt:
        lines.append(int(line))

for i in lines:
    for j in lines:
        for f in lines:
            sum = i + j + f
            if sum == 2020:
                print(i*j*f)
