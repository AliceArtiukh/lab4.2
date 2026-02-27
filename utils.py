def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
def gsd(a,b):
    while b:
        a,b=b,a%b
    return a
