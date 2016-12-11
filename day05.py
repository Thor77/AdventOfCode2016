from hashlib import md5

door_id = ''
with open('input/05') as f:
    door_id = f.read().rstrip('\n')

password = ''
i = 0
while len(password) < 8:
    hexed = md5((door_id + str(i)).encode('utf-8')).hexdigest()
    if hexed.startswith('00000'):
        password += hexed[5]
    i += 1

print('Password:', password)

password_p2 = [None] * 8
i = 0
while None in password_p2:
    hexed = md5((door_id + str(i)).encode('utf-8')).hexdigest()
    if hexed.startswith('00000'):
        try:
            position = int(hexed[5])
        except ValueError:
            i += 1
            continue
        char = hexed[6]
        if position < len(password_p2) and password_p2[position] is None:
            password_p2[position] = char
    i += 1
print('Password (Part2):', ''.join(password_p2))
