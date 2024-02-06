with open('streetin.txt', 'r') as input_file:
    n, k = map(int, input_file.readline().split())

largest_block = int(n/(k+1))

with open('streetout.txt', 'w') as output_file:
    output_file.write(str(largest_block))
