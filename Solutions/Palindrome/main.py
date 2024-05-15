with open("palin.txt", "r") as input_file:
    n = int(input_file.readline())
    string = list(input_file.readline().strip())


# Loop characters of string with two pointers on either side of the array
# If characters don't match -> set the bigger to the smaller
for i in range(n // 2):
    front = string[i]
    back = string[n - i - 1]

    if front == back:
        continue

    if front < back:
        string[n - i - 1] = front
    else:
        string[i] = back


with open("palout.txt", "w") as output_file:
    output_file.write("".join(string))
