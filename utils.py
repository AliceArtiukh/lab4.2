def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
<<<<<<< HEAD
def fibonacci(n):
    """Повертає n-те число Фібоначчі (0, 1, 1, 2, 3, 5...)"""
    if n < 0:
        return None
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
=======
def gsd(a,b):
    while b:
        a,b=b,a%b
>>>>>>> cf72af8c2eab413b25521957136a1639cb80b53e
    return a
