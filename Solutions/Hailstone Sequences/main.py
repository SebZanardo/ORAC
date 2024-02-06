input_file = open('hailin.txt', 'r')

steps = []
while True:
    n = int(input_file.readline())
    if n == 0:
        break

    step = 0
    while n != 1:
        # Even
        if n % 2 == 0:
            n /= 2
        # Odd
        else:
            n = n * 3 + 1

        step += 1
    steps.append(step)

with open('hailout.txt', 'w') as output_file:
    for step in steps:
        output_file.write(f'{step}\n')
