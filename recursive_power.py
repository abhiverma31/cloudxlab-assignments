def power(x,n):
    if n < 0:
        return power(1/x, abs(n))
    if n == 0:
        return 1
    return x * power(x, n - 1)

print(power(4,3))
print(power(4,-3))