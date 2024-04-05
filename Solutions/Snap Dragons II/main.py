with open("snapin.txt", "r") as input_file:
    w, h, rx, ry, sx, sy = map(int, input_file.readline().split())

# Only board dimensions created between the two dragons start position needed.
#   If one of the dragons moves away in a direction, the other would follow.

# Therefore, the dragon that moves first, ROSE will win on even length paths.
#   And SCARLET will win on odd length paths. The game is never a draw!

nw = abs(rx - sx)
nh = abs(ry - sy)
path_length = nw + nh - 1  # Find path between dragons

winner = "SCARLET"
if path_length % 2 == 0:
    winner = "ROSE"

with open("snapout.txt", "w") as output_file:
    output_file.write(str(winner))
