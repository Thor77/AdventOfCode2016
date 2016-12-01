raw = ''
with open('input/01') as f:
    raw = f.read().rstrip('\n')
instructions = raw.split(', ')


def calculate_distance(x, y):
    if x < 0:
        x *= -1
    if y < 0:
        y *= -1
    return x + y

orientation = 1  # N, E, S, W
x, y = 0, 0

for instruction in instructions:
    # parse instruction
    direction = instruction[0]
    distance = int(instruction[1:])

    # turn
    if direction == 'R':
        orientation += 1
    elif direction == 'L':
        orientation -= 1

    # validate orientation
    if orientation > 4:
        orientation = 1
    if orientation < 1:
        orientation = 4

    # move
    if orientation == 1:
        y += distance
    elif orientation == 2:
        x += distance
    elif orientation == 3:
        y -= distance
    elif orientation == 4:
        x -= distance

print('Position:', (x, y))
print('Distance:', calculate_distance(x, y))
