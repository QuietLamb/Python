# n = int(input("Enter number: "))

# def plus(n):
#     if n == 0:
#         return 0
#     else:
#         return n + plus(n-1)
# print(plus(n))

# ************************
x = int(input('Enter x: '))
n = int(input('Enter n: '))

def pow_n(x,n):
    if n == 0:
        return 1
    else:
        return x * pow_n(x,n-1)
print(pow_n(x,n))