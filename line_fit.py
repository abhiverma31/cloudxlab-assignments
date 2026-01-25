import math
def fit(x1, y1, x2, y2):
    # we need to find the slope m and intercept c
    # assume the equation is a standard straight line: y = m * x + c
    # we'd end up with 2 equations with 2 variables - i'd use
    # simulataneous equation to determine m and c
    
    # case when x1 == x2
    
    # vertical line
    if x1 == x2:
        return (x1, math.inf)
    
    # from coordinate of point 1 (x1, y1)    
    m = c = int()
    # # eqn 1
    # y1 = x1 * m + c
    # # eqn 2
    # y2 = x2 * m + c
        
    # eqn 1 - eqn 2
    m = (y1 - y2)/(x1 - x2)
    
    # fit m in eqn 1 to obtain c    
    c = y1 - x1 * m
    
    return (m, c)

print(fit (1, 2, 3, 6))
print(fit (0, 5, 2, 9))
print(fit (4, 2, 4, 8))
    
    