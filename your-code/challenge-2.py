"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""
import string
from random import choice
from sys import exit

a = string.ascii_lowercase + '0123456789'


def RandomStringGenerator(lenght=12):
    counter = 0
    StringGenerated = ''
    while counter < lenght:
        StringGenerated += choice(a)
        counter += 1
    return StringGenerated


def BatchStringGenerator(StringsNumber, LenghtMin=8, LenghtMax=12):
    List = []
    TempVar = 0
    for counter in range(StringsNumber):
        if LenghtMin < LenghtMax:
            TempVar = choice(range(LenghtMin, LenghtMax))
        elif LenghtMin == LenghtMax:
            TempVar = LenghtMin
        else:
            exit('Incorrect min and max string lengths. Try again.')
        List.append(RandomStringGenerator(TempVar))
    return List


LenghtMin = input('Enter minimum string length: ')
LenghtMax = input('Enter maximum string length: ')
StringsNumber = input('How many random strings to generate? ')

print(BatchStringGenerator(int(StringsNumber), int(LenghtMin), int(LenghtMax)))
