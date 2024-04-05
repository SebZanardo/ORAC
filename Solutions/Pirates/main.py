with open("piratein.txt", "r") as input_file:
    l = int(input_file.readline())
    x = int(input_file.readline())
    y = int(input_file.readline())

clockwise = l - x + l - y
anti_clockwise = x + y

shortest = clockwise if clockwise < anti_clockwise else anti_clockwise

with open("pirateout.txt", "w") as output_file:
    output_file.write(str(shortest))
