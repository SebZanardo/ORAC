input_file = open("dictin.txt", "r")

d, w = map(int, input_file.readline().split())
dictionary = {}
for _ in range(d):
    key, val = input_file.readline().split()
    dictionary[key] = val
words = [input_file.readline().strip() for _ in range(w)]

input_file.close()

output_file = open("dictout.txt", "w")

for word in words:
    translation = "C?"
    if word in dictionary:
        translation = dictionary[word]
    output_file.write(f"{translation}\n")

output_file.close()
