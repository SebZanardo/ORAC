with open("taktakin.txt", "r") as input_file:
    n = int(input_file.readline())

moon = 0
while n % 11 != 1:
    n *= 2
    moon += 1

with open("taktakout.txt", "w") as output_file:
    output_file.write(f"{moon} {n}")
