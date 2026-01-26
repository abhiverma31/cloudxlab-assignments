# Print design a coin toss that prints "Head" or "Tail"

# a simple way to implement this is to represent the two
# possible states - HEAD and TAIL as numbers (1, 2)
# then with each run (flip of the coin) randomely pick
# either of the two states

states = {1: 'Head', 2: 'Tail'}

import random
def print_head_or_tail():
    probability = random.random()
    
    print(probability)
    
    # equal length of interval should imply equal probability of 
    # output falling under those intervals 
    # hence I'm going ahead with this logic:
    
    if 0.0 < probability < 0.5:
        print(states.get(1))
    else:
        print(states.get(2))    

print_head_or_tail()