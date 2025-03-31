cafe_menu = {'Americano':3000, 
        'Iced Americano':3500,
        'Cappuchino':4000, 
        'cafe latte':4500,
        'Espresso':3600}
while True:
    command = input("$ ")
    if command.startswith('q'):
        print("Exit the menu")
        break
    elif command.startswith('<'):
        command = command.replace('<', "")
        new_menu = command.split(':')
        if len(new_menu) < 2:
            print("An input error")
            continue
        else:
            cafe_menu[new_menu[0].strip()] = new_menu[1].strip()
    elif command.startswith('>'):
        command = command.replace('>', "")
        menu = command.split(':')
        key = menu[0].strip()
        if key in cafe_menu:
            print(cafe_menu[key])
        else:
            print(menu,'not in the menu')
    else:
        print("Input error")
