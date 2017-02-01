def inventory():
    'Shows the inventory for all the items in stock'
    with open('inventory.txt', 'r') as file:
        inventory = file.read()
        return inventory[33:]
print(inventory())

def renting():
    'Calculates rental fees and adds to rented.txt'
    rent = 100
    tax = 1.07
    if dress == 'Prom dress':
        deposit = 200/10 * quan
        pay = tax * rent + deposit
    elif dress == 'Wedding dress':
        deposit = 300/10 * quan
        pay = tax * rent + deposit
    elif dress == 'Pageant dress':
        deposit = 150/10 * quan
        pay = tax * rent + deposit
    elif dress == 'Cocktail dress':
        deposit = 100/10 * quan
        pay = tax * rent + deposit
    elif dress == 'Evening dress':
        deposit = 175/10 * quan
        pay = tax * rent + deposit
    elif dress == 'Casual dress':
        deposit = 120/10 * quan
        pay = tax * rent + deposit

    with open('rented.txt', 'a') as file:
        file.write(dress + ' ' + str( quan) + '\n')
    return pay
print(renting()) 

def purchasing():
    'Calculates replacement fee and adds to replacement.txt'
    tax = 1.07
    if dress == 'Prom dress':
        total = tax * 200 * quan
    elif dress == 'Wedding dress':
        total = tax * 300 * quan
    elif dress == 'Pageant dress':
        total = tax * 150 * quan
    elif dress == 'Cocktail dress':
        total = tax * 100 * quan
    elif dress == 'Evening dress':
        total = tax * 175 * quan
    elif dress == 'Casual dress':
        total = tax * 120 * quan

    with open('replacement.txt', 'a') as file:
        file.write(dress + ' ' + str( quan) + '\n')
    return total
print(purchasing())

# def returning(dress, quan):
#     'Subtracts 10% of item and quantity from the total sales'
#     return None

# def total_sales(rented):
#     'Calculates the total sales of all rented items'
#     return None

# def rented():
#     'History of all rented items with dates, quantities, and prices'
#     return None


# if __name__ == '__main__':
#     options = input('What action would you like to take(Enter "inventory, rented, or total")\n')