from person import Person
import csv


class Mentor(Person):
    '''Class that inherits basic attributes from Person class, adds 2 attributes of its own and creates a mentor object.
    '''


    def __init__(self, first_name, last_name, date_of_birth, gender, class_location, nickname, field_of_expertise):
        '''Function that initializes class object using given arguments, plus error handling.'''

        Person.__init__(self, first_name, last_name, date_of_birth, gender,  class_location="Cracow")
        self.nickname = nickname
        self.field_of_expertise = field_of_expertise

        try:
            if not(self.nickname and self.field_of_expertise):
                raise TypeError

        except TypeError as class_error:
            class_error.args = ('At least one of the arguments was not provided.',)
            raise

    @classmethod
    def create_by_csv(cls, filename='data/mentors.csv'):
        '''Generates mentors_obj_lst from a .csv file, which is a list of Mentor class objects.'''

        mentors_list = []
        f = open(filename)
        for mentor in csv.reader(f):
            mentors_list.append(mentor)

        mentors_obj_lst = []
        for human in mentors_list:
            mentor_obj = Mentor(human[0], human[1], int(human[2]), human[3], human[4], human[5], human[6])
            mentors_obj_lst.append(mentor_obj)
        return mentors_obj_lst