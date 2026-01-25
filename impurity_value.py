# This appears a very simple way to compute impurity and 
# the results aren't looking too off with the tests I've run.
# The main thinking I have is I assign higher impurity
# as the delta of the two classes is narrowing 

# I'd like to get some feedback on the thought process


def my_impurtiy(c1, c2):
    # if c1 == c2:
    #     return 1.0
    
    # elif c1 == 0 or c2 == 0:
    #     return 0.0
    
    current_delta = abs(c1 - c2)
    
    result = current_delta / (c1 + c2)
    
    return (1 - result)

print(my_impurtiy(7, 3))
print(my_impurtiy(0, 5))
print(my_impurtiy(9, 1))
print(my_impurtiy(20, 3))
print(my_impurtiy(6, 6))
    
    
    
    