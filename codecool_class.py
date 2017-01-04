from mentor import Mentor
from student import Student
import random
import csv

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
        name_of_student = (input("Please,  give a name and surname of Student: ")).split(" ")

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
        name_of_mentor = (input("Please, give a name and surname of Mentor: ")).split(" ")

        for mentor in self.mentors:
            if mentor.__dict__["first_name"] == name_of_mentor[0] and mentor.__dict__["last_name"] == name_of_mentor[1]:
                choosen_mentor = mentor.__dict__
                print("Name and surname: {} {} Year of birt: {} Gender: {} Class location: {} nickname: {} expertise: {}".format(choosen_mentor["first_name"]\
                ,choosen_mentor["last_name"], choosen_mentor["year_of_birth"]\
                ,choosen_mentor["gender"],choosen_mentor["class_location"]\
                ,choosen_mentor["nickname"],choosen_mentor["field_of_expertise"]))
                return mentor

        print ("No such mentor, try again")

    def do_gymnastics(self):
        name_of_student = (input("Please, give a name and surname of Student")).split(" ")

        for student in self.students:
            if student.__dict__["first_name"] == name_of_student[0] and student.__dict__["last_name"] == name_of_student[1]:
                choosen_student = student.__dict__
                choosen_student["energy_level"] += random.randint(1, 10)
                print (choosen_student["first_name"], choosen_student["last_name"], "energy is now:", choosen_student['energy_level'])

    def check_overal_energy(self):
        overalEnergy = 0
        for student in self.students:
            overalEnergy +=student.__dict__["energy_level"]
        print(overalEnergy)

    def give_motivational_speech(self):
        mentor_that_motivates = self.find_mentor_by_full_name().__dict__
        student_to_motivate = self.find_student_by_full_name().__dict__
        if mentor_that_motivates['field_of_expertise'] == "Java":
            student_to_motivate["knowledge_level"] += 5
        elif mentor_that_motivates['field_of_expertise'] == "Python":
            student_to_motivate["knowledge_level"] += 10
        elif mentor_that_motivates['field_of_expertise'] == "RubyOnRails":
            student_to_motivate["knowledge_level"] += 1
        elif mentor_that_motivates['field_of_expertise'] == "MySql":
            student_to_motivate["knowledge_level"] += 2
        elif mentor_that_motivates['field_of_expertise'] == "CPP":
            student_to_motivate["knowledge_level"] += 3
        elif mentor_that_motivates['field_of_expertise'] == "PHP":
            student_to_motivate["knowledge_level"] += 4
        print (student_to_motivate["first_name"], student_to_motivate["last_name"], "knowledge is now:", student_to_motivate['knowledge_level'])

        with open('data/students.csv', 'w', encoding='utf-8') as students_list:
            for student in self.students:
                choosen_student = student.__dict__
                line_to_be_written = ', '.join(choosen_student["first_name"]\
                ,choosen_student["last_name"], str(choosen_student["year_of_birth"])\
                ,choosen_student["gender"], choosen_student["class_location"]\
                ,str(choosen_student["class_annual"]),str(choosen_student["energy_level"])\
                ,str(choosen_student["knowledge_level"])
                students_list.write(line_to_be_written + '\n')

            students_list.close()

        #         exp_inv = inventory.items()
        #
        #         for item in exp_inv:
        #             line = map(str, item)
        #             line_to_be_written = ", ".join(line) + "\n"
        #             exported.write(line_to_be_written)
        #
        #     exported.close()
        #     studentwriter = csv.writer(students_list, delimiter = ' ',quotechar = '|', quoting=quoting=csv.QUOTE_MINIMAL)
        #     for student in self.students:
        #         students_list.write()
        #
        # for student in self.students:
        #     print(student.__dict__)

    @classmethod
    def generate_local(self):
        local_class = CodecoolClass()
        return local_class

m = CodecoolClass()
# for mentor in m.mentors_list:
#     print(mentor.__dict__)
# m.find_student_by_full_name()
#m.find_mentor_by_full_name()
m.check_overal_energy()
#m.do_gymnastics()
m.give_motivational_speech()
