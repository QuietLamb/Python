lst = range(1,100)
def func1(a):
    def fun2():
        result1 = []
        for i in a:
            if i%5 == 0:
                result1.append(i)
        return result1
    def fun3():
        result2 = []
        for i in a:
            if i%7 == 0:
                result2.append(i)
        return result2
    print(fun2())
    print(fun3())
print(func1(lst))
