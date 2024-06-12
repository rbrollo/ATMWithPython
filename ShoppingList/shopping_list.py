shopping_list = []
running = True
OPTIONS = {
    "list" : "l", 
    "insert" : "i", 
    "delete" : "d", 
    "exit" : "e",
    }

while running:
    chosen_option = input("Select an option: \n [i]nsert [d]elete [l]ist [e]xit: ")
    if chosen_option == OPTIONS['list']:
        if not shopping_list:
            print("Your list is empty")
        else:
            for i, item in enumerate(shopping_list, start=1):
                print(i, '-', item)

    elif chosen_option == OPTIONS["insert"]:
        item_add = input("Enter the name of the new item: ")
        shopping_list.append(item_add)
        print(f'{item_add} added to the shopping list')

    elif chosen_option == OPTIONS["delete"]:
        if not shopping_list:
            print("Your list is empty, so there is nothing to delete \n")
            continue
        item_remove = input("Enter the position of the item you want to remove: ")
        try:
            int(item_remove)
            if int(item_remove) > len(shopping_list):
                print("Please indicate a valid position \n")
                continue
        except ValueError:
            print("Please indicate a valid position \n")
            continue
        removed_item = shopping_list[int(item_remove) - 1]
        print(f" The item: {removed_item}, was removed from the shopping list")
        shopping_list.pop(int(item_remove) - 1)

    elif chosen_option == OPTIONS["exit"]:
        print("Exiting...")
        running = False

    else:
        print("Please select a valid option \n")
