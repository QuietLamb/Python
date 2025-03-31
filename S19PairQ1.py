# score = [100,90,95,90,80,70,0,80,90,90,0,90,100,75,20,30,50,90]
# chunk_size = 3
# students_grades = (lambda x, n : [x[i:i + n] for i in range(0, len(x), n)])(score, chunk_size)
# valid_student = list(filter(lambda student: all(grade !=0 for grade in student), students_grades))
# print(students_grades)
# print(valid_student)