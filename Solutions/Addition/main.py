with open("addin.txt", "r") as input_file:
    a, b = map(int, input_file.readline().split())

total = a + b

with open("addout.txt", "w") as output_file:
    output_file.write(str(total))
