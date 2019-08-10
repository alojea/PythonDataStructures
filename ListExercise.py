#!/usr/bin/python
import wordList

numberList = [226, 267, 271, 89, 389, 132, 472, 80, 240, 272, 170, 419, 253, 4, 162, 315, 305]
evenNumbersList = []
numberListOddIndexElements = []

index = 0

for number in numberList:
    if index % 2 != 0:
        numberListOddIndexElements.append(number)
    if number % 2 == 0:
        evenNumbersList.append(number)
    index = index + 1

print("===RESULTS NUMBER LIST====")
print("1. Print the elements at odd-index position:")
print(numberListOddIndexElements)
print("2. Print all the even numbers in the list:")
print(evenNumbersList)
print("3. Print the list in reverse:")

index = len(numberList) - 1

print("[", end="")
while index >= 0:
    if index == 0:
        print(numberList[index], end="")
    else:
        print(numberList[index], end=",")
    index = index - 1
print("]")

wordList.wordListExercise()

