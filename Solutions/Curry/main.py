with open("curryin.txt", "r") as input_file:
    c, r, v = map(int, input_file.readline().split())

x, y, z = 0, 0, 0

largest = max(c, r, v)
half_c = int(c / 2)
half_r = int(r / 2)
half_v = int(v / 2)

# If all equal
# if even x = r//2, y = c//2, v //2
# if odd x = r//2+1, y = c//2+1, v //2 Doesn't matter where extras go
if c == r and c == v:
    if c % 2 == 0:
        x = half_c
        y = half_c
        z = half_c
    else:
        x = half_c + 1
        y = half_c + 1
        z = half_c

# If two equal and max
# smaller goes into each max smallest//2 times
# two same go together max - smallest//2
elif largest == r and largest == v:
    y = half_c
    z = half_c
    x = r - half_c

elif largest == c and largest == v:
    x = half_r
    z = half_r
    y = c - half_r

elif largest == c and largest == r:
    x = half_v
    y = half_v
    z = c - half_v

# Find difference of two smaller numbers to largest number
# If other two sum <= max: just go into perfectly ignore left over in max
# Else: two smaller numbers go together int(s_diff-max/2) times and then into max for the rest
#   and if int(s_diff-max/2) was rounded then - 1 from one of the two
elif largest == c:
    remaining = r + v
    if remaining <= c:
        y = v
        z = r
    else:
        together = (remaining - c) / 2
        together_rounded = int(together)
        x = together_rounded
        y = v - together_rounded
        z = r - together_rounded
        if together_rounded != together:
            y -= 1

elif largest == r:
    remaining = c + v
    if remaining <= r:
        x = v
        z = c
    else:
        together = (remaining - r) / 2
        together_rounded = int(together)
        y = together_rounded
        x = v - together_rounded
        z = c - together_rounded
        if together_rounded != together:
            x -= 1

elif largest == v:
    remaining = c + r
    if remaining <= v:
        x = r
        y = c
    else:
        together = (remaining - v) / 2
        together_rounded = int(together)
        z = together_rounded
        x = r - together_rounded
        y = c - together_rounded
        if together_rounded != together:
            x -= 1


with open("curryout.txt", "w") as output_file:
    output_file.write(f"{x} {y} {z}")
