list = [ i for i in range(52)]


#shuffle

import random

random.shuffle(list)

print("After shuffle, deck of cards is", list)

random.choice(list)

print("Picked card is ", random.choice(list))
