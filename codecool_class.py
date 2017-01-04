from mentor import Mentor
from student import Student



class CodecoolClass:


    def __init__(self):
        self.students = Student.create_by_csv()
        #self.mentors = 'X'
        self.location = 'Cracow'
        self.year = 2016


    @classmethod
    def generate_local(self):
        local_class = CodecoolClass()
        return local_class


print(CodecoolClass().__dict__)
