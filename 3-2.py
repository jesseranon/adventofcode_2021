# https://adventofcode.com/2021/day/3/input

file = open("day3input.txt")

inp = file.read()
file.close()

# gamma = '' # most common
# epsilon = '' # least common

o2 = inp.split('\n')
co2 = o2.copy()

ratings = {
    'o2': o2,
    'co2': co2
}

for rating in list(ratings.keys()):
    bits = ratings[rating]
    for i in range(0,len(bits[0])):
        if len(bits) > 1:
            print(i)
            itotal = 0
            for b in bits:
                itotal += int(b[i])
            if itotal >= len(bits)/2:
                if rating == 'o2':
                    bits = list(filter(lambda x: x[i] == '1', bits))
                else:
                    bits = list(filter(lambda x: x[i] == '0', bits))
            else:
                if rating == 'o2':
                    bits = list(filter(lambda x: x[i] == '0', bits))
                else:
                    bits = list(filter(lambda x: x[i] == '1', bits))
        else:
            break

    ratings[rating] = bits[0]

print(ratings['o2'], ratings['co2'])

decimals = {
    ratings['o2']: 0,
    ratings['co2']: 0
}

for binary in list(decimals.keys()):
    steps = -1
    for x in range(len(binary)-1,-1,-1):
        steps += 1
        decimals[binary] += int(binary[x])*(2**steps)
print(decimals[ratings['o2']]*decimals[ratings['co2']])
