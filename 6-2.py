file = open("day6input.txt")

inp = file.read()
file.close()

fish = {}

inp = [int(i) for i in inp.split(',')]

for f in range(9):
    if f in inp:
        fish.update({
            f: inp.count(f)
        })
    else:
        fish.update({
            f: 0
        })

def spawn():
    global fish
    buffer = sorted([(k,v) for (k,v) in fish.items()],reverse=True)
    for i, num in buffer:
        if i > 0:
            try:
                fish[i-1] = num
            except KeyError:
                fish.update({
                    i-1: num
                })
        else:
            try:
                fish[8] = num
            except KeyError:
                fish.update({
                    8: num
                })
            try:
                fish[6] += num
            except KeyError:
                fish.update({
                    6: num
                })

def simulate(days):
    global fish
    while days > 0:
        spawn()
        days -= 1
    res = 0
    for x in fish.values():
        res += x
    return res

print(simulate(256))