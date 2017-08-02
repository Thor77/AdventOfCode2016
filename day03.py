from itertools import permutations, chain


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
        # PART 2
        # parse integers and save them into a matrix
        sides_list = [
            triangle[coord]
            for coord in range(3)
            for triangle in chain.from_iterable([filter(list, triangles)] * 3)
        ]
        triangles_p2 = [
            (sides_list[i], sides_list[i + 1], sides_list[i + 2])
            for i in range(0, len(sides_list), 3)
        ]
    possible_triangles = filter(is_possible, triangles)
    print(len(list(possible_triangles)), 'triangles are possible')
    print(
        'PART 2:',
        len(list(filter(is_possible, triangles_p2))),
        'triangles are possible'
    )
