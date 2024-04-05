input_file = open("bendin.txt", "r")
ax1, ay1, ax2, ay2 = map(int, input_file.readline().split())
bx1, by1, bx2, by2 = tuple(map(int, input_file.readline().split()))
input_file.close()

aw = ax2 - ax1
ah = ay2 - ay1
bw = bx2 - bx1
bh = by2 - by1

area = aw * ah + bw * bh

# Check for overlapping
if ax2 > bx1 and ax1 < bx2 and ay2 > by1 and ay1 < by2:
    # Create new box
    ox1 = max(ax1, bx1)
    oy1 = max(ay1, by1)
    ox2 = min(ax2, bx2)
    oy2 = min(ay2, by2)

    ow = abs(ox2 - ox1)
    oh = abs(oy2 - oy1)
    area -= ow * oh

output_file = open("bendout.txt", "w")
output_file.write(str(area))
output_file.close()
