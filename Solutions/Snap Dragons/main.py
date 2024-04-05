input_file = open("snapin.txt", "r")
r, s = map(int, input_file.readline().split())
r_cards = {}
s_cards = {}
for _ in range(r):
    card = int(input_file.readline())
    if card in r_cards:
        r_cards[card] += 1
    else:
        r_cards[card] = 1
for _ in range(s):
    card = int(input_file.readline())
    if card in s_cards:
        s_cards[card] += 1
    else:
        s_cards[card] = 1
input_file.close()

matches = 0
for c1, o1 in r_cards.items():
    if c1 in s_cards:
        matches += o1 * s_cards[c1]

output_file = open("snapout.txt", "w")
output_file.write(str(matches))
output_file.close()
