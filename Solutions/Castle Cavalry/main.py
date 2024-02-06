input_file = open('cavalryin.txt', 'r')

n = int(input_file.readline())
squad_count = {}  # squad_size : knights
for _ in range(n):
    size = int(input_file.readline())
    if size not in squad_count:
        squad_count[size] = 1
    else:
        squad_count[size] += 1

input_file.close()

valid = True
for key, val in squad_count.items():
    if val % key != 0:
        valid = False

output_file = open('cavalryout.txt', 'w')

if valid:
    output_file.write("YES\n")
else:
    output_file.write("NO\n")

output_file.close()
