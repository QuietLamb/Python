import random

l = 'left'
c = 'center'
r = 'right'

user = input("Choose one(l,c,r): ")


n = int(random.randint(1,3))

if n==1:
    computer = 'left'
elif n==2:
    computer = 'center'
else:
    computer = 'right'

print("Computer chose ",computer)

if(user == l) or (user == c) or (user==r):
    print("No Goal!")
else:
    print("Goal!")

