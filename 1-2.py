# https://adventofcode.com/2021/day/1/input

file = open("day1input.txt")

inp = file.read()
file.close()

g = inp.split('\n')
count = 0
# print(len(g))
for x in range(1, len(g)-2):
    if int(g[x]) + int(g[x+1]) + int(g[x+2]) > int(g[x-1]) + int(g[x]) + int(g[x+1]):
        count += 1

print(count)