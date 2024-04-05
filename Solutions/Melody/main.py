input_file = open("melodyin.txt", "r")
n, k = map(int, input_file.readline().split())

repeat_length = 3
frequency = [{} for _ in range(repeat_length)]
max_frequency = [[-1, -1] for _ in range(repeat_length)]
for i in range(n):
    note = int(input_file.readline())

    f = frequency[i % 3]
    if note in f:
        f[note] += 1
    else:
        f[note] = 1

    max_f = max_frequency[i % 3]
    if f[note] > max_f[0]:
        max_f[0] = f[note]
        max_f[1] = note
input_file.close()

to_change = sum(
    [n // repeat_length - max_frequency[i % 3][0] for i in range(repeat_length)]
)

output_file = open("melodyout.txt", "w")
output_file.write(str(to_change))
output_file.close()
