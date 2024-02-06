with open('rainin.txt', 'r') as input_file:
    n, c = map(int, input_file.readline().split())
    nums = [int(line) for line in input_file.readlines()]

captured = 0
day = 1
for rainfall in nums:
    captured += rainfall
    if captured >= c:
        break
    day += 1

with open('rainout.txt', 'w') as output_file:
    output_file.write(str(day))
