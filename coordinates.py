x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x>0 and y>0:
    print("In the 1 quadrant")
elif x>0 and y<0:
    print("In the 4 quadrant")
elif x<0 and y>0:
    print("In the 2 quadrant")
else:
    print("In the 3 quadrant")