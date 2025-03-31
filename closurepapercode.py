# def greetings():
#     def say_hi():
#         print('Hello')
#     return say_hi()
# greetings()

# Q2
def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b
    return mul_add
num = calc()
print(num(3))

# Q3
# def calc():
#     a = 3
#     b = 5
#     return lambda x : a * x + b
# num = calc()
# print(num(3))

# Q4

    