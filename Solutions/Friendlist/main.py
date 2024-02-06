def add_friend(friendships, id, friend):
    if id in friendships:
        friendships[id].append(friend)
    else:
        friendships[id] = [friend]


input_file = open("listin.txt", "r")

f = int(input_file.readline())
friendships = {}
for _ in range(f):
    a, b = map(int, input_file.readline().split())
    add_friend(friendships, a, b)
    add_friend(friendships, b, a)

input_file.close()

# Find biggest friend list
biggest = 0
for key, val in friendships.items():
    if len(val) > biggest:
        biggest = len(val)

output_file = open("listout.txt", "w")

for key, val in sorted(friendships.items()):
    if len(val) != biggest:
        continue
    output_file.write(f"{key}\n")

output_file.close()
