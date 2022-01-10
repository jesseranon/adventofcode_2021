file = open("day9input.txt")

inp = file.read()
file.close()

inp =  inp.split('\n')
grid = []

for row in inp:
    digits = []
    for x in row:
        digits.append(int(x))
    grid.append(digits)

test = '2199943210\n3987894921\n9856789892\n8767896789\n9899965678'
test_grid = []
for row in test.split('\n'):
    digits = []
    for x in row:
        digits.append(int(x))
    test_grid.append(digits)

print(test_grid)
### find low points
def risk(g):
    # low_points = []
    risk_level = 0
    for i, row in enumerate(g):
        # print(f'in {i} row of grid')
        for f, height in enumerate(row):
            # print(f'in {f} position of row {i}')
            comparators = []
            lowest = True
            #use i for up and down
            #use f for left and right
            if i > 0:
                # print(f'comparing {height} to {g[i-1][f]}')
                comparators.append(g[i-1][f])
            if i <= len(g)-2:
                # print(f'comparing {height} to {g[i+1][f]}')
                comparators.append(g[i+1][f])
            if f > 0:
                # print(f'comparing {height} to {row[f-1]}')
                comparators.append(row[f-1])
            if f < len(row)-1:
                # print(f'comparing {height} to {row[f+1]}')
                comparators.append(row[f+1])
            for c in comparators:
                if height >= c:
                    lowest = False
                    break
            if lowest:
                risk_level += height + 1

    return risk_level

print(risk(grid))

# 24059 too high

##if index > 0
#check left

##if index < len(row)
#check right

##if row > 0
#check up

##if row < len(grid)
#check down

#risk level = low point + 1

#return sum of risk levels of all low points
#risk_level += low_point + 1