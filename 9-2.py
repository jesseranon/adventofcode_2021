file = open("day9input.txt")

inp = file.read()
file.close()

inp =  inp.split('\n')

grid = []
for row in inp:
    digits = [int(x) for x in row]
    grid.append(digits)

test = '2199943210\n3987894921\n9856789892\n8767896789\n9899965678'
test_grid = []
for row in test.split('\n'):
    digits = [int(x) for x in row]
    test_grid.append(digits)

##### to-do
# add method to Basin to automatically run get_flow() until results come back all False

def low(g, height, row, pos):
    comps = []
    comps.append(height < g[row - 1][pos] if row - 1 >= 0 else True)
    comps.append(height < g[row + 1][pos] if row + 1 <= len(g) - 1 else True)
    comps.append(height < g[row][pos - 1] if pos - 1 >= 0 else True)
    comps.append(height < g[row][pos + 1] if pos + 1 <= len(g[row]) - 1 else True)
    return all(comps)

class Point:
    def __init__(self, height, vector):
        self.point = {
            'height': height,
            'vector': vector,
            'flow': []
        }

    def get_flow(self, g):
        height = self.point['height']
        row = self.point['vector'][0]
        pos = self.point['vector'][1]
        directions = {}
        directions['n'] = Point(g[row - 1][pos], (row - 1, pos)) if bool(row - 1 >= 0 and height < g[row - 1][pos] and g[row - 1][pos] < 9) else False
        directions['s'] = Point(g[row + 1][pos], (row + 1, pos)) if bool(row + 1 <= len(g) - 1 and height < g[row + 1][pos] and g[row + 1][pos] < 9) else False
        directions['w'] = Point(g[row][pos - 1], (row, pos - 1)) if bool(pos - 1 >= 0 and height < g[row][pos - 1] and g[row][pos - 1] < 9) else False
        directions['e'] = Point(g[row][pos + 1], (row, pos + 1)) if bool(pos + 1 <= len(g[0]) - 1 and height < g[row][pos + 1] and g[row][pos + 1] < 9) else False
        
        self.point['flow'] += [v.get_flow(g) for v in directions.values() if v]
        return self
        
    def disp(self):
        res = [self.point['vector']]
        for f in self.point['flow']:
            res += f.disp()
        return res

class Basin:
    def __init__(self, g, low_point):
        self.grid = g
        self.low_point = low_point
        self.flow = []
    
    def fill(self):
        self.low_point.get_flow(self.grid)
        d = self.low_point.disp()
        self.flow += set(d)

    def return_length(self):
        self.fill()
        return len(self.flow)
        
### find low points
def plot(g):
    basins = []
    for r, row in enumerate(g):
        # print(f'in {i} row of grid')
        for pos, height in enumerate(row):
            # print(f'in {f} position of row {i}')
            if low(g, height, r, pos):
                basins.append(Basin(g, Point(height, (r, pos))))
    print(f"There are {len(basins)} low points in the grid")
    return basins

def solve(g):
    basins = plot(g)
    lengths = [b.return_length() for b in basins]
    lengths.sort()
    print(lengths)
    res = 1
    for l in lengths[-3:]:
        res *= l
    return res

print(solve(grid))