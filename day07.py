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


def find_aba_or_bab(text):
    for c1, c2, c3 in window(text, size=3):
        if c1 == c3 and c1 != c2:
            yield c1, c2
    else:
        yield (None, None)





def supports_tls(address):
    address_sequences, hypernet_sequences = address
    if list(filter(contains_abba, address_sequences)) \
            and not list(filter(contains_abba, hypernet_sequences)):
        return True


def supports_ssl(address):
    address_sequences, hypernet_sequences = address
    aba_s_in_address = sum(list(map(list, (map(find_aba_or_bab, address_sequences)))), [])
    bab_s_in_hypernet = sum(list(map(list, (map(find_aba_or_bab, hypernet_sequences)))), [])
    for a_char, b_char in aba_s_in_address:
        if not a_char or not b_char:
            continue
        if (b_char, a_char) in bab_s_in_hypernet:
            return True


if __name__ == '__main__':
    addresses = []
    with open('input/07') as f:
        addresses = [
            parse_address(line.rstrip('\n'))
            for line in f
        ]
    print(len(list(filter(supports_tls, addresses))), 'support tls')
    print(len(list(filter(supports_ssl, addresses))), 'support ssl')
