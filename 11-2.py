file = open("day11input.txt")

inp = file.read()
file.close()
inp = inp.split('\n')

test1 = '11111\n19991\n19191\n19991\n11111'.split('\n') # test for 2 steps

# After step 1:
# 34543
# 40004
# 50005
# 40004
# 34543

# After step 2:
# 45654
# 51115
# 61116
# 51115
# 45654

test2 = '5483143223\n2745854711\n5264556173\n6141336146\n6357385478\n4167524645\n2176841721\n6882881134\n4846848554\n5283751526'.split('\n') # test for 10 steps - 204 flashes. 100 steps - total 1656 flashes

class Octopus:
    def __init__(self, energy_level, vector):
        self.energy_level = int(energy_level)
        self.vector = vector
        self.flashes = 0
        self.flashing = False
        self.adjacent = []

    def add_adjacent(self, oct_dict):
        self.adjacent += [x for x in oct_dict.values() if x]
    
    def increase(self):
        self.energy_level += 1
        if self.energy_level > 9:
            if self.flashing is False:
                self.flash()

    def flash(self):
        self.flashing = True
        if self.energy_level > 9:
            for octopus in self.adjacent:
                if octopus.flashing is False:
                    octopus.increase()

    def reset(self):
        if self.energy_level > 9:
            self.energy_level = 0
        if self.flashing is True:
            self.flashes += 1
            self.flashing = False

    def disp(self):
        return self.energy_level

    def return_flashes(self):
        return self.flashes

def octo_grid(list_of_strings):
    octopus_grid = []
    for row in list_of_strings:
        octo_row = []
        for o, e in enumerate(row):
            octo_row.append(Octopus(e, (row, o)))
            # print(f"Octo row now at: {len(octo_row)}")
        # print(f"Will append octo_row {octo_row}")
        octopus_grid.append(octo_row)
        # print(octopus_grid)
    return octopus_grid

def group_octopodes(grid):
    for row, r in enumerate(grid):
        for pos, octopus in enumerate(r):
            directions = {}
            directions['nw'] = grid[row - 1][pos - 1] if bool(row - 1 >= 0 and pos - 1 >= 0) else False
            directions['n'] = grid[row - 1][pos] if bool(row - 1 >= 0) else False
            directions['ne'] = grid[row - 1][pos + 1] if bool(row - 1 >= 0 and pos + 1 <= len(r) - 1) else False
            directions['w'] = grid[row][pos - 1] if bool(pos - 1 >= 0) else False
            directions['e'] = grid[row][pos + 1] if bool(pos + 1 <= len(r) - 1) else False
            directions['sw'] = grid[row + 1][pos - 1] if bool(row + 1 <= len(grid) - 1 and pos - 1 >= 0) else False
            directions['s'] = grid[row + 1][pos] if bool(row + 1 <= len(grid) - 1) else False
            directions['se'] = grid[row + 1][pos + 1] if bool(row + 1 <= len(grid) - 1 and pos + 1 <= len(r) - 1) else False
            octopus.add_adjacent(directions)
        # print(directions)

def display_octopodes(octo_grid):
    res = []
    for row in octo_grid:
        r = []
        for octopus in row:
            # print(octopus.disp())
            r.append(octopus.disp())
        res.append(r)
    return res

def print_grid(grid):
    for row in grid:
        r_copy = []
        for i in row:
            r_copy.append(str(i))
        print(''.join(r_copy))

def increase_octopodes(octo_grid):
    for row in octo_grid:
        for octopus in row:
            octopus.increase()

def absorb_octopodes(octo_grid):
    for row in octo_grid:
        for octopus in row:
            octopus.absorb()

def flash_octopodes(octo_grid):
    for row in octo_grid:
        for octopus in row:
            octopus.flash()

def reset_octopodes(octo_grid):
    for row in octo_grid:
        for octopus in row:
            octopus.reset()

def get_flashes(octo_grid):
    res = 0
    for row in octo_grid:
        for octopus in row:
            res += octopus.return_flashes()
    return res

def all_flashing(octo_grid):
    for row in octo_grid:
        for octopus in row:
            if octopus.flashing is False:
                return False
    return True

def simulate(grid):
    o_grid = octo_grid(grid)
    group_octopodes(o_grid)
    steps = 0
    while all_flashing(o_grid) is False:
        increase_octopodes(o_grid)
        if all_flashing(o_grid):
            return steps + 1
        reset_octopodes(o_grid)
        steps += 1
    
print(simulate(inp))