list1 = [3,5,7]
list2 = [2,3,4,5,6]
for j in list2:
    for i in list1:
        print("{}*{}={:2d}".format(i,j,i*j),end="  ")
    print()
        
