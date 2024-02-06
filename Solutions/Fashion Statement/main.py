with open('fashin.txt', 'r') as input_file:
    n = int(input_file.readline())

notes = [100, 20, 5, 1]
fewest = 0

while n > 0:
    for note in notes:
        if note <= n:
            n -= note
            fewest += 1
            break

with open('fashout.txt', 'w') as output_file:
    output_file.write(str(fewest))
