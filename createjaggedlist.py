a = [1,2,3,4,5]
b = []
for i in a:
    line = []
    for j in range(i):
        line.append(j)
        print(j, end=" ")
    b.append(line)
    print()