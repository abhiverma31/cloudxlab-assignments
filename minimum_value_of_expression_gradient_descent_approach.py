def f(a):
    #return 10 * a ** 2 - 4 * a + 5
    #return a ** 4 - 3 * a ** 3 - 5 * a + 10
    return 13 * a ** 2 - 10 * a + 50

def find_min(f):  
    eps = .000001
    a = 10
    #slope = (f(a + eps) - f(a)) / eps
    #print(slope)
    
    while True :
        slope = (f(a + eps) - f(a)) / eps
        #print(f"diff is {slope}")
        
        if slope > -.0001 and slope < .0001:
            print(f'returing with slope as => {slope} and a as => {a}')
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
        
if __name__ == '__main__':
    a, slope = find_min(f)
    print(f'The minimum value of function is {f(a)} and it occurs at point a = {a}')
    