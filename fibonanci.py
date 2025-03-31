def fibonacci(n):
    if n<= 1:
        return n
    else:
        return(fibonacci(n-1)+ fibonacci(n-2))

nterms = int(input("How many fibonacci number you want: "))

if nterms<=0:
    print("Error")
else:
    print("Fibonacci Sequence : ",end="")
    for i in range(nterms):
        print(fibonacci(i) ,end=' ')
        