# https://adventofcode.com/2021/day/3/input

file = open("day3input.txt")

inp = file.read()
file.close()

gamma = ''
epsilon = ''

bits = inp.split('\n')

for i in range(0,len(bits[0])):
    itotal = 0
    for b in bits:
        itotal += int(b[i])
    if itotal >= len(bits)/2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

decimals = {
    gamma: 0,
    epsilon: 0
}

for binary in list(decimals.keys()):
    steps = -1
    for x in range(len(binary)-1,-1,-1):
        steps += 1
        decimals[binary] += int(binary[x])*(2**steps)
print(decimals[gamma]*decimals[epsilon])
