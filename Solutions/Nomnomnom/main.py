input_file = open('nomin.txt', 'r')

n = int(input_file.readline())

needs = 0  # Minimum needed to eat
hippo = 0
eaten = 0
for i in range(n):
    food = int(input_file.readline())

    # Satisfied a hippo, move onto next
    if food + eaten >= needs:
        if food + eaten > needs:
            needs = food + eaten
        eaten = 0
        hippo += 1
    # Hippo not yet satisfied
    else:
        eaten += food

with open('nomout.txt', 'w') as output_file:
    output_file.write(str(hippo))
