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
bot_instructions = {}

# first initialize all bots and collect instructions
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
        cmpd = compare_match.groupdict()
        bot_instructions[cmpd['bot']] = cmpd['high'], cmpd['low']

target_types = {
    'bot': bots,
    'output': outputs
}
# now move chips around
while bots:
    for _, bot in list(filter(lambda i: len(i[1].chips) == 2, bots.items())):
        lower_chip, higher_chip = sorted(bot.chips)
        if lower_chip == 17 and higher_chip == 61:
            print('Solution (Part 1):', bot)
        higher, lower = bot_instructions[bot.number]
        # parse instruction
        high_type, high_name = higher.split()
        if high_name in target_types[high_type]:
            target_types[high_type][high_name].chips.append(higher_chip)
        else:
            args = (high_name,)
            kwargs = {'chips': [higher_chip]}
            target_types[high_type][high_name] = Bot(*args, **kwargs) \
                if high_type == 'bot' else Output(*args, **kwargs)
        low_type, low_name = lower.split()
        if low_name in target_types[low_type]:
            target_types[low_type][low_name].chips.append(lower_chip)
        else:
            args = (low_name,)
            kwargs = {'chips': [lower_chip]}
            target_types[low_type][low_name] = Bot(*args, **kwargs) \
                if low_type == 'bot' else Output(*args, **kwargs)
        # remove bot from store
        del bots[bot.number]
