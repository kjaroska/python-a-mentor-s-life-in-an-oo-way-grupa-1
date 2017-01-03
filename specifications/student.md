# Student

## Description
This class represents a group of students that are attending the class.

## Parent class
Person

## Attributes

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

## Instance methods

### ```create_by_csv```

Creates a list of students from real-life data contained in .csv format file.

#### Arguments

path to .csv file

#### Return value

List of students

### ```__init__```

The constructor of the student object.

#### Arguments

Everything inherited from Person class  
-class_location,
-knowledge_level,
-energy_level,
-class_annual

#### Return value
None
