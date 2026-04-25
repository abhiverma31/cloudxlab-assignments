def f(a):
    #return 10 * a ** 2 - 4 * a + 5
    #return a ** 4 - 3 * a ** 3 - 5 * a + 10
    return 13 * a ** 2 - 10 * a + 50

def E_func(a,b): # a, b are model parameters
    return (2*a + b - 10) ** 2 + (3*a + b -30) ** 2

def find_min_one_model_parameter(f):  
    eps = .000001
    a = 10
    #slope = (f(a + eps) - f(a)) / eps
    #print(slope)
    
    while True :
        slope = (f(a + eps) - f(a)) / eps
        #print(f"diff is {slope}")
        
        if slope > -.0001 and slope < .0001:
            #print(f'returing with slope as => {slope} and a as => {a}')
            return a, f"{slope:.10f}"
        
        a = a - eps * slope
        print(f'a is {a}, slope is {slope}')
        
    # this if/else is not required, since the sign of diff will ensure
    # the current direction in which 'a' will move
        # if (diff < 0):
        #     # negative slope => increasing x will reduce error
        #     a = a - diff
        #     print(f'a is -> {a}')
        #     diff = (f(a + eps) - f(a)) / eps  
        #     print(f"diff1 -> {diff}")  
            
        # elif (diff > 0):
        #     print('here..')
        #     # positive slope => decreasing x will reduce error  
        #     a = a - diff
        #     print(f'a is -> {a}')
        #     diff = (f(a + eps) - f(a)) / eps
        #     print(f'diff2 -> {diff}') 
        
        
def find_min_two_model_parameters(f):    
    eps = .000001
    movement_measure = .001
    a = 0
    b = 0
    
    while True :
        diff_a = (f(a+eps, b) - f(a,b)) / eps
        diff_b = (f(a, b+eps) - f(a,b)) / eps
        
        if diff_a > -.0001 and diff_a < .0001 and  diff_b > -.0001 and diff_b < .0001 :            
            return a, b, f"{diff_a:.10f}", f"{diff_b:.10f}"
        
        a = a - movement_measure * diff_a
        b = b - movement_measure * diff_b
        
if __name__ == '__main__':
    print('1 model parameter')
    a, slope = find_min_one_model_parameter(f)
    print(f'The minimum value of function is {f(a)} and it occurs at point a = {a}')
    
    print('-' * 80)
    
    print('2 model parameters:')
    a1, b1, slope_a, slope_b = find_min_two_model_parameters(E_func)
    print(f'The minimum value of function is {E_func(a1,b1)} and it occurs at point a = {a1}, b = {b1}')
    