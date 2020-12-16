columnnum = 0
linenum = 0
tree = 0
tree1 = 0
tree2 = 0
tree3 = 0
tree4 = 0
with open("adventofcode/day03test.txt") as inpt:
    for line in inpt:
        if linenum == 0:
            linenum += 1
            continue
        columnnum += 3
        if columnnum >= 31:
            columnnum -= 31
        if line[columnnum] == '#':
            tree += 1
    linenum = 0

    for line in inpt:
        if line == 0:
            linenum += 1
            continue
        columnnum += 1
        if columnnum >= 31:
            columnnum -= 31
        if line[columnnum] == '#':
            tree1 += 1
    linenum = 0

    for line in inpt:
        if line == 0:
            linenum += 1
            continue
        columnnum += 5
        if columnnum >= 31:
            columnnum -= 31
        if line[columnnum] == '#':
            tree2 += 1
    linenum = 0

    for line in inpt:
        if line == 0:
            linenum += 1
            continue
        columnnum += 7
        if columnnum >= 31:
            columnnum -= 31
        if line[columnnum] == '#':
            tree3 += 1
    
    linenum = 0
    for line in inpt:
        if linenum == 0:
            linenum += 1
            continue
        columnnum += 1
        if columnnum >= 31:
            columnnum -= 31
        if line[columnnum] == '#':
            tree4 += 1
        linenum -= 1

print(tree * tree1 * tree2 * tree3 *tree4)
