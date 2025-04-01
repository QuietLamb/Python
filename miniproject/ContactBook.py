contact = {'Channy': [11111,'Channy@gmail.com'], 
           'Neang': [22222,'neangneang@gmail.com']}

def add():
    n = input('Enter name: ')
    c = input('Enter number: ')
    e = input('Enter Email: ')
    contact[n] = [c,e]
def search():
    user = input('Enter name: ')
    if user in contact.keys():
        print(contact[user])
def delete():
    user = input('Enter name: ')
    contact.pop(str(user))

