from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
import time

def main():
    codecool_krk = CodecoolClass.generate_local()
    time.sleep(0.5)
    codecool_krk.do_gymnastics("Jadwiga Milecka")
    time.sleep(0.5)
    codecool_krk.check_overal_energy()
    time.sleep(0.5)
    codecool_krk.give_motivational_speech("Jadwiga Milecka", "Kamil Jocz")

    codecool_krk.find_student_by_full_name("Marek Sawek")
    codecool_krk.find_student_by_full_name("Mariusz Pudzianowski")

    codecool_krk.find_mentor_by_full_name("Justyna Głowa")
    codecool_krk.find_mentor_by_full_name("Beata Szydło")

    print('Number of Students in Codecool Cracow: {}.'.format(len(codecool_krk.students)))
    print('Number of Mentors in Codecool Cracow: {}.'.format(len(codecool_krk.mentors)))


main()
