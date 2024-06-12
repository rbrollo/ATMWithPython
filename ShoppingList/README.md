# Shopping List

This project is a simple shopping list manager in Python. It allows users to add items, list items, delete items, and exit the program.

## Features

- **List Items**: Displays all items in the shopping list.
- **Add Items**: Adds new items to the shopping list.
- **Delete Items**: Removes items from the shopping list by specifying the item's position.
- **Exit**: Exits the program.

## How to Use

1. **Choose an option**:
   - `[i]` - Add item
   - `[d]` - Delete item
   - `[l]` - List items
   - `[e]` - Exit

## Usage Example

```sh
Select an option:
[i]nsert [d]elete [l]ist [e]xit : i
Enter the name of the new item: Apple
Apple added to the shopping list

Select an option:
[i]nsert [d]elete [l]ist [e]xit : l
1 - Apple

Select an option:
[i]nsert [d]elete [l]ist [e]xit : d
Enter the position of the item to remove: 1
The item: Apple, was removed from the shopping list

Select an option:
[i]nsert [d]elete [l]ist [e]xit : e
Exiting...
```

#### Business Rules

- **Add Items**: The user can add any item name.
- **List Items**: Displays all items added to the list. If the list is empty, a message will be displayed.
- **Delete Items**: The user must provide the position of the item in the list to remove it. If the position is invalid or the list is empty, an error message will be displayed.
- **Exit**: Terminates the program execution.

#### Notes

The script is a simple and educational example of a shopping list manager.
There is no data persistence; items are stored only in memory during script execution.
