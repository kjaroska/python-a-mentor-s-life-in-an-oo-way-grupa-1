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
* ```class_location```
  * data type: string
  * description: stores the location of the class to which person attends (city).

## Class methods

None


## Instance methods

### ```__init__```
The constructor of the object. Constructor checks given arguments and raises error if any of the arguments is empty, its type is invalid or if provided gender is not valid. 

#### Arguments

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
* ```class_location```
  * data type: string
  * description: stores the location of the class to which person attends (city). 

#### Return value
None


