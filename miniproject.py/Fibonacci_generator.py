n = int(input('Enter number: '))

def fibo(n):
    if n<2:
        return n
    else:
        result = fibo(n-1) + fibo(n-2)
        return result
print(fibo(n))