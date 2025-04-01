import random as rd

attempt = 0
while True:
    n = int(input('Enter number: '))

    computer = rd.randint(0, 2)

    if n == computer:
        print('Computer choose:', computer)
        print('You are correct')
        print("Number of attemps:", attempt)
    else:
        print('Computer choose:', computer)
        print('You are incorrect')
    attempt += 1
