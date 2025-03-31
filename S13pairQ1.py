s = 0
while s==0:
    try:
        a = int(input("Enter number: "))
        b = int(input("Enter number: "))
        s = a/b
        print(s)
    except ValueError:
        print("Please enter interger")
    except ZeroDivisionError:
        print("Cannot divide by zero")