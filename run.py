import argparse
import functools
import importlib
from os import path as ospath


def single(func):
    @functools.wraps(func)
    def wrapped_func(lines):
        return func(lines[0])
    return wrapped_func


input_directory = 'input/'


def run(day, parts=['part1', 'part2'], test=False):
    # convert day to str and fill with leading zero
    day = str(day).zfill(2)
    # import code for day (adding 'day' prefix)
    module = importlib.import_module('day' + day, package='.')
    # read input for day
    input_lines = []

    # test mode
    if test:
        input_path = ospath.join(input_directory, 'test', day)
    else:
        input_path = ospath.join(input_directory, day)

    with open(input_path) as f:
        # remove newline-endings and filter empty lines
        input_lines = list(
            filter(
                None,
                map(
                    lambda line: line.replace('\n', '').strip(),
                    f.readlines()
                )
            )
        )
    for part in parts:
        print(
            'Solution', part.title() + ':', getattr(module, part)(input_lines)
        )


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('day', help='day to solve', type=int)
    parser.add_argument(
        '-p1', '--part1', help='solve part1', action='store_true'
    )
    parser.add_argument(
        '-p2', '--part2', help='solve part2', action='store_true'
    )
    parser.add_argument(
        '-t', '--test', help='use test input', action='store_true'
    )
    args = parser.parse_args()
    if args.part1 and not args.part2:
        parts = ['part1']
    elif not args.part1 and args.part2:
        parts = ['part2']
    else:
        parts = ['part1', 'part2']
    run(args.day, parts, args.test)
