with open('sitin.txt', 'r') as input_file:
    r, s = map(int, input_file.readline().split())
    t = int(input_file.readline())

if r * s >= t:
    sitting = t
    standing = 0
else:
    sitting = r * s
    standing = t - r * s

with open('sitout.txt', 'w') as output_file:
    output_file.write(f'{sitting} {standing}')
