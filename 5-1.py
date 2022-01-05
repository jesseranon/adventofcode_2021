file = open("day5input.txt")

inp = file.read()
file.close()

inp = inp.split('\n')
# inp = '419,207 -> 419,109\n300,888 -> 803,385\n104,959 -> 457,959'.split('\n')

plot = {}
vhlines = []

# pull out vertical and horizontal lines
for i in inp:
    i1 = i[:i.find(' ')]
    x1 = i1[:i1.find(',')]
    y1 = i1[i1.find(',')+1:]
    i2 = i[i.rfind(' ')+1:]
    x2 = i2[:i2.find(',')]
    y2 = i2[i2.find(',')+1:]
    if x1 == x2 or y1 == y2:
        vhlines.append([(int(x1),int(y1)),(int(x2),int(y2))])

# generate tuples for points in between
for l in vhlines:
    to_plot = []
    (p1,p2) = l
    (x1,y1) = p1
    (x2,y2) = p2
    if x1 == x2:
        ymax = max(y1,y2)+1
        ymin = min(y1,y2)
        for y in range(ymin, ymax):
            new_point = (x1,y)
            to_plot.append(new_point)
    elif y1 == y2:
        xmax = max(x1,x2)+1
        xmin = min(x1,x2)
        for x in range(xmin, xmax):
            new_point = (x,y1)
            to_plot.append(new_point)
    
    #plot points
    for p in to_plot:
        try:
            plot[p] += 1
        except KeyError:
            plot.update({
                p: 1
            })

res = 0
for point in plot:
    if plot[point] >= 2:
        res += 1

print(res)