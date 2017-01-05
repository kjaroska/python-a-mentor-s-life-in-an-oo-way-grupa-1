from person import Person
import csv


class Student(Person):
    '''Class that inherits basic attributes from Person class, adds 3 attributes of its own and creates a student object.
    '''


    def __init__(self, first_name, last_name, date_of_birth, gender, class_location, class_annual, energy_level, knowledge_level):
        '''Function that initializes class object using given arguments, plus error handling.'''

        Person.__init__(self, first_name, last_name, date_of_birth, gender, class_location)
        self.class_annual = class_annual
        self.energy_level = energy_level
        self.knowledge_level = knowledge_level

        try:
            if not(self.class_annual and self.energy_level and knowledge_level):
                raise TypeError

        except TypeError as class_error:
            class_error.args =  ('At least one of the arguments was not provided.',)
            raise

    @classmethod
    def create_by_csv(cls, filename='data/students.csv'):
        '''Generates students_obj_lst from a .csv file, which is a list of Student class objects.'''

        students_list = []
        f = open(filename)
        for student in csv.reader(f):
            students_list.append(student)

        students_obj_lst = []
        for human in students_list:
            students_obj = Student(human[0], human[1], int(human[2]), human[3], human[4], human[5], int(human[6]),
                                   int(human[7]))
            students_obj_lst.append(students_obj)
        return students_obj_lst