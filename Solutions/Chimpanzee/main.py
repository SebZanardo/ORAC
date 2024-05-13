with open("chimpin.txt", "r") as input_file:
    x, y = map(int, input_file.readline().split())

# Simulate moving around spiral
page = 0
side_length = 1
length_travelled = 0
sx, sy = 0, 0

NORTH = (0, 1)
EAST = (1, 0)
SOUTH = (0, -1)
WEST = (-1, 0)

directions = [EAST, NORTH, WEST, SOUTH]
current_direction = 0

while sx != x or sy != y:
    move_direction = directions[current_direction]
    sx += move_direction[0]
    sy += move_direction[1]
    page += 1
    length_travelled += 1

    if length_travelled == side_length:
        if move_direction == NORTH:
            side_length += 1
        elif move_direction == SOUTH:
            side_length += 1

        current_direction += 1
        current_direction %= 4

        length_travelled = 0

with open("chimpout.txt", "w") as output_file:
    output_file.write(str(page))
