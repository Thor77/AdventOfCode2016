from itertools import takewhile, zip_longest


def window(iterable, size=2):
    args = [iter(iterable)] * size
    return takewhile(
        lambda t: None not in t,
        zip_longest(*args)
    )


def generate_dragon_curve(data, disk_size=272):
    while len(data) < disk_size:
        data = data + '0' + data[::-1].translate(str.maketrans({
            '0': '1',
            '1': '0'
        }))
    return data


def generate_checksum(data):
    def _generate(i):
        return ''.join(
            map(lambda d: '1' if d[0] == d[1] else '0', window(i))
        )
    checksum = _generate(data)
    while (len(checksum) % 2) == 0:
        checksum = _generate(checksum)
    return checksum

if __name__ == '__main__':
    initial_state = ''
    with open('input/16') as f:
        initial_state = f.read().rstrip('\n')
    size = 272
    data = generate_dragon_curve(initial_state, disk_size=size)[:size]
    print('Solution (Part 1):', generate_checksum(data))
