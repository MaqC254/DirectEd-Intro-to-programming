from random import choice
from random import randint
from random import shuffle


coin = choice(["heads", "tails"])
print(coin)

number = randint(1, 10)
print(number)

cards = ["jack", "queen", "king"]
shuffle(cards)
for card in cards:
    print(card)

my_friends = ["Sam","John","Kim","Kasongo","Peter","Esther"]
shuffle(my_friends)
for _ in (my_friends):
    print(_)