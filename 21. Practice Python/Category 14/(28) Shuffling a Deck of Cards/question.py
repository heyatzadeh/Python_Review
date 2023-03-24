# ----------------- Program Task Description
# Write a program that creates a deck of cards and shuffles it each time the program is run.
import random

cards = list()
for i in range(1, 11):
    cards.append(str(i))
cards.append("Bishop")
cards.append("Queen")
cards.append("King")

for index, value in enumerate(cards):
    random_index = random.randint(0, len(cards) - 1)
    random_value = cards[random_index]

    cards[random_index] = cards[index]
    cards[index] = random_value

print(cards)
