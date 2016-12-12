instructions = []
with open('input/12') as f:
    instructions = [
        line.rstrip('\n') for line in f
    ]

register = {}
i = 0  # use verbose for-loop to support jumping
while i < len(instructions):
    instruction = instructions[i].split()
    command, data = instruction[0], instruction[1:]
    if command == 'cpy':
        value, var = data
        try:
            register[var] = int(value)
        except ValueError:
            register[var] = register[value]
    elif command == 'inc':
        register[data[0]] += 1
    elif command == 'dec':
        register[data[0]] -= 1
    elif command == 'jnz':
        var, jump = data
        if register.get(var, 0) != 0:
            i += int(jump)
            continue
    i += 1

print('value of a:', register['a'])
