class Student:
    def __init__(self, name = 'Unknown', Id = 0, eng_score = 0, math_score = 0, science_score = 0):
        self.name = name
        self.Id = Id
        self.eng_score = eng_score
        self.math_score = math_score
        self.science_score = science_score
    def __str__(self):
        return "Name: {} Id: {} \nEnglish Score: {}, Math Score: {}, Science Score: {} ".format(self.name, self.Id, self.eng_score, self.math_score, self.science_score)

    def __add__(self):
        self.total = self.math_score + self.eng_score + self.science_score
        return 'Total score: {}'.format(self.total)
    
    def average(self):
        self.result = self.total/3
        return 'Average score: {}'.format(self.result)
        

stu = Student()
stu.name = input("Enter name: ")
stu.Id = int(input("Enter Id: "))
stu.eng_score = int(input("Enter English score: "))
stu.math_score = int(input("Enter Math score: "))
stu.science_score = int(input("Enter Science score: "))

print(stu.__add__(),", ", stu.average())