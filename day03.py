from itertools import permutations


def is_possible(triangle):
    for s1, s2, s3 in permutations(triangle):
        if not (s1 + s2) > s3:
            return False
    else:
        return True


if __name__ == '__main__':
    triangles = []
    with open('input/03') as f:
        triangles = [
            (int(s1), int(s2), int(s3))
            for s1, s2, s3 in [line.rstrip('\n').strip().split() for line in f]
        ]
    possible_triangles = filter(is_possible, triangles)
    print(len(list(possible_triangles)), 'triangles are possible')
