# Factorial of any number n is represented by n! and is equal to 1*2*3*....*(n-1)*n. E.g.-
# 4! = 1*2*3*4 = 24
# 3! = 3*2*1 = 6
# 2! = 2*1 = 2
# Also,
# 1! = 1
# 0! = 1

def factorial(n):
    result = 1;
    for x in range(n,0,-1):
        result = result * x;
    return result;

print(factorial(4))