from mentor import Mentor
from student import Student
from person import Person

students_list = Student.create_by_csv("data/students.csv")
students_obj_lst = []
for human in students_list:
    students_obj = Student(human[0], human[1], int(human[2]), human[3], human[4], human[5], human[6], human[7])
    students_obj_lst.append(students_obj.__dict__)
print (students_obj_lst)


class CodecoolClass:
    pass
