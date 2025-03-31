class BankAccount:
    def __init__(self, name, account_num, balance = 0):
        self.name = name
        self.account_num = account_num
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print('{} won has been deposited. The balance now is {}'.format(amount, self.balance))

    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
        else:
            print("Not enough money")

    def __str__(self):
        return 'The balance of {} {} is {:,} won'.format(self.name,self.account_num, self.balance)

account1 = BankAccount('David', '123-0001')
print(account1)
account1.deposit(2000)
print(account1)
account1.withdraw(1000)
print(account1)
account1.withdraw(5000)
