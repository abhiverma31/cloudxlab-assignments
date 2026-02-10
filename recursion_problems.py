# Division using Recursion to Find Quotient and Remainder

# Division is the process of finding how many times one number (called the divisor) fits 
# into another number (called the dividend). 

# For example, in 17 ÷ 5, the number 5 fits into 17 three times (that’s the quotient) 
# and there are 2 left over (that’s the remainder), because:

# 5 + 5 + 5 = 15, and 17 - 15 = 2  
# So, 17 ÷ 5 gives quotient = 3 and remainder = 2
# Recursion means solving a problem by breaking it into smaller versions of the same 
# problem. In this case, we repeatedly subtract the divisor from the dividend 
# and count how many times we do it until what’s left is smaller than the divisor 
# (that’s the remainder).

def non_recursive_division(dividend, divisor): # dividend, divisor
    # if dividend == 1:
    #     return (dividend, 0)
    # diff = 9 - 2 = 7
    # diff = 7 - 2 = 5
    # diff = 5 - 2 = 3
    # diff = 3 - 2 = 1
    
    # now 1 < 2, so we're at the end of the process
    # quotient = count_of_diff
    # remainder = the final diff value = 1
    
    count_diff_taken = 0
    while (dividend >= divisor):
        dividend = dividend - divisor
        count_diff_taken = count_diff_taken + 1
    return (count_diff_taken, dividend)  


# try converting this to recursion
def recursive_division(dividend, divisor, counter): # (dividend, divisor)
    if divisor > dividend:
        return (counter, dividend)
    
    return recursive_division(dividend - divisor, divisor, counter + 1)

def add_same_number_multiple_times(a, b): # multiply_recursive
    # add a  -> b times: a + a + a .....b times
    if b == 1:
        return a    
    return a + add_same_number_multiple_times(a, b-1)

print(add_same_number_multiple_times(6, 5))
print(non_recursive_division(27,8))
print(recursive_division(34, 7, 0))