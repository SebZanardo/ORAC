with open('cultin.txt', 'r') as input_file:
    n = int(input_file.readline())

day = 0
while n % 2 == 0:
    n /= 2
    day += 1

with open('cultout.txt', 'w') as output_file:
    output_file.write(f'{int(n)} {day}')
