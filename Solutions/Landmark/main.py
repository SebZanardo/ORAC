with open("landin.txt", "r") as input_file:
    r, c = map(int, input_file.readline().split())

    city_block = []
    for row in range(r):
        city_block.append(list(input_file.readline().strip()))

FULL = "#"
EMPTY = "."

br1, bc1, br2, bc2 = 0, 0, 0, 0
longest = 0

cr1, cc1 = 0, 0
current_length = 0
inside = False

# Horizontal
for y in range(r):
    for x in range(c):
        cell = city_block[y][x]
        if cell == FULL:
            current_length = 0
            inside = False

        elif cell == EMPTY:
            if not inside:
                cr1 = y
                cc1 = x
                inside = True

            current_length += 1

            if current_length > longest:
                br1 = cr1
                bc1 = cc1
                br2 = y
                bc2 = x
                longest = current_length

    current_length = 0
    inside = False

# Vertical
for x in range(c):
    for y in range(r):
        cell = city_block[y][x]
        if cell == FULL:
            current_length = 0
            inside = False

        elif cell == EMPTY:
            if not inside:
                cr1 = y
                cc1 = x
                inside = True

            current_length += 1

            if current_length > longest:
                br1 = cr1
                bc1 = cc1
                br2 = y
                bc2 = x
                longest = current_length

    current_length = 0
    inside = False

with open("landout.txt", "w") as output_file:
    output_file.write(f"{br1+1} {bc1+1} {br2+1} {bc2+1}")
