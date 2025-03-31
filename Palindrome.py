import math
n = int(input("Enter number: "))
reversed = 0
original = n

while n>0:
    last = int(n)%10
    reversed = (reversed*10)+last
    n = n//10
if original == reversed:
    print(original,"Is palindrome num")
else:
    print(original,"Is not palindrome number")

    
    

