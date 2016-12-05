import re
from operator import itemgetter
from string import ascii_lowercase

raw_rooms = []
with open('input/04') as f:
    raw_rooms = [
        line.rstrip('\n') for line in f
    ]

'''
raw_rooms = [
    'aaaaa-bbb-z-y-x-123[abxyz]',
    'a-b-c-d-e-f-g-h-987[abcde]',
    'not-a-real-room-404[oarel]',
    'totally-real-room-200[decoy]'
]
'''


def caesar_decrypt(text, shift):
    return ''.join(
        ascii_lowercase[
            (ascii_lowercase.index(char) + shift) % len(ascii_lowercase)
        ]
        for char in text
    )

room_re = re.compile(r'(?P<name>.*)-(?P<sector_id>\d+)\[(?P<checksum>\w+)\]')
valid_rooms = []

for raw_room in raw_rooms:
    room = room_re.match(raw_room).groupdict()
    room_name = room['name'].replace('-', '')
    char_count = {}
    for char in room_name:
        char_count.setdefault(char, 0)
        char_count[char] += 1
    # sort by alphabet
    char_count = sorted(char_count.items(), key=itemgetter(0))
    char_count = sorted(char_count, key=itemgetter(1), reverse=True)
    expected_checksum = ''.join(map(itemgetter(0), char_count[:5]))
    if expected_checksum == room['checksum']:
        valid_rooms.append(room)

for valid_room in valid_rooms:
    name = ' '.join(
        map(
            lambda r: caesar_decrypt(r, int(valid_room['sector_id'])),
            valid_room['name'].split('-')
        )
    )
    if name == 'northpole object storage':
        print(valid_room['sector_id'], name, sep=' | ')
print(len(valid_rooms), 'out of', len(raw_rooms), 'are valid')
print('Sector ID sum:', sum(map(lambda r: int(r['sector_id']), valid_rooms)))
