from collections import namedtuple

Elf = namedtuple('Elf', ['number', 'presents'])


def solve(elf_count):
    # give all elves their initial present
    elves = [Elf(i, presents=1) for i in range(elf_count)]
    while len(elves) > 1:
        for i in range(len(elves)):
            if i >= len(elves):
                break
            # find elf next to elf i with presents on hand
            next_elf = (i + 1) % len(elves)
            while elves[next_elf].presents == 0:
                if next_elf + 1 >= len(elves):
                    break
                next_elf = (next_elf + 1) % len(elves)
            # take presents from next elf
            elves[i] = elves[i]._replace(
                presents=elves[i].presents + elves[next_elf].presents
            )
            del elves[next_elf]
    return elves[0].number + 1

if __name__ == '__main__':
    elf_count = 0
    with open('input/19') as f:
        elf_count = int(f.read().rstrip('\n'))
    print('Solution (Part 1):', solve(elf_count))
