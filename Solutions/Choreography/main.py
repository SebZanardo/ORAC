input_file = open("dancein.txt", "r")
d, t = map(int, input_file.readline().split())

dancers = {}
for line in input_file.readlines():
    a, b = map(int, line.split())
    if a in dancers and dancers[a] > 0:
        dancers[a] -= 1
    else:
        dancers[a] = 0

    if b in dancers:
        dancers[b] += 1
    else:
        dancers[b] = 1

input_file.close()

min_hoops = sum(dancers.values())

output_file = open("danceout.txt", "w")
output_file.write(str(min_hoops))
output_file.close()
