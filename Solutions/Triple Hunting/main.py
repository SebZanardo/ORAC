input_file = open("tripin.txt", "r")

n = int(input_file.readline())
nums = [int(input_file.readline()) for _ in range(n)]

input_file.close()

triples = []
for i, num in enumerate(nums):
    if num % 3 != 0:
        continue
    triples.append(str(i+1))

output_file = open("tripout.txt", "w")

if not triples:
    output_file.write("Nothing here!")
else:
    output_file.write(f"{len(triples)}\n")
    output_file.write(f"{' '.join(triples)}")

output_file.close()
