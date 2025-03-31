import random

seat = []
avaiable = 0

for i in range(3):
    line = []
    for j in range(6):
        rand = random.randrange(0,2)
        line.append(rand)
    seat.append(line)

for i in range(3):
    for j in range(6):
        print(seat[i][j], '',end='')
        if (seat[i][j]==0):
            avaiable+=1
    print()
print("The number of avaiable seat is: ",avaiable)