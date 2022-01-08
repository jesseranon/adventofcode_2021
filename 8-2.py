file = open("day8input.txt")

inp = file.read()
file.close()

output_values  = inp.split('\n')

test = "fgcae ebafc cabdef eg abecfg abgfed feg gafdc bceg ebgcadf | defagbc faecg cfdag gecb"

def decode(s): #s for signal
    segments = {x: '' for x in ['top', 'ul', 'ur', 'mid', 'bl', 'br', 'low']}
    signal_buffer = [x for x in s.split(' | ')[0].split(' ')]
    output_buffer = [x for x in s.split(' | ')[1].split(' ')]
    numbers_buffer = {x: '' for x in range(10)}
    # compare numbers to decode segments
    numbers_buffer[1] = ''.join([x for x in signal_buffer if len(x) == 2])
    numbers_buffer[4] = ''.join([x for x in signal_buffer if len(x) == 4])
    numbers_buffer[7] = ''.join([x for x in signal_buffer if len(x) == 3])
    numbers_buffer[8] = ''.join([x for x in signal_buffer if len(x) == 7])
    five = [x for x in signal_buffer if len(x) == 5]
    segments['top'] = ''.join(c for c in numbers_buffer[7] if c not in numbers_buffer[1])
    bllow = ''.join(c for c in numbers_buffer[8] if c not in numbers_buffer[4]+segments['top'])
    for i, f in enumerate(five):
        check = ''.join(c for c in f if c not in numbers_buffer[1])
        if len(check) == 3:
            numbers_buffer[3] = five.pop(i)
            break
    segments['low'] = ''.join(c for c in numbers_buffer[3] if c not in numbers_buffer[4]+segments['top'])
    segments['bl'] = ''.join(c for c in bllow if c not in segments['low'])
    segments['mid'] = ''.join(c for c in numbers_buffer[3] if c not in numbers_buffer[1]+segments['top']+segments['low'])
    for i, f in enumerate(five):
        check = ''.join(c for c in f if c not in ''.join(segments.values()))
        if len(check) == 1:
            numbers_buffer[2] = five.pop(i)
            segments['ur'] = check
            break
    numbers_buffer[5] = five.pop()
    numbers_buffer[0] = ''.join(c for c in numbers_buffer[8] if c not in segments['mid'])
    numbers_buffer[6] = ''.join(c for c in numbers_buffer[8] if c not in segments['ur'])
    numbers_buffer[9] = ''.join(c for c in numbers_buffer[8] if c not in segments['bl'])

    res = ''

    for x in output_buffer:
        for n, s in numbers_buffer.items():
            if len(x) == len(s) and all([c in x for c in s]):
                res += str(n)
                break

    return int(res)

o_res = 0
for o in output_values:
    o_res += decode(o)
print(o_res)