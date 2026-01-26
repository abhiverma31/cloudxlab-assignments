# calculate square root using binary search method
def sqrt_binary_search(n, precision):
    # square root will be between 1 and n
    low = 1
    high = n
    mid = (low + high)/2
    product = mid * mid
    while (abs(product - n) > precision):
        
        if product == n:
            return mid
        
        if product - n > precision:
            high = mid
            
        elif product - n < precision:
            low = mid
        
        print(f"Low -> {low}")
        print(f"High -> {high}")
        mid = (low + high)/2
        print(f"guess --> {mid}")
        product = mid * mid
        
        print(f"Product --> {product}") 
            
    return mid  


# calculate cube root using binary search method
def cube_binary_search(n, precision):
    # cube root will be between 1 and n
    low = 1
    high = n
    mid = (low + high)/2
    product = mid * mid * mid
    while (abs(product - n) >= precision):
        
        if product - n > precision:
            high = mid
            
        elif product - n < precision:
            low = mid
        
        print(f"Low -> {low}")
        print(f"High -> {high}")
        mid = (low + high)/2
        print(f"guess --> {mid}")
        product = mid * mid * mid
        
        print(f"Product --> {product}")    
            
    return mid 

print("\n\n SQUARE ROOT CALCULATION")
square_root = sqrt_binary_search(64, .00001)
print(f"Sqaure root --> {square_root}")
print(f"Verify accuracy --> {square_root ** 2}")

print("\n\n CUBE ROOT CALCULATION")
cube_root = cube_binary_search(100, .00001)
print(f"Cube root --> {cube_root}")
print(f"Verify accuracy --> {cube_root ** 3}")
