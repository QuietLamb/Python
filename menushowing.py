menu = {'Americano':3000,'Iced Americano':3500,
        'Cappuchino':4000,'cafe latte':4500,
        'Espresso':3600}

for k,v in menu.items():
    print('The price of {} is {:2d}'.format(k,v))
n = input("Enter :")
if n in menu.keys():
    print("The price of {} is {}".format(n,menu[n]))
else:
    pass