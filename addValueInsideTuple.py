#!/usr/bin/python

def addValue(originalTuple):
    while True:
        valueForAddInsideTuple = input("Enter a character for insert inside the tuple \n")
        if len(valueForAddInsideTuple) > 1:
            print("Error! Please type just one character...Try again")
        else:
            break
    tmptuple = tuple(valueForAddInsideTuple)
    print("New Tuple:")
    return(tuple(originalTuple)+tmptuple)