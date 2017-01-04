from person import Person
import csv


class Student(Person):

    @classmethod
    def create_by_csv(cls, filename = 'data/students.csv'):
        students_list = []
        f = open(filename)
        for student in csv.reader(f):
            students_list.append(student)

        students_obj_lst= []
        for human in students_list:
            students_obj = Student(human[0], human[1], int(human[2]), human[3], human[4], human[5], human[6],
                                       human[7])
            students_obj_lst.append(students_obj)
        return students_obj_lst

    def __init__(self, first_name, last_name, date_of_birth, gender, class_location, class_annual, energy_level, knowledge_level):
        Person.__init__(self, first_name, last_name, date_of_birth, gender, class_location)
        self.class_annual = class_annual
        self.energy_level = energy_level
        self.knowledge_level = knowledge_level
