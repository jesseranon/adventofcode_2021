# https://adventofcode.com/2021/day/4/input
import re

file = open("day4input.txt")

inp = file.read()
file.close()

inp = inp.split('\n\n')
draws = inp.pop(0).split(',')
boards = []
last_draw = ''
regex = 'XX'
bingo = False

def draw(numstr):
    global last_draw
    if type(numstr) != str:
        numstr = str(numstr)
    last_draw = numstr
    for b in boards:
        b.mark(numstr)
        b.checkbingo()

class Board:
    def __init__(self, rows):
        self.rows = list([row.split(' '), []] for row in rows)
        for row in self.rows:
            try:
                while row[0].index('') > -1:
                    row[0].pop(row[0].index(''))
            except ValueError:
                pass
        self.bingo = False

    def mark(self, numstr):
        for row in self.rows:
            try:
                j = row[0].index(numstr)
                row[0][j] = regex
                row[1] = [i for i, x in enumerate(row[0]) if x == regex]
            except ValueError:
                pass

    def checkvertical(self):
        marks = []
        for i in range(5):
            if len(self.rows[i][1]) < 1:
                return self.bingo
            else:
                marks.append(self.rows[i][1])
        if len(marks) == 5:
            comps = marks[0].copy()
            flat = [mark for l in marks for mark in l]
            for i in range(len(comps)):
                if flat.count(comps[i]) == 5:
                    self.bingo = True
                    break
        return self.bingo

    def checkhorizontal(self):
        for row in self.rows:
            if len(row[1]) == 5:
                self.bingo = True
        return self.bingo

    def checkscore(self):
        if self.bingo:
            res = 0
            for r in self.rows:
                for num in r[0]:
                    if num != regex:
                        res += int(num)
            return res * int(last_draw)
        else:
            return self.bingo

    def checkbingo(self):
        global bingo
        if self.checkvertical() or self.checkhorizontal():
            bingo = True
            print(self.checkscore())
            return self.checkscore()

    def state(self):
        for row in self.rows:
            print(row[0])
            
# generate boards
for _ in inp:
    b = Board(_.split('\n'))
    boards.append(b)

# run through draws
for d in range(len(draws)):
    if bingo:
        break
    else:
        draw(draws[d])

# # # testing
# b1 = Board(['38 66 51 93 39', '12 96 99 36 97', '40 21 95 10 94', ' 3 22 18 26 49', '91 61 73 70 47'])
# # b2 = Board(['38 66 51 93 99', '12 96 99 36 97', '40 21 95 10 94', ' 3 22 18 26 49', '91 61 73 70 47'])
# boards.append(b1)
# # boards.append(b2)

# draw(66)
# draw(96)
# draw(21)
# draw(22)
# draw(61)
# draw(38)
# draw(66)
# draw(51)
# draw(93)
# draw(39)