class Numpad:
    def __init__(self, matrix=[
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ], start=[1, 1]):
        self.matrix = matrix
        self.__index = start

    @property
    def number(self):
        y, x = self.__index
        return self.matrix[y][x]

    def up(self):
        new_value = self.__index[0] - 1
        if new_value >= 0:
            self.__index[0] = new_value

    def down(self):
        new_value = self.__index[0] + 1
        if new_value < len(self.matrix):
            self.__index[0] = new_value

    def left(self):
        new_value = self.__index[1] - 1
        if new_value >= 0:
            self.__index[1] = new_value

    def right(self):
        new_value = self.__index[1] + 1
        if new_value < len(self.matrix[self.__index[0]]):
            self.__index[1] = new_value


lines = []
with open('input/02') as f:
    lines = [
        line.rstrip('\n') for line in f
    ]

pad = Numpad()
for line in lines:
    instructions = list(line)
    for instruction in instructions:
        if instruction == 'L':
            pad.left()
        elif instruction == 'R':
            pad.right()
        elif instruction == 'U':
            pad.up()
        elif instruction == 'D':
            pad.down()
    print('Number:', pad.number)
