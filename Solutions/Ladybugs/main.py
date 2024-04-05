with open("ladyin.txt", "r") as input_file:
    d = int(input_file.readline())
    posts = set([int(line) for line in input_file.readlines()])

length = max(posts) - min(posts) + 1

with open("ladyout.txt", "w") as output_file:
    output_file.write(str(length))
