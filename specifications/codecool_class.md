# CodecoolClass

## Description
This class represents a real class @ Codecool, containing mentors and students working at the class.

## Parent class
None

## Attributes

* ```location```
  * data type: string
  * description: stores the city where the the class started
* ```year```
  * data type: integer
  * description: stores the year when the class started
* ```mentors```
   * data type: list (containing Mentor objects)
   * description: stores the mentors of the class
* ```students```
  * data type: list (containing Student objects)
  * description: stores the students of the class

## Class methods

### ```create_local_school```

Creates a ```CodecoolClass``` object having some real-life data from the implementer students' real class.

#### Arguments
None

#### Return value

```CodecoolClass``` object

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None

### ```find_student_by_full_name```
Gives back a student with the same full name as the argument from ```students```

#### Arguments
* ```full_name```
  * data_type: string
  * description: holds the full name of the student to be found

#### Return value
```Student``` object

### ```find_mentor_by_full_name```

#### Arguments
* ```full_name```
  * data_type: string
  * description: holds the full name of the mentor to be found

#### Return value
```Mentor``` object

### ```do_gymnastics```
Specified student do gymnastics randomly (1-10) increasing his/her energy level.

#### Arguments
* ```name_of_student```
  * data_type: string
  * description: Name of the student to train

#### Return value
None

### ```give_motivational_speech```
Specified mentor motivates a student increasing his/her knowledge level depending on his/her field of expertise.

#### Arguments
* ```student_to_motivate```
  * data_type: string
  * description: Name of the student to motivate
* ```mentor_that_motivates```
  * data_type: string
  * description: Name of the mentor that motivates

#### Return value
None

### ```check_overal_energy```
Method checks overall energy of all students in a class.

#### Arguments
None

#### Return value
None

### ```saving_into_file```
Method that saves changes in Student's attribute into csv file containing data of all Students.

#### Arguments
None

#### Return value
None
