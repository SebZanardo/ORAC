input_file = open('encyin.txt', 'r')

n, q = map(int, input_file.readline().split())
encyclopedia = [input_file.readline() for _ in range(n)]
questions = [int(input_file.readline()) for _ in range(q)]

input_file.close()

output_file = open('encyout.txt', 'w')

for question in questions:
    output_file.write(encyclopedia[question-1])

output_file.close()
