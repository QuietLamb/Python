import random

def roll_dice(number_of_dice):
    dice = []
    for i in range(number_of_dice):
        dice.append(random.randint(1,6))
    return dice

def roll_again(choices, dice_list):
    num = 0
    for i in choices:
        if i == 'r':
            dice_list[num] = random.randint(1,6)
        num+=1
    return dice_list
def find_winner(c_list,u_list):
    sum_of_com = sum(c_list)
    sum_of_user = sum(u_list)
    print('computer_tota', sum_of_user)
    print('user-total', sum_of_user)
    if sum_of_user > sum_of_com:
        print('user win')
    elif sum_of_user < sum_of_com:
        print('computer win')
    else:
        print('it is tie') 
    
        
def computer_choices(n,c_list):
    choice = '' 
    for i in range(n):
        if c_list[i] < 5:
            choice += 'r'
        else: 
            choice += '-'
    return choice

dice_num = int(input('Enter number of dice: '))
ready = input('Ready? hit any key to start: ')
user_roll = roll_dice(dice_num)
print("user first roll: ", user_roll)
user_choice = input("Enter - to hold or r to roll again: ")
while len(user_choice) != dice_num:
    user_chice = input("invalid answer please Enter - to hold or r to roll again: ") 
roll_again(user_choice,user_roll)
print('Player new roll', user_roll)


computer_roll = roll_dice(dice_num)
print('computer first roll: ', computer_roll)
computer_choice = computer_choices(dice_num,computer_roll)
find_winner(computer_roll,user_roll)