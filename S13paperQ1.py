list = ['11','20','X','30','40','50','ABC']
for i in list:
    try:
        print(int(i),end='')
        print()
    except:
        print('Unable to convert {} to an interger'.format(i))