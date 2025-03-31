print('Plese select one: ')
print('1. Add tasks')
print('2. View all tasks')
print('3. Mark tasks as complete')
print('4. Remove tasks')
print('5. Exit')

task = []
complete = []
num = [1,]

while True:
    user = int(input('Enter number: '))

    def add_task():
        task.append(input("Enter tasks: "))
    def show_task():
        print('======= All tasks ======')
        n = 1
        for i in task:
            if i in complete:
                print(f'{n}. {i} completed', end="")
                n+=1 
                print()
                num.append(n)
            else:
                print(f'{n}. {i}', end=" ")
                n+=1 
                print()
                num.append(n)
    def mark():
        tick = int(input("Choose number: "))
        if tick in num:
            result = task[tick - 1]
            complete.append(result)
    def remove_task():
        remove = int(input('Choose number: '))
        if remove in num:
            task.pop(remove - 1)

    if user == 1:
        add_task()
    elif user == 2:
        show_task()
    elif user == 3:
        mark()
    elif user == 4:
        remove_task()
    elif user == 5:
        print('You exit the program')
        break