class Person:
    '''Class that creates Person object with basic data (name,year of  birth, gender, class locatiom.'''

    def __init__(self, first_name='', last_name='', year_of_birth=0, gender='', class_location=''):
        '''Function that initializes class object and checks given arguments.'''

        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.gender = gender
        self.class_location = class_location

        try:
            if not(self.first_name and self.last_name and self.year_of_birth and self.gender and self.class_location):
                raise TypeError

        except TypeError as class_error:
            class_error.args = ('At least one of the arguments was not provided.',)
            raise

        try:
            if not(type(self.year_of_birth) is int and type(self.first_name) is str and type(self.last_name) is str and
                                                        type(self.gender) is str and type(self.class_location) is str):

                raise TypeError

        except TypeError as class_error:
            class_error.args = ('Incorrect type of argument.',)
            raise

        genders = ('male', 'female', 'notsure')
        locations = ('Cracow')

        try:
            if self.gender.lower() not in genders:
                raise ValueError

        except ValueError as class_error:
                class_error.args = ('Gender is incorrect (indicate either male, female or notsure).',)
                raise

        try:
            if self.class_location not in locations:
                raise ValueError

        except ValueError as class_error:
                class_error.args = ('Location is incorrect (there is no Codecool school in this location).',)
                raise
