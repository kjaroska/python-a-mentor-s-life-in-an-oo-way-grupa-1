# Person


## Description
This class is a Parent class for Student and Mentor class. This class contains basic data of a person (first name, last name, year of birth, gender). 

## Parent class
None

## Attributes

* ```first_name```
  * data type: string
  * description: stores the first name of the person.
* ```last_name```
  * data type: string
  * description: stores the last name of the person.
* ```year_of_birth```
   * data type: integer
   * description: stores the person's year of birth.
* ```gender```
  * data type: string
  * description: stores the person's gender - one from the following collection (male/female/notsure).

## Class methods

None

#### Arguments

None

#### Return value

None.

## Instance methods

### ```__init__```
The constructor of the object. Constructor checks given arguments and raises error if any of the attributes is empty or if provided gender is not valid. 

#### Arguments

All of the arguments of the class itself.

#### Return value
None


