print("Choose Operator: ")
print("a> Sum")
print("b> Sub")
print("c> Mul")
print("d> Div")

while True:
    x = int(input("Enter Number: "))
    y = int(input("Enter Number: "))
    n = input("Enter option: ")

    Sum = lambda x,y : x + y
    Sub = lambda x,y : x - y
    Mul = lambda x,y : x * y
    Div = lambda x,y : x / y

    if n == 'a':
        result = Sum(x,y)
        print(result)
    elif n == 'b':
        result = Sub(x,y)
        print(result)
    elif n == 'c':
        result = Mul(x,y)
        print(result)
    elif n == 'd':
        result = Div(x,y)
        print(result)
    else:
        print("Enter valid value")
