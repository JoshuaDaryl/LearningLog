#Interactive shopping list, starting with a constructor form list()

print("SHOPPING LIST")

list = list()

while True:
    item = input("Please enter an item to add to your shopping list (type 'Quit' to finish list)\n")
    item = item.capitalize()
    if item != "Quit":
        list.append(item)
        continue
        
    else:
        print(f"Here is yout shopping list:\n {list}")
        quit()

    