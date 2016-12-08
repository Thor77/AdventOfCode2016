from itertools import islice, zip_longest, takewhile


def window(iterable, size=2):
    return takewhile(
        lambda t: None not in t,
        zip_longest(*[
            islice(iterable, i, None)
            for i in range(size)
        ])
    )


def contains_abba(text):
    for c1, c2, c3, c4 in window(text, size=4):
        if c2 == c3 and c1 == c4 and c2 != c4:
            return True
    else:
        return False


def parse_address(address):
    address_sequences = []
    hypernet_sequences = []
    hypernet = False
    hypernet_sequence = ''
    address_sequence = ''
    for char in address:
        if char == '[':
            hypernet = True
            address_sequences.append(address_sequence)
            address_sequence = ''
        elif char == ']':
            hypernet = False
            hypernet_sequences.append(hypernet_sequence)
            hypernet_sequence = ''
        else:
            if hypernet:
                hypernet_sequence += char
            else:
                address_sequence += char
    if address_sequence:
        address_sequences.append(address_sequence)
    return address_sequences, hypernet_sequences


addresses = []
with open('input/07') as f:
    addresses = [
        parse_address(line.rstrip('\n'))
        for line in f
    ]

supporting_tls = 0
for address_sequences, hypernet_sequences in addresses:
    if list(filter(contains_abba, address_sequences)) \
            and not list(filter(contains_abba, hypernet_sequences)):
        supporting_tls += 1

print(supporting_tls, 'out of', len(addresses), 'support tls')
