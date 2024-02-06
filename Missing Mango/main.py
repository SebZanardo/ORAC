with open('manin.txt', 'r') as input_file:
    ix, cx, id, cd = map(int, input_file.readline().split())

cleft = cx - cd
cright = cx + cd
ileft = ix - id
iright = ix + id

location = cright
if cleft == ileft or cleft == iright:
    location = cleft

with open('manout.txt', 'w') as output_file:
    output_file.write(str(location))
