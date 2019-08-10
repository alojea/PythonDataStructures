#!/usr/bin/python

def isCharInsideTuple(tuple):
    while True:
        valueForSearchInTuple = input("Enter a character for search inside the tuple \n")
        if len(valueForSearchInTuple) > 1:
            print("Error! Please type just one character...Try again")
        else:
            break

    for tupleValue in tuple:
        if tupleValue == str(valueForSearchInTuple):
            print("Character '"+valueForSearchInTuple+"' is inside the tuple!")
            return 'true'

    print("Character '" + valueForSearchInTuple + "' is not inside the tuple.")
    return 'false'
