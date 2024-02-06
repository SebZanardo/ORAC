input_file = open('chimin.txt', 'r')
n = int(input_file.readline())
a = input_file.readline().strip()
b = input_file.readline().strip()
x = input_file.readline().strip()
input_file.close()

valid = True
inside = None
slices = 0
for i, c in enumerate(x):
    in_a = c == a[i]
    in_b = c == b[i]
    if not in_a and not in_b:
        valid = False
        break


    if inside == 'a':
        if not in_a:
            slices += 1
            inside = 'b'

    elif inside == 'b':
        if not in_b:
            slices += 1
            inside = 'a'

    else:
        if not in_a:
            inside = 'b'
        elif not in_b:
            inside = 'a'
        # Still don't know which one we are inside
        else:
            continue

output_file = open('chimout.txt', 'w')
if not valid:
    output_file.write('PLAN FOILED\n')
else:
    output_file.write('SUCCESS\n')
    output_file.write(str(slices))
output_file.close()
