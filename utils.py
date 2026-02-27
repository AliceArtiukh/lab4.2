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
    return a
