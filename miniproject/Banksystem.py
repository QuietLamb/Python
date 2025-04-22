class BankAccount:
    def __init__(self, name = None, id = None, password = None, balance = 0):
        self.name = name
        self.id = id
        self.__password = password
        self.__balance = balance
    
    def __str__(self):
        return f"Account Name: {self.name}\nAccount Id: {str(self.id)}\nBalance: {self.__balance}"

    @property
    def balance(self):
        return self.__balance
    @property
    def password(self):
        return self.__password
    
    def deposit(self,depo_balance):
        self.__balance += depo_balance
        print(f'You Deposited: {depo_balance}')
    
    def withdraw(self,withdraw_balance):
        self.__balance -= withdraw_balance
        print(f'You Withdrawl: {withdraw_balance}')

Channy = BankAccount('Channy','1001','1111',1000) 
Neang = BankAccount('Neang','1002','2222',2000)
setname = BankAccount()

Database = [Channy, Neang]

print('======== Welcome to Doji Bank ========')
print('Please Log in first')
n = input('Enter Account Name: ')
p = input('Enter Password: ')
login = 0
for i in Database:
    if i.name == n and i.password == p:
        print('Please choose one option:')
        print('1.Account Infomation')
        print('2.Deposit')
        print('3.Withdrawl')
        print('4.Exit')
        print('5.Add Account')
        login += 1
        n = i
        break
    else:
        print('Invalid name or password')
        break

while login == 1:
    user = int(input('Enter Option: '))
    if user == 1:
        print(n.__str__())
    elif user == 2:
        amount = int(input('Enter Amount: '))
        n.deposit(amount)
    elif user == 3:
        amount = int(input('Enter Amount: '))
        n.withdraw(amount)
    elif user == 4:
        break
    elif user == 5:
        setname = input('Enter Account Name: ')
        setid = input('Enter Account ID: ')
        setpassword = input('Enter Password: ')
        Database.append(setname)
        print(setname.__str__())
    else:
        print('Please input again')
