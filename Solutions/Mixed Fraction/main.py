with open("mixin.txt", "r") as input_file:
    n, d = map(int, input_file.readline().split())

a = int(n / d)
b = n % d

equation = str(a) if b == 0 else f"{a} {b}/{d}"

with open("mixout.txt", "w") as output_file:
    output_file.write(equation)
