#(c) Annabell Noora Czinzoll
# Lotto Number-gen
import random

number_all = []
number_all.extend(range(1,50))
number_won = random.sample(number_all, 6)
print(number_won)
