input_file = open('genin.txt', 'r')
n, p = map(int, input_file.readline().split())
input_file.close()

completed = [0 for _ in range(n)]
c = 0
i = 0
while c < p:
    c += i+1
    completed[i%n] += i+1
    if c > p:
        completed[i%n] -= c-p
    i += 1

best = max(completed)
person = completed.index(best)+1

output_file = open('genout.txt', 'w')
output_file.write(f'{person} {best}\n')
output_file.close()
