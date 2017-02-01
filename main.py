def inventory():
    'Shows the inventory for all the items in stock'
    with open('inventory.txt', 'r') as file:
        inventory = file.read()
        return inventory[33:]
print(inventory())

def renting(dress, quan):
    'Calculates rental fees and adds to rented.txt'
    rent = 100
    tax = 1.07
    if dress == 'Prom dress':
        deposit = 200/10 * quan
        pay = tax * rent + deposit
        return pay
    elif dress == 'Wedding dress':
        deposit = 300/10 * quan
        pay = tax * rent + deposit
        return pay
    elif dress == 'Pageant dress':
        deposit = 150/10 * quan
        pay = tax * rent + deposit
        return pay
    elif dress == 'Cocktail dress':
        deposit = 100/10 * quan
        pay = tax * rent + deposit
        return pay
    elif dress == 'Evening dress':
        deposit = 175/10 * quan
        pay = tax * rent + deposit
        return pay
    elif dress == 'Casual dress':
        deposit = 120/10 * quan
        pay = tax * rent + deposit
        return pay
# print(renting('Prom dress', 2))

def purchasing(dress, quan):
    'Calculates replacement fee and adds to replacement.txt'
    tax = 1.07
    if dress == 'Prom dress':
        pay = tax * 200 * quan
        return pay
    elif dress == 'Wedding dress':
        pay = tax * 300 * quan
        return pay
    elif dress == 'Pageant dress':
        pay = tax * 150 * quan
        return pay
    elif dress == 'Cocktail dress':
        pay = tax * 100 * quan
        return pay
    elif dress == 'Evening dress':
        pay = tax * 175 * quan
        return pay
    elif dress == 'Casual dress':
        pay = tax * 120 * quan
        return pay
# print(purchasing('Wedding dress', 1))     

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