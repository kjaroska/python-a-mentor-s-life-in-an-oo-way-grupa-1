from mentor import Mentor
from student import Student


class CodecoolClass:


    def __init__(self):
        self.students = Student.create_by_csv()
        self.mentors = Mentor.create_by_csv()
        self.location = 'Cracow'
        self.year = 2016


    @classmethod
    def generate_local(self):
        local_class = CodecoolClass()
        return local_class


    def find_student_by_full_name(self):
        name_of_student = (input("Please, give a name and surname: ")).split(" ")

        for student in self.students:
            if student.__dict__["first_name"] == name_of_student[0] and student.__dict__["last_name"] == name_of_student[1]:
                choosen_student = student.__dict__
                print("Name and surname: {} {} Year of birt: {} Gender: {} Class location: {} Class anual: {} Energy level: {} knowledge_level: {}".format(choosen_student["first_name"]\
                ,choosen_student["last_name"], choosen_student["year_of_birth"]\
                ,choosen_student["gender"],choosen_student["class_location"]\
                ,choosen_student["class_annual"],choosen_student["energy_level"]\
                ,choosen_student["knowledge_level"] ))
                return student

        print ("No such student, try again")

    def find_mentor_by_full_name(self):
        name_of_mentor = (input("Please, give a name and surname: ")).split(" ")

        for mentor in self.mentors:
            if mentor.__dict__["first_name"] == name_of_mentor[0] and mentor.__dict__["last_name"] == name_of_mentor[1]:
                choosen_mentor = mentor.__dict__
                print("Name and surname: {\033[91m} {\033[91m} Year of birt: {} Gender: {} Class location: {} nickname: {} expertise: {}".format(choosen_mentor["first_name"]\
                ,choosen_mentor["last_name"], choosen_mentor["year_of_birth"]\
                ,choosen_mentor["gender"],choosen_mentor["class_location"]\
                ,choosen_mentor["nickname"],choosen_mentor["field_of_expertise"]))
                return mentor

        print ("No such mentor, try again")

    @classmethod
    def generate_local(self):
        local_class = CodecoolClass()
        return local_class

m = CodecoolClass()
# for mentor in m.mentors_list:
#     print(mentor.__dict__)
# m.find_student_by_full_name()
m.find_mentor_by_full_name()
