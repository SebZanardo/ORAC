with open('vasesin.txt', 'r') as input_file:
    n = int(input_file.readline())

if n < 6:
    solution = '0 0 0'
else:
    solution = f'1 2 {n-3}'

with open('vasesout.txt', 'w') as output_file:
    output_file.write(solution)
