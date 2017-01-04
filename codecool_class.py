from mentor import Mentor
from student import Student


class CodecoolClass:

    def __init__(self,location):
        self.student_list = Student.create_by_csv()
        self.location = location
        self.year





M = CodecoolClass()

print(M)