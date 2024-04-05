with open("artin.txt", "r") as input_file:
    n = int(input_file.readline())
    points = [tuple(map(int, line.split())) for line in input_file.readlines()]

# To find minimum poster dimensions, need to find min x, y and max x, y
min_x = points[0][0]
max_x = points[0][0]
min_y = points[0][1]
max_y = points[0][1]

for point in points:
    x, y = point
    if x < min_x:
        min_x = x
    elif x > max_x:
        max_x = x

    if y < min_y:
        min_y = y
    elif y > max_y:
        max_y = y

area = (max_x - min_x) * (max_y - min_y)

with open("artout.txt", "w") as output_file:
    output_file.write(str(area))
