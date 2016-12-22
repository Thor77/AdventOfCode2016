def simulate_part1(elf_count):
    # give all elves their initial present
    elves = [[i, 1] for i in range(elf_count)]
    while len(elves) > 1:
        for i in range(len(elves)):
            if i >= len(elves):
                break
            # find elf next to elf i with presents on hand
            next_elf = (i + 1) % len(elves)
            while elves[next_elf][1] == 0:
                if next_elf + 1 >= len(elves):
                    break
                next_elf = (next_elf + 1) % len(elves)
            # take presents from next elf
            elves[i][1] += elves[next_elf][1]
            del elves[next_elf]
        print(len(elves), 'elves left after this round')
    return elves[0][0] + 1


def part1(elf_count):
    # Thanks to Numberphile https://www.youtube.com/watch?v=uCsD3ZGzMgE
    elf_count_binary = bin(elf_count)[2:]
    return int(elf_count_binary[1:] + elf_count_binary[-1], 2)

if __name__ == '__main__':
    elf_count = 0
    with open('input/19') as f:
        elf_count = int(f.read().rstrip('\n'))
    print('Solution (Part 1):', part1(elf_count))
