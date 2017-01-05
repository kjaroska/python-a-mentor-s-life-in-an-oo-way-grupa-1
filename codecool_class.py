from mentor import Mentor
from student import Student
import random
import csv

class CodecoolClass:
    '''Class that generate codecool class object with list of mentors (separate objects) and list of students
    (also separate objects). This class enable finding mentor/student by its name as well as changing student energy
    and knowledge level.'''


    def __init__(self):
        self.students = Student.create_by_csv()
        self.mentors = Mentor.create_by_csv()
        self.location = 'Cracow'
        self.year = 2016


    def find_student_by_full_name(self):
        '''Function enabling searching for a object from Student class in students list of object
        by given name of a student.'''

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

        print ("No such student.")


    def find_mentor_by_full_name(self):
        '''Function enabling searching for a object from Mentor class in mentors list of object
                by given name of a mentor.'''

        name_of_mentor = (input("Please, give a name and surname of Mentor: ")).split(" ")

        for mentor in self.mentors:
            if mentor.__dict__["first_name"] == name_of_mentor[0] and mentor.__dict__["last_name"] == name_of_mentor[1]:
                choosen_mentor = mentor.__dict__
                print("Name and surname: {} {} Year of birt: {} Gender: {} Class location: {} nickname: {} expertise: {}".format(choosen_mentor["first_name"]\
                ,choosen_mentor["last_name"], choosen_mentor["year_of_birth"]\
                ,choosen_mentor["gender"],choosen_mentor["class_location"]\
                ,choosen_mentor["nickname"],choosen_mentor["field_of_expertise"]))
                return mentor

        print ("No such mentor.")


    def saving_into_file(self):
        '''Function that saves changed attributes of object from Student class into csv file containing students data.'''

        with open('data/students.csv', 'w', encoding='utf-8') as students_list:
            for student in self.students:
                choosen_student = student.__dict__
                values = [choosen_student["first_name"]\
                ,choosen_student["last_name"], str(choosen_student["year_of_birth"])\
                ,choosen_student["gender"], choosen_student["class_location"]\
                ,str(choosen_student["class_annual"]),str(choosen_student["energy_level"])\
                ,str(choosen_student["knowledge_level"])]

                line_to_be_written = ','.join(values)
                students_list.write(line_to_be_written + '\n')

            students_list.close()


    def do_gymnastics(self):
        '''Function that changes energy level attribute of object from Student class (extracted from Students list of
        object) specified by a given name of a Student.'''

        name_of_student = (input("Please, give a name and surname of Student: ")).split(" ")

        try:  #error handling
            name_of_student[1]

        except IndexError:
            print('You have not given proper name and surname of a Student.')

        for student in self.students:
            if student.__dict__["first_name"] == name_of_student[0] and student.__dict__["last_name"] == name_of_student[1]:
                choosen_student = student.__dict__
                choosen_student["energy_level"] += random.randint(1, 10)
                print (choosen_student["first_name"], choosen_student["last_name"], "energy is now:", choosen_student['energy_level'])

        self.saving_into_file()


    def check_overal_energy(self):
        '''Function that provides information about overall energy of class calculated by using energy level attribute
        taken from each object from Student class, being part of Students list'''

        overalEnergy = 0

        for student in self.students:
            overalEnergy +=student.__dict__["energy_level"]

        print(overalEnergy)


    def give_motivational_speech(self):
        '''Function that changes knowledge level attribute of object from Student class (extracted from Students list of
                object) specified by a given name of a Student.'''

        try:  #error handling
            mentor_that_motivates = self.find_mentor_by_full_name().__dict__
            student_to_motivate = self.find_student_by_full_name().__dict__

        except AttributeError:
            print('You have not indicated proper names and surnames of existing student'
                  ' or existing mentor.')
            return None

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

        self.saving_into_file()


    @classmethod
    def generate_local(self):
        '''Function that generates CodecoolClass object.'''
        local_class = CodecoolClass()
        return local_class

m = CodecoolClass()

# m.find_student_by_full_name()
#m.find_mentor_by_full_name()
m.check_overal_energy()
m.do_gymnastics()
m.give_motivational_speech()
