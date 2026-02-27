def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
def fibonacci(n):
    """Повертає n-те число Фібоначчі (0, 1, 1, 2, 3, 5...)"""
    if n < 0:
        return None
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
def is_power_of_five(n):
    if n <= 0:
        return False
    
    while n % 5 == 0:
        n = n // 5
        
    return n == 1

def gsd(a,b):
    while b:
        a,b=b,a%b
    return a

