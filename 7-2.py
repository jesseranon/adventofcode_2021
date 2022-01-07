file = open("day7input.txt")

inp = file.read()
file.close()

inp = [int(i) for i in inp.split(',')]

hpos = {}

for i in range(max(inp)+1):
    hpos.update({
        i: inp.count(i)
    })

def simulate():
    global hpos
    res = 0
    for i in range(max(hpos)+1):
        # print(f'simulating position {i}')
        fuel = 0
        for pos in hpos:
            # print(f'checking position {pos}')
            fuel += sum(range(abs(i - pos)+1),0) * hpos[pos]
            if res > 0 and fuel > res:
                break
        if res == 0:
            res = fuel
        else:
            res = fuel if fuel < res else res

    return res

print(simulate())