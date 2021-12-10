# https://adventofcode.com/2021/day/2/input

file = open("day2input.txt")

inp = file.read()
file.close()

g = inp.split('\n')
depth = 0
horiz = 0

for line in g:
    match line.split():
        case ['forward', num]:
            horiz += int(num)
        case ['up', num]:
            depth -= int(num)
        case ['down', num]:
            depth += int(num)

print(depth * horiz)