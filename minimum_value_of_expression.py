import random

# We're solving for minimum value for strictly such polyomial functions that have a single point of 
# infexion (I mean a single/ definitive minima). These are typically U / V shaped graphs if we plot

# This is my thought process:
  # For any any random x, I first establish whether f(x) in the increasing or decreasing interval
    # IF f(x) < f(x+1) -> f(x) lies in the increasing interval of the function
    # IF f(x) > f(x+1) -> f(x) lies in the decreasing interval of the function
    
    # For the example: f(x) =  x ** 4 - 3 * x ** 3 - 5 * x + 10
    # analysing the behaviour of the function w.r.t some integer values of x
    # f(-1) = -19 -> f(0)  = 10 -> f(1)  = 3 -> f(2) = -8 ... [decreasing]
    # f(3) = -5 -> f(4) = 54 ...... [increasing]
    
    # so it's clear that from [-inf., 2.....] [decreasing]
    # and [2...., +inf.] [increasing]
    
  # From above two paths emerge:  
    # if f(x) is in the increasing interval, I continually decrement x until f(x) has gone beyond the point of infexion which will mean I break at f(x) > f(x + 1)
    # if f(x) is in the decreasing interval, I continually increment x until f(x) has gone beyond the point of infexion which will mean in this case I break at f(x) < f(x + 1)
    
    # based on the above observation I safely conclude that the minimum value
    # of the function lies with [x - 1, x + 1]
    
  # Finding the integer range[low, high] in which mimima lies helps narrowing the search space for the minima and I think is a good optimisation strategy.
  # Once the range is found I basically follow a simple logic to arrive at the minimum:
     # again I start with f(high) and continually decrement high by an infinitesimally small 'h' and break as soon as f(x - h) > f(x) which means 
     # break as soon as I again get past the point of inflexion
     
     # Once I break out of the above loop, I've effectively found the minima and at what x the minima occurs
     # Note: I'm getting near accurate results for the minima, the smaller I keep 'h', the better approximation
     
    
def f(x):
    return x ** 4 - 3 * x ** 3 - 5 * x + 10

def get_integer_range_in_which_minima_lies():
    
    x = random.randrange(-10,10) # I can pick any random range here, doesn't really matter

    increasing_interval = False
    decreasing_interval = False
    
    print(f"Random x -> {x}")
    if f(x) < f(x + 1):
        increasing_interval = True
        print("in the increasing interval")
    else:
        decreasing_interval = True
        print("in the decreasing interval")

    # if in the increasing interval -> 
        # reduce x -> check for y
        # repeat ^ until y shows an increasing trend
        
    # if in the decreasing flank ->
        # increase x -> check for y
        # repeat ^ until y shows an increasing trend
            
    range_containing_minima = ()
    
    if increasing_interval:
            # we need to continually bring down x -> which should lower y also
            # continue until there is again a rise in value of y                
            # decrement by 1
            while (f(x - 1) < f(x)):
                x = x - 1
                
            range_containing_minima = (x - 1, x + 1)            
              
    elif decreasing_interval:
            # we need to continually increase  x -> which should decrease y
            # continue until there is again a rise in value of y
            while(f(x + 1) < f(x)):
                x = x + 1
                
            range_containing_minima = (x - 1, x + 1)  
            
    print(f"range containing minima --> {range_containing_minima}") 
            
    return range_containing_minima

def get_function_minima():
    
    # get the range within which the minima lies
    range_containing_minima = get_integer_range_in_which_minima_lies()
    
    # now, determine at what point in the graph we get f(x - h) > f(x) (the function is just crossing the point of inflexion)
    # if we keep threshold infinitesimally small, we will get a very accurate result for the mimimum val. of the expression
    h = .00000001
    
    low = range_containing_minima[0]
    high = range_containing_minima[1]

    while f(high - h) < f(high):
        high = high - h

    print(f"""Minima of the given polynommial is  -> {f(high)} and minima
            occurs at {high}""")  
    
    
get_function_minima()