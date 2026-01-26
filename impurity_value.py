# This appears a very simple way to compute impurity and 
# the results aren't looking too off with the tests I've run.
# The main thinking I have is I assign higher impurity
# as the delta of the two classes is narrowing 

def my_impurtiy_idea1(c1, c2):
    # if c1 == c2:
    #     return 1.0
    
    # elif c1 == 0 or c2 == 0:
    #     return 0.0
    
    current_delta = abs(c1 - c2)
    
    result = current_delta / (c1 + c2)
    
    return (1 - result) 


# aim is to reward (assign higher purity) for scenarios when 
# there is higher degree of separation in the composition of the classes 
# impurity is proportional to separation, impurity = k * composition_separation
def my_impurtiy_idea2(c1, c2):
    if c1 == c2:
        return 1.0
    
    elif c1 == 0 or c2 == 0:
        return 0.0
    
    mixture_composition = c1 + c2
     
    # composition of each class in the mixture
    c1_composition = c1 / mixture_composition
    c2_composition = c2 / mixture_composition
    
    # print(f"c1 composition is -> {c1_composition}  AND "
    #       f"c2 composition is -> {c2_composition}""")
    
    composition_separation = abs(c1_composition - c2_composition)
    #print (f"Separation --> {composition_separation}")
    
    # aim is to reward (assign higher purity) for scenarios when 
    # there is higher degree of separation in the composition of the classes 
    # impurity is proportional to separation, impurity = k * composition_separation
    
    result = 0.99 * composition_separation
    
    return 1  - result

print("\n FIRST IDEA")

print(f"Impurity is --> {my_impurtiy_idea1(7, 3)}")
print(f"Impurity is --> {my_impurtiy_idea1(0, 5)}")
print(f"Impurity is --> {my_impurtiy_idea1(9, 1)}")
print(f"Impurity is --> {my_impurtiy_idea1(20, 3)}")
print(f"Impurity is --> {my_impurtiy_idea1(6, 6)}")

print("\n SECOND IDEA")

print(f"Impurity is --> {my_impurtiy_idea2(7, 3)}")
print(f"Impurity is --> {my_impurtiy_idea2(0, 5)}")
print(f"Impurity is --> {my_impurtiy_idea2(9, 1)}")
print(f"Impurity is --> {my_impurtiy_idea2(20, 3)}")
print(f"Impurity is --> {my_impurtiy_idea2(6, 6)}")
    
    
    
    