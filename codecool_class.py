from mentor import Mentor
from student import Student

students_list = Student.create_by_csv("data/students.csv")
students_obj_lst = []
for human in students_list:
    students_obj = Student(human[0], human[1], human[2], human[3], human[4], human[5], human[6], human[7])
    students_obj_lst.append(sudents_obj)
print (students_obj_lst)


class CodecoolClass:
    pass
