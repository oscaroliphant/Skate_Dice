# Skate Dice
# Genrates a random skateboarding trick 

import random

list1 = ['regular', 'fakie', 'switch', 'nollie']
list2 = ['bs', 'fs', ' ', ' ']
list3 = ['180', '360', '540', ' ', ' ']
list4 = ['kickflip', 'heelflip', 'shuvit', 'ollie', ' ', ' ']

while True:
    word1 = random.choice(list1)
    word2 = random.choice(list2)
    word3 = random.choice(list3)
    word4 = random.choice(list4)

    trick = f"{word1} {word2} {word3} {word4}"

    if trick == f"{word1} bs {word3} heelflip":
        trick = f"{word1} inward {word3} {word4}"
        break

    if trick == f"{word1} fs {word3} kickflip":
        trick = f"{word1} {word3} hardflip"
        break

    if word3 != ' ' or word4 != ' ':
        break

print(trick)