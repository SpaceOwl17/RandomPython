columnnum = 0
tree = 0
with open("adventofcode/day03.txt") as inpt:
    for line in inpt:
        if line == '........#....#..##..#...#.....#\n':
            continue
        columnnum += 3
        if columnnum > 30:
            columnnum -= 33
        if line[columnnum] == '#':
            tree += 1

print(tree)
