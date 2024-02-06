input_file = open('robotin.txt', 'r')

k = int(input_file.readline())
instructions = list(input_file.readline().strip())

input_file.close()

x = 0
y = 0
for instruction in instructions:
    if instruction == 'N':
        y -= 1
    elif instruction == 'E':
        x += 1
    elif instruction == 'S':
        y += 1
    elif instruction == 'W':
        x -= 1
steps_back = abs(x) + abs(y)

output_file = open('robotout.txt', 'w')

output_file.write(f"{steps_back}\n")

output_file.close()
