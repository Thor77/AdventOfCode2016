class Numpad:
    def __init__(self, matrix=[
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ], start=[1, 1]):
        self.matrix = matrix
        self.__index = start
        self.result = ''

    @property
    def number(self):
        y, x = self.__index
        return self.matrix[y][x]

    def up(self):
        new_value = self.__index[0] - 1
        if new_value >= 0:
            self.__index[0] = new_value
        # stop at edges
        if not self.number:
            self.__index[0] += 1

    def down(self):
        new_value = self.__index[0] + 1
        if new_value < len(self.matrix):
            self.__index[0] = new_value
        # stop at edges
        if not self.number:
            self.__index[0] -= 1

    def left(self):
        new_value = self.__index[1] - 1
        if new_value >= 0:
            self.__index[1] = new_value
        # stop at edges
        if not self.number:
            self.__index[1] += 1

    def right(self):
        new_value = self.__index[1] + 1
        if new_value < len(self.matrix[self.__index[0]]):
            self.__index[1] = new_value
        # stop at edges
        if not self.number:
            self.__index[1] -= 1


lines = []
with open('input/02') as f:
    lines = [
        line.rstrip('\n') for line in f
    ]

pad_p1 = Numpad()
pad_p2 = Numpad(matrix=[
    [None, None, 1, None, None],
    [None, 2, 3, 4, None],
    [5, 6, 7, 8, 9],
    [None, 'A', 'B', 'C', None],
    [None, None, 'D', None, None]
], start=[2, 0])
pads = (pad_p1, pad_p2)
for line in lines:
    instructions = list(line)
    for instruction in instructions:
        for pad in pads:
            if instruction == 'L':
                pad.left()
            elif instruction == 'R':
                pad.right()
            elif instruction == 'U':
                pad.up()
            elif instruction == 'D':
                pad.down()
    pad_p1.result += str(pad_p1.number)
    pad_p2.result += str(pad_p2.number)
print('Part 1:', pad_p1.result)
print('Part 2:', pad_p2.result)
