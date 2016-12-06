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
