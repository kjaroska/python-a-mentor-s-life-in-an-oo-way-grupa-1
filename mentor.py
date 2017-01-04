from person import Person
import csv

class Mentor(Person):

    @classmethod
    def create_by_csv(cls, filename = 'data/mentors.csv'):
        mentors_list = []
        f = open(filename)
        for mentor in csv.reader(f):
            mentors_list.append(mentor)

        mentors_obj_lst= []
        for human in mentors_list:
            mentor_obj = Mentor(human[0], human[1], int(human[2]), human[3], human[4], human[5], human[6])
            mentors_obj_lst.append(mentor_obj)
        return mentors_obj_lst

    def __init__(self, first_name, last_name, date_of_birth, gender, class_location, nickname, field_of_expertise):
        Person.__init__(self, first_name, last_name, date_of_birth, gender,  class_location = "Cracow")
        self.nickname = nickname
        self.field_of_expertise = field_of_expertise
