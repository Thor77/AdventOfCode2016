import re


class Matrix:
    def __init__(self, width=50, height=6):
        self.width = width
        self.height = height
        self.matrix = [[False for x in range(width)] for y in range(height)]

    def rect(self, width, height):
        for y in range(height):
            for x in range(width):
                self.matrix[y][x] = True

    def rotate_row(self, row, by):
        new_row = [False] * self.width
        for i, item in enumerate(self.matrix[row]):
            new_row[(i + by) % self.width] = item
        self.matrix[row] = new_row

    def rotate_column(self, column, by):
        new_column = [False] * self.height
        # build column
        old_column = [
            row[column]
            for row in self.matrix
        ]
        # build new_column
        for i, item in enumerate(old_column):
            new_column[(i + by) % self.height] = item
        # set new column values
        for i in range(len(self.matrix)):
            self.matrix[i][column] = new_column[i]

    def __len__(self):
        '''
        Return how many pixel are lit in the matrix
        '''
        lit = 0
        for line in self.matrix:
            for column in line:
                if column:
                    lit += 1
        return lit

    def __repr__(self):
        return '\n'.join(
            ''.join(map(lambda c: '#' if c else '.', line))
            for line in self.matrix
        )


instructions = []
with open('input/08') as f:
    instructions = [
        line.rstrip('\n')
        for line in f
    ]


def print_matrix(matrix):
    for line in matrix:
        print(''.join(map(lambda c: '#' if c else '.', line)))

matrix = Matrix()
rect_re = re.compile(r'rect\ (?P<width>\d+)x(?P<height>\d+)')
rotate_re = re.compile(
    r'rotate\ ((?P<row>row\ y=)|(?P<column>column\ x=))'
    r'(?P<coord>\d+)\ by\ (?P<by>\d+)'
)

for instruction in instructions:
    rect_match = rect_re.match(instruction)
    rotate_match = rotate_re.match(instruction)
    if rect_match:
        data = rect_match.groupdict()
        matrix.rect(int(data['width']), int(data['height']))
    elif rotate_match:
        data = rotate_match.groupdict()
        if 'row' in data and data['row']:
            matrix.rotate_row(int(data['coord']), int(data['by']))
        elif 'column' in data and data['column']:
            matrix.rotate_column(int(data['coord']), int(data['by']))
    print('-' * matrix.width)
    print(matrix)

print(len(matrix), 'pixel are lit')
