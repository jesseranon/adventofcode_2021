file = open("day8input.txt")

inp = file.read()
file.close()

inp  = inp.split('\n')

output_values = [i.split(' | ')[1] for i in inp]

def unique():
    global output_values
    
    res = 0
    for val in output_values:
        for v in val.split(' '):
            if len(v) in {2,3,4,7}:
                res += 1

    return res
print(unique())