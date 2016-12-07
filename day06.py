from collections import Counter

lines = []
with open('input/06') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

encoded_positions = {}
for line in lines:
    for position, char in enumerate(line):
        encoded_positions.setdefault(position, '')
        encoded_positions[position] += char

message = ''
for _, encoded in encoded_positions.items():
    message += Counter(encoded).most_common(1)[0][0]

print('Message:', message)
