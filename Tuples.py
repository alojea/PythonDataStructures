#!/usr/bin/python
import isCharacterInsideTuple
import convertTupleIntoList
import addValueInsideTuple

alphabetTuple = ('a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
stringTuple = ""


for valueTuple in alphabetTuple:
    stringTuple = stringTuple + valueTuple

print("1.Convert the alphabet tuple to a string and print the string.")
print(stringTuple)
print()
print("2. Output the length of the tuple")
print(len(alphabetTuple))
print()
print("3. Write a program that ask the user to input a character, and will then tell the user whether the character is in the tuple and give its position if it is.")
isCharacterInsideTuple.isCharInsideTuple(alphabetTuple)
print()
print("4. Write a program that will convert the tuple to a list.")
print(type(alphabetTuple)," was converted into ",type(convertTupleIntoList.convertTupleIntoList(alphabetTuple)))
print()
print("5. Write a program that will ask the user for input, and will then add their input to the tuple.")
print(addValueInsideTuple.addValue(alphabetTuple))








