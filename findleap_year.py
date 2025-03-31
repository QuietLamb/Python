n = int(input("Enter year: "))
result = n%4==0 and n%100!=0 or n%400==0
print("Is this year a leap year", result)