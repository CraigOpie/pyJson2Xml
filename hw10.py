#!/usr/bin/env python
"""
Name:   Craig Opie
Class:  CENT110
File:   hw10.py

Algorithm:
1)  Import the 'loads' function from the json module.
2)  Define a function called 'name' that accepts a string type attribute:
    A.  Create a variable to store the attribute (names) and remove spaces and split by ",".
    B.  Store the firstName XML data as a string on a new line in 'return_'.
    C.  Store the lastName XML data as a string on a new line in 'return_'.
    D.  Return 'return_'
3)  Define a function called 'hwAvg' that accepts a list type attribute:
    A.  Create 'hwAvg' to store the sum of the attribute divided by the len of the attribute.
    B.  Return 'hwAvg' as XML data.
4)  Define a function called 'exam' that accepts a float type attribute:
    A.  Return the attribute as XML data.
5)  Take input from the user to specify the filename of the JSON file and store in 'filename'.
6)  Open 'filename' as 'infile':
    A.  Read the data in filename and store as a string in 'contentsIn', then close 'infile'.
7)  Create a new dictionary using 'loads' to process 'contentsIn' and store in 'studentsDict'.
8)  Create a new list using 'studentsDict['roster'] and store in 'studentsList'.
9)  Create the first line of the XML file and store in 'contentsOut'.
10) Create the second line of the XML file and add to 'contentsOut'.
11) Process through each value in 'studentsList':
    A.  Add '<student>' tag to 'contentsOut'.
    B.  Provide key['name'] to 'name' for processing and add to 'contentsOut'.
    C.  Provide key['hwscores'] to 'hwAvg' for processing and add to 'contentsOut'.
    D.  Provide key['exam'] to 'exam' for processing and add to 'contentsOut'.
    E.  Add '</student>' tag to 'contentsOut'.
12) Add '</roster>' tag to 'contentsOut'.
13) Change the .json or .JSON extension to .xml for 'filename'.
14) Create 'filename' as 'outfile':
    A.  Write the string 'contentsOut' to 'outfile', then close 'outfile'.
"""
from json import loads

def name(names):
    """
    Input must be of string type.
    Process name data into first and last names, then return a string in xml format.
    """
    names = names.replace(" ","").split(",")
    return_ = ('\n        <firstName>'+names[0]+'</firstName>')
    return_ += ('\n        <lastName>'+names[1]+'</lastName>')
    return(return_)

def hwAvg(scores):
    """"
    Input must be of list type containing integers or floats.
    Process homework scores into an average, then return a string in xml format.
    """
    hwAvg = sum(scores)/len(scores)
    return('\n        <hwaverage>'+("%.2f" % hwAvg)+'</hwaverage>')

def exam(scores):
    """
    Process homework score, then return a string in xml format.
    """
    return('\n        <exam>'+("%.2f" % scores)+'</exam>')

# User specifies a JSON filename for conversion
filename = input("Please enter the JSON filename for conversion to XML: ")

# Open the JSON file, store as string in contents, then close the file
with open(filename, "r") as infile:
    contentsIn = infile.read()

# Load the value of contents into a dictionary
studentsDict = loads(contentsIn)

# Load the first key in the dictionary and store as a list
studentsList = studentsDict['roster']

# Create the string value to store the information for outfile, write the xml header information
contentsOut = '<?xml version="1.0" ?>'
contentsOut += '\n<roster>'

# Add each students data to 'contents'
for key in studentsList:
    contentsOut += '\n    <student>'
    contentsOut += name(key['name'])
    contentsOut += hwAvg(key['hwscores'])
    contentsOut += exam(key['exam'])
    contentsOut += '\n    </student>'

# Add the closing tag for the XML file
contentsOut += '\n</roster>'

# Convert the user specified filename to an XML output for the outfile
filename = filename.replace(".json", ".xml").replace(".JSON", ".xml")

# Create the XML file, write the value of contents, then close the XML file
with open(filename, "w") as outfile:
    outfile.write(contentsOut)
