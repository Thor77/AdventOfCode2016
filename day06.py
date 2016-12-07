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
message_p2 = ''
for _, encoded in encoded_positions.items():
    most_common = Counter(encoded).most_common()
    message += most_common[0][0]
    message_p2 += most_common[-1][0]

print('Message:', message)
print('Message (part2):', message_p2)
