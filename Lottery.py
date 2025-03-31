w1, w2, w3 = 2, 3, 9
n=0

a, b, c = input("Enter three numbers separated by commas: ").split(",")
a = int(a)
b = int(b)
c = int(c)

if (a==w1) or (a==w2) or (a==w3):
    n = n+1
    if (b==w1) or (b==w2) or (b==w3):
        n+=1
        if (c==w1) or (c==w2) or (c==w3):
            n+=1
if(n==3):
    print("You won the lottery")
else:
    print("You lost")