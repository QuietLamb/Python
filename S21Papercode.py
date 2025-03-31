# class Dog:
#     def bark(self):
#         return 'Woof Woof'
    
# my_dog = Dog()

# print(my_dog.bark())

class Dog:
    name = ''
    def __init__(self, name):
        self.name = name
    def bark(self):
        return self.name +' : ' + 'Woof Woof'
    
my_dog = Dog('Bingo')
print(my_dog.bark())