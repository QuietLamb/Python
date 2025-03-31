# class Vector2D :
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def __add__(self, other):
#         return Vector2D(self.x + other.x, self.y + other.y)
#     def __sub__(self, other):
#         return Vector2D(self.x - other.x, self.y - other.y)
#     def __str__(self):
#         return '({}, {})'.format(self.x, self.y)
# v1 = Vector2D(30 ,40)
# v2 = Vector2D(10, 20)
# v3 = v1 + v2
# v4 = v1 - v2
# print(v3)
# print(v4)
# print(v1.__dict__)

# class Cat:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

#     def __str__(self):
#         return 'Cat(name=)' + self.name + ', color=', self.color +')'
    
# nabi = Cat('Nabi', 'Black')
# nero = Cat('Nero', 'White')

# print(nabi)
# print(nero)

class Person:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    
class Employee(Person):
    def __init__(self, name, staff_id):
        Person.__init__(self, name)
        self.staff_id = staff_id
    def info(self):
        return 'Employee: ' + self.get_name() + ', Staff ID: ' + str(self.staff_id)
    
class Manager(Person):
    def __init__(self, name, position):
        Person.__init__(self, name)
        self.position = position
    def info(self):
        return 'Employee: '+ self.get_name() + ', Position: ' + str(self.position)

worker1 = Employee('David', 1111)
worker2 = Employee('Paul', 2222)
cfo = Manager('Anna', 3333, 'CFO')

print(worker1.info())
print(worker2.info())
print(cfo.info())