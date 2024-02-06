with open('ninjain.txt', 'r') as input_file:
    n, k = map(int, input_file.readline().split())


caught = 0
for i in range(0, n, k+1):
    caught += 1

missed = n - caught

with open('ninjaout.txt', 'w') as output_file:
    output_file.write(str(missed))
