# Print design a coin toss that prints "Head" or "Tail"

# a simple way to implement this is to represent the two
# possible states - HEAD and TAIL as numbers (1, 2)
# then with each run (flip of the coin) randomely pick
# either of the two states

states = {1: 'Head', 2: 'Tail'}

import random
def print_head_or_tail():
    print(states.get(random.randrange(1, 3)))

print_head_or_tail()