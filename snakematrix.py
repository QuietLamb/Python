n = int(input("Enter: "))
row = n
cols = n
total = n*n

for i in range(1,total):
    print(i,end=" ")
    if(i%cols==0):
        print()
    

