from mentor import Mentor
from student import Student


class CodecoolClass:

    def __init__(self):
        self.student_list = Student.create_by_csv()
        self.mentors_list = Mentor.create_by_csv()

    def find_student_by_full_name(self):
        name_of_student = input("Please, give a name")
        for student in self.student_list   :
            if student.__dict__["first_name"] == name_of_student:
                print(student.__dict__)
            else:
                print(student.__dict__)
                print ("No such student, try again")
                break

m = CodecoolClass()
# for mentor in m.mentors_list:
#     print(mentor.__dict__)
m.find_student_by_full_name()
