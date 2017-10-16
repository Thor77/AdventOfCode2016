import re

from run import single

marker_re = re.compile(r'\((\d+)x(\d+)\)')


@single
def part1(line):
    final_sequence = ''
    match_pos = 0
    while True:
        match = marker_re.search(line, pos=match_pos)
        if not match:
            break
        next_x, repeat_x = int(match.group(1)), int(match.group(2))
        final_sequence += line[match_pos:match.start()]
        final_sequence += line[match.end():match.end() + next_x] * repeat_x
        match_pos = match.end() + next_x
    if match_pos != len(line):
        # add remaining characters to final sequence
        final_sequence += line[match_pos:]

    return len(final_sequence) if final_sequence else len(line)


@single
def part2(line):
    return None
