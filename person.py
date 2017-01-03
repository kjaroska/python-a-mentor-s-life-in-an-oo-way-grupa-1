class Person:
    '''Class that creates Person object with basic data (name,yearof birth, gender, class locatiom.'''


    def __init__(self,first_name = 'empty', last_name = 'empty',year_of_birth = 0, gender = 'empty', class_location = 'empty'):
        '''Function that Initializes class object and checks given arguments.'''

        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.gender = gender
        self.class_location = class_location

        if self.first_name == 'empty' or self.last_name == 'empty' or self.class_location == 'empty' \
                or self.gender == 'empty' or self.year_of_birth == 0:
            raise AttributeError('At least one of the attributes of Person class is empty. Indicate first name '
            'last name, year of birth and gender, class location.')

        genders = ('male', 'female', 'notsure')

        if self.gender.lower() not in genders:
            raise AttributeError('Gender attribute is incorrect (please indicate either male, female or notsure).')

        locations = ('Cracow')
        if self.class_location not in locations:
            raise AttributeError('Location attribute is incorrect (there is no such location).')
