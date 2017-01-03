from person import Person
import csv


class Student(Person):

    @classmethod
    def create_by_csv(cls, filename):
        students_list = []
        f = open(filename)
        for student in csv.reader(f):
            students_list.append(student)
        return students_list

    def __init__(self, first_name, last_name, date_of_birth, gender, class_location, class_annual, energy_level, knowledge_level):
        Person.__init__(self, first_name, last_name, date_of_birth, gender, class_location)
        self.class_annual = class_annual
        self.energy_level = energy_level
        self.knowledge_level = knowledge_level
