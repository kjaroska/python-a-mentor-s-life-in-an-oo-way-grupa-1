# Mentor

## Description
This class represents mentors

## Parent class
Person

## Attributes
* ```nickname```
  * data type: string
  * description: stores the secret nickname of a mentor
* ```fields of expertise```
  * data type: string
  * description: stores specialization of the mentor
* ```location```
  * data type: string
  * description: stores the location that mentor works in

## Class methods
None

#### Arguments


#### Return value

## Instance methods

### ```create_by_csv```
Creates a list of mentors from real-life data contained in .csv format file.
Gets a csv file path as an argument (the csv contains all the data needed to instantiate a mentor object) and gives back a list of mentors.

#### Arguments
Path to a .csv file

#### Return value
List of mentors

### ```__init__```
The constructor of the mentor object.

#### Arguments
Everything inherited from Person class plus:
-location,
-field of expertise,
-nickname.

#### Return value
None
