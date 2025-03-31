# mylist = [(1,2), (4,5), (4,2), (3,1), (9,4)]

# input = input("Enter: ")
# a,b = map(int,input.split())

# if (a,b) in mylist:
#     position = mylist.index((a,b)) +1
#     print(a,b,"is at",position,"position")
# elif (b,a) in mylist:
#     position = mylist.index((b,a)) +1
#     print(b,a,"is at",position,"position")
# else:
#     print("Both are not on the list")



mylist = [(1,2),(4,5),(4,2),(3,1),(9,4)]
input = input("Enter: ")
a,b = map(int,input.split())

if (a,b) in mylist:
    print(f"These is element{(a,b)} at the {mylist.index(a,b)}")
elif (b,a) in mylist: 
    print(f"{(a,b)} element is not present, but there is a{mylist}")
else:
    print('those element are not present')  
