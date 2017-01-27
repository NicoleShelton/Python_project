def inventory():
    'Shows the inventory for all the items in stock'
    with open('inventory.txt', 'r') as file:
        inventory = file.read()
        return inventory[33:]
print(inventory())

# def renting():
#     'Calculates rental fees and adds to rented.txt'
#     return None

# def purchasing():
#     'Calculates replacement fee and adds to replacement.txt'
#     return None

# def returning():
#     'Subtracts 10% of item and quantity from the total sales'
#     return None

# def total_sales():
#     'Calculates the total sales of all rented items'
#     return None

# def rented():
#     'History of all rented items with dates, quantities, and prices'
#     return None


# if __name__ == '__main__':
#     options = input('What action would you like to take(Enter "inventory, rented, or total")\n')