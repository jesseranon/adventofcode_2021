file = open("day6input.txt")

inp = file.read()
file.close()

inp = [int(i) for i in inp.split(',')]

def spawn(numdays):
    global inp
    while numdays > 0:
        for i, f in enumerate(inp):
            inp[i] = f - 1
            if inp[i] < 0:
                inp[i] = 6
                inp.append(9)

        numdays -= 1
    return len(inp)


print(spawn(80))