with open('nortin.txt', 'r') as input_file:
    w, h = map(int, input_file.readline().split())

area = w * h
if w % 2 != 0 and h % 2 != 0:
    longest_path = area - 1
else:
    longest_path = area

with open('nortout.txt', 'w') as output_file:
    output_file.write(str(longest_path))
