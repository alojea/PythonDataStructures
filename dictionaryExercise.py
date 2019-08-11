def printItems(fuitAndVeg):
    for fruit,quantity in fruitAndVegDictionary.items():
        print("Fuit: "+fruit)
        print("Quantity: "+str(quantity))

def printValuesInAscendingOrder(fuitAndVeg):
    print(sorted(fruitAndVegDictionary.values()))

def isTheiteamInTheDictionary(fuitAndVeg):
    while True:
        keyForSearch = input("Type an item for search inside the dictionary \n")

        if not keyForSearch:
            print("Error! Please type a valid item.")
        else:
            break

    if fuitAndVeg.get(keyForSearch) is None:
        print("Key "+str(keyForSearch)+" is not present in the dictionary.")
    else:
        print("The value for the key '"+str(keyForSearch)+"' is "+str(fuitAndVeg.get(keyForSearch)))


fruitAndVegDictionary = { 'apple': 51, 'apricot':42, 'asparagus': 12, 'aubergine': 1, 'avocado': 100,
                          'banana': 200, 'beetroot': 5, 'broccoli': 34, 'butternutsquash' : 150,
                          'carrot': 34, 'clementine': 500, 'courgette': 10, 'elderberry': 800,
                          'fennel': 50, 'fig': 83, 'garlic': 40, 'grapes': 900, 'greenbean': 2,
                          'grapefruit':32, 'iceberglettuce':50, 'kiwi': 11, 'leek': 53, 'lemon': 64,
                          'mango': 93, 'melon': 1, 'mushroom': 89, 'nectarine': 350, 'olive': 1000,
                          'orange': 2500, 'pea': 5000, 'peanut': 5, 'pear': 225,
                          'pepper (red)': 412, 'pineapple': 10, 'pumpkin': 70, 'radish': 679,
                          'rhubarb': 6, 'satsuma': 113, 'strawberry': 412, 'sweetpotato': 532,
                          'tomato': 29, 'turnip': 3, 'vineleaf': 564, 'watercress': 5000, 'watermelon': 40 }

print("1.Write a method to print each item in the dictionary using a for loop. Each item should display the item name and the quantity in the inventory.")
printItems(fruitAndVegDictionary)
print("=========================================")
print("2.Write a method to print the dictionary keys and values in ascending order (by value)")
printValuesInAscendingOrder(fruitAndVegDictionary)
print("=========================================")
print("3. If a product has less than 75 items in the inventory, Marie needs to order more. Print out a list of the products that Marie needs to order more of.")

referenceQuantity = 75

for product,quantity in fruitAndVegDictionary.items():
    if quantity < referenceQuantity:
        print(product+":"+str(quantity)+" ")

print("=========================================")
print("4. Marie has set up a delivery system and needs a way to quickly check if an item exists "
      "in the dictionary and if so how many. Write a method that will check if an item exists in "
      "the dictionary and will print out how many there is in inventory.")
isTheiteamInTheDictionary(fruitAndVegDictionary)