import csv

def inventory():
    'Shows the inventory for all the items in stock'
    with open('inventory.csv') as file:
        inventory = csv.reader(file)
        header = next(inventory)
        entries = list(inventory)
    return entries

def renting(dress, quan):
    'Calculates rental fees'
    rent = 100
    tax = 1.07
    product_dict = {'Prom dress': 200, 'Wedding dress': 300, 'Pageant dress': 150, 
            'Cocktail dress': 100, 'Evening dress': 175, 'Casual dress': 120}
    pay = quan * product_dict[dress] / 10 + rent * tax
    return pay

def remove_update_inventory_rent():
    'Removes item from inventory then updates it with remaining items'
    return None

def write_to_rented(dress, quan, pay):
    'Writes rented item into rented.csv'
    with open('rented.csv', 'a') as file:
        rent = csv.writer(file)
        rent.writerow([dress, quan, pay])

def purchasing(dress, quan):
    'Calculates replacement fee'
    tax = 1.07
    product_dict = {'Prom dress': 200, 'Wedding dress': 300, 'Pageant dress': 150, 
            'Cocktail dress': 100, 'Evening dress': 175, 'Casual dress': 120}
    total = tax * product_dict[dress] * quan
    return total

def write_to_replacement(dress, quan, total):
    'Writes purchased item into replacement.csv'
    with open('replacement.csv', 'a') as file:
        replace = csv.writer(file)
        replace.writerow([dress, quan, total])

def total_sales_rented():
    'Calculates the total sales of all rented items'
    with open('rented.csv', 'r') as file:
        total = csv.reader(file)
        header = next(total)
        entries = list(total)
    total = 0
    for e in entries:
        total += float(e[2])
    with open('total_sales_rented.csv', 'a') as file:
        file.write(str(total))
    return total

def total_sales_purchased():
    'Calculates the total sales of all purchased items'
    with open('replacement.csv', 'r') as file:
        total = csv.reader(file)
        header = next(total)
        entries = list(total)
    total = 0
    for e in entries:
        total += float(e[2])
    return total

def returning(dress, quan):
    'Subtracts 10% of item and quantity from the total sales'
    product_dict = {'Prom dress': 200, 'Wedding dress': 300, 'Pageant dress': 150, 
            'Cocktail dress': 100, 'Evening dress': 175, 'Casual dress': 120}
    returned = product_dict[dress] / 10 * quan
    return returned

def update_inventory_returning():
    'Updates invenetory for returned item and quantity'
    return None

def rented():
    'Shows all rented items'
    with open('rented.csv', 'r') as file:
        total = csv.reader(file)
        header = next(total)
        entries = list(total)
    return entries

def replaced():
    'Shows all replaced items'
    with open('replacement.csv', 'r') as file:
        total = csv.reader(file)
        header = next(total)
        entries = list(total)
    return entries

if __name__ == '__main__':
    user = input('Customer or Owner?\n')
    if user == 'Customer':
        cust_options = input('What action would you like to take(Enter "Rent, Purchase, or Return")\n')
        if cust_options == 'Rent':
            print('Inventory:', inventory())
            dress = input('What dress will you be renting?\n')
            quan = int(input('How many?\n'))
            pay = renting(dress, quan)
            write_to_rented(dress, quan, pay)
            print(renting(dress, quan))
        elif cust_options == 'Purchase':
            print('Inventory:', inventory())
            dress = input('What dress will you be purchasing?\n')
            quan = int(input('How many?\n'))
            total = purchasing(dress, quan)
            write_to_replacement(dress, quan, total)
            print(purchasing(dress, quan))
        else:
            dress = input('What dress will you be returning?\n')
            quan = int(input('How many?\n'))
            print(returning(dress, quan))
    else:
        owner_options = input('What action would you like to take(Enter "Rented, Replaced, Total_Rent, or Total_Purchased")\n')
        if owner_options == 'Rented':
            print('Rented:', rented())
        elif owner_options == 'Replaced':
            print('Replaced:', replaced())
        elif owner_options == 'Total_Rent':
            print('Total Sales:', total_sales_rented())
        else:
            print('Total Sales:', total_sales_purchased())