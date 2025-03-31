import random

n = int(input("Enter Number: "))
attemp = 0
computer = random.randint(1,5)

while n!=computer:
    print("computer chose: ",computer)
    if n<computer:
        print("Lower")       
    else:
        print("Higher")
    n = int(input("Enter Number: "))
print("Correct")
attemp+=1
print("Total attemp: ",attemp)



    
