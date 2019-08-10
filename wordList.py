#!/usr/bin/python
wordList = ['dog', 'airport', 'suitcase', 'journey', 'dinosaur', 'coffee', 'code', 'question', 'cannon', 'remind', 'abundant', 'panoramic', 'cushion', 'summer', 'squirrel', 'distribution', 'reminsecent', 'sea', 'shoe']

def wordListExercise():
    print("===RESULTS WORD LIST====")

    print("1. Print each word in the wordList followed by the number of characters in that word.")

    for word in wordList:
        print(word + ":", len(word), "chars")

    print("2. Print all the words with a length less than or equal to 5")
    print("[", end=" ")

    for word in wordList:
        if len(word) <= 5:
            print(word, end=" ")
    print("]")

    print("3. Print all words that contain the letter 's'")
    print("[", end=" ")
    for word in wordList:
        if len(word) <= 5:
            print(word, end=" ")
    print("]")

    print("4. Print many word in the list have an even number of characters.")
    print("[", end=" ")
    for word in wordList:
        if len(word) % 2 == 0:
            print(word, end=" ")
    print("]")
