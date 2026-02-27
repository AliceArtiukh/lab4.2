def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
def is_power_of_five(n):
    if n <= 0:
        return False
    
    while n % 5 == 0:
        n = n // 5
        
    return n == 1