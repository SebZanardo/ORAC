with open("countin.txt", "r") as input_file:
    n = int(input_file.readline())

with open("countout.txt", "w") as output_file:
    for i in range(1, n + 1):
        output_file.write(f"{i}\n")
