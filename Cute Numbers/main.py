with open('cutein.txt', 'r') as input_file:
    d = int(input_file.readline().strip())
    nums = [int(line) for line in input_file.readlines()]

count = 0
for i in range(d-1, -1, -1):
    if nums[i] != 0:
        break
    count += 1

with open('cuteout.txt', 'w') as output_file:
    output_file.write(str(count))
