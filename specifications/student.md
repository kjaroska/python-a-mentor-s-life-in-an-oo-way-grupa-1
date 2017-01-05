# Student

## Description
This class represents a group of students that are attending the class.

## Parent class
Person

## Attribute
* ```class_location```
  * data type: string
  * description: city where class location is
* ```knowledge_level```
  * data type: integer
  * description: stores the knowledge level of the student in programming
* ```energy_level```
  * data type: integer
  * description: current energy level
* ```class_annual```
  * data type: integer
  * description: year when Codecool started


## Class methods

### ```create_by_csv```
Creates a list of students from real-life data contained in .csv format file.

#### Arguments
filename - path to .csv file

#### Return value
List of student objects

## Instance methods

### ```__init__```
The constructor of the student object.

#### Arguments
Everything inherited from Person class plus:  
-class_location,
-knowledge_level,
-energy_level,
-class_annual

#### Return value
None
