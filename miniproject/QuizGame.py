quiz = {'Capital of China' : 'Beijing', 
        'Capital of Cambodia' :'Cambodia', 
        'Capital of Thailand' :'Bangkok'}

score = 0
for i in quiz:
    answer = input(f'{i} is: ')
    if answer.upper() == quiz[i].upper():
        score += 1
    else:
        print('Wrong answer')
print('Your score is: ',score)
    