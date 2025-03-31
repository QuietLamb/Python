price_input = input("Enter the price of items: ")
price = price_input.split(';')
price = [int(p.strip()) for p in price] 
price.sort(reverse=True)
for i in price:
    print(i, end="")
    print()
