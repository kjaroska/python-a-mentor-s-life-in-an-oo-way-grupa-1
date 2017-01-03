# Student

## Description
This class represents a group of students that are attending the class.

## Parent class
Person

## Attributes

* ```knowledge_level```
  * data type: integer
  * description: stores the knowledge level of the student in programming

* ```energy_level```
  * data type: integer
  * description: current energy level

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

Everything inherited from Person class plus knowledge_level and energy_level.

#### Return value
None
