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


def inclusive_range(start, stop, step=1):
    return range(start, (stop + 1) if step >= 0 else (stop - 1), step)


orientation = 1  # N, E, S, W
x, y = 0, 0
locations = [(x, y)]

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

    # save previous position
    previous_x = x
    previous_y = y

    # move
    steps = []
    if orientation == 1:
        y += distance
        steps = map(
            lambda s: (x, s),
            inclusive_range(previous_y, y)
        )
    elif orientation == 2:
        x += distance
        steps = map(
            lambda s: (s, y),
            inclusive_range(previous_x, x)
        )
    elif orientation == 3:
        y -= distance
        steps = map(
            lambda s: (x, s),
            inclusive_range(previous_y, y, -1)
        )
    elif orientation == 4:
        x -= distance
        steps = map(
            lambda s: (s, y),
            inclusive_range(previous_x, x, -1)
        )

    for step in list(steps)[1:]:
        if step in locations:
            print(
                'Part 2:', step,
                'Distance:', calculate_distance(step[0], step[1])
            )
        else:
            locations.append(step)

print('Position:', (x, y))
print('Distance:', calculate_distance(x, y))
