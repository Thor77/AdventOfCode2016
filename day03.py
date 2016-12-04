from itertools import permutations

triangles = []
with open('input/03') as f:
    triangles = [
        (int(s1), int(s2), int(s3))
        for s1, s2, s3 in [line.rstrip('\n').strip().split() for line in f]
    ]

possible_triangles = 0

for triangle in triangles:
    for s1, s2, s3 in permutations(triangle):
        if not (s1 + s2) > s3:
            break
    else:
        possible_triangles += 1

print(possible_triangles, 'triangles are possible')
