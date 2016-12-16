import re
from collections import namedtuple

Bot = namedtuple('Bot', ['number', 'chips'])
Output = Bot

instructions = []
with open('input/10') as f:
    instructions = [
        line.rstrip('\n') for line in f
    ]

value_re = re.compile(r'value\ (?P<value>\d+)\ goes\ to\ bot\ (?P<bot>\d+)')
compare_re = re.compile(
    r'bot (?P<bot>\d+) gives low to (?P<low>((bot)|(output)) \d+) and high to '
    r'(?P<high>((bot)|(output)) \d+)'
)
bots = {}
outputs = {}

# first initialize all bots
compare_instructions = []
for instruction in instructions:
    value_match = value_re.match(instruction)
    compare_match = compare_re.match(instruction)
    if value_match:
        bot_number = value_match.group('bot')
        value = int(value_match.group('value'))
        if bot_number in bots:
            bots[bot_number].chips.append(value)
        else:
            bots[bot_number] = Bot(bot_number, chips=[value])
    elif compare_match:
        compare_instructions.append(compare_match)

print(bots, outputs)
# now move chips around
for compare_instruction in compare_instructions:
    bot_name = compare_instruction.group('bot')
    if bot_name not in bots:
        continue
    # compare chips and choose lower + higher one
    sorted_chips = bots[bot_name].chips
    lower = sorted_chips[0]
    if len(sorted_chips) > 1:
        higher = sorted_chips[-1]
    high_type, high_name = compare_instruction.group('high').split()
    if high_type == 'bot' and high_name in bots:
        bots[high_name].chips.append(higher)
    elif high_type == 'output':
        if high_name in outputs:
            outputs[high_name].chips.append(higher)
        else:
            outputs[high_name] = Output(high_name, chips=[higher])
    low_type, low_name = compare_instruction.group('low').split()
    if low_type == 'bot' and low_name in bots:
        bots[low_name].chips.append(lower)
    elif low_type == 'output':
        if low_name in outputs:
            outputs[low_name].chips.append(lower)
        else:
            outputs[low_name] = Output(low_name, chips=[lower])
    # empty bots chips
    bots[bot_name] = bots[bot_name]._replace(chips=[])

print(bots, outputs)
