class Person:


    def __init__(self,first_name = 'empty', last_name = 'empty',year_of_birth = 0, gender = 'empty'):

        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.gender = gender

    #   if (self.first_name or self.last_name or self.gender) == 'empty' or year_of_birth == 0:
    #       raise AttributeError('One of the attributes of Person class is empty.')



    def __str__(self):
        return '{}, {}, {}, {}'.format(self.first_name,self.last_name, self.year_of_birth, self.gender)










