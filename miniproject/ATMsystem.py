print('======== Welcome to Channy Bank==========')
print('1. Check balance')
print('2. Deposit money')
print('3. Withdraw money')
print('4. History')
print('5. Exit')

customer = {'Name':'Channy', 'Balance':1000, 'Password':'sokneang'}
History = []

password = input('Please Enter password: ')

def check():
    print('You balance is: ',customer['Balance'])
def deposit():
    money = int(input("Enter amount of money: "))
    customer['Balance']+= money
    History.append(money)
    print('You have add: ',money)
def withdraw():
    money = int(input("Enter amount of money: "))
    customer['Balance']-= money
    print('You withdraw: ',money)
def history():
    print(History, end="")
    print()

while password == customer['Password']:
    user = int(input('Please choose one: '))
    if user == 1:
        check()
    elif user == 2:
        deposit()
    elif user == 3:
        withdraw()
    elif user == 4:
        history()
    elif user == 5:
        print('Exit the system')
        break
    else:
        print('Please input again')
        print()
      