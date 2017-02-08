import csv

def inventory():
    'Puts the items in inventory into a nested list'
    with open('inventory.csv') as file:
        inventory = csv.reader(file)
        header = next(inventory)
        entries = list(inventory)
    return entries

def view_inventory():
    'Shows the user the items in stock and prices as a string'
    inventory()
    return '\n'.join(map(str, inventory())).replace('[', '').replace(']', '').replace("'", '').replace("'", '')

def item_in_inventory():
    'Checks to see if the item is in stock if not it returns "Not in stock"'
    return None

def renting(dress, quan):
    'Calculates rental fees'
    rent = 100
    tax = 1.07
    product_dict = {'Prom dress': 200, 'Wedding dress': 300, 'Pageant dress': 150, 
            'Cocktail dress': 100, 'Evening dress': 175, 'Casual dress': 120}
    pay = quan * tax * product_dict[dress] / 10 + rent
    sale = quan * tax + rent
    return sale, '${:.2f}'.format(pay)

def remove_update_inventory_rent(dress, quan):
    'Removes item from inventory then updates it with remaining items'
    return None

def write_to_rented(dress, quan, sale):
    'Writes rented item into rented.csv'
    with open('rented.csv', 'a') as file:
        rent = csv.writer(file)
        rent.writerow([dress, quan, sale])

def mega_rent(dress, quan):
    sale, rent = renting(dress, quan)
    print('${:.2f}'.format(rent))
    write_to_rented(dress, quan, sale)

def purchasing(dress, quan):
    'Calculates replacement fee'
    tax = 1.07
    product_dict = {'Prom dress': 200, 'Wedding dress': 300, 'Pageant dress': 150, 
            'Cocktail dress': 100, 'Evening dress': 175, 'Casual dress': 120}
    total = tax * product_dict[dress] * quan
    return "{:.2f}".format(total)

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
    with open('total_sales_rented.csv', 'w') as file:
        file.write("${:.2f}".format(total))
    return "${:.2f}".format(total)

def total_sales_purchased():
    'Calculates the total sales of all purchased items'
    with open('replacement.csv', 'r') as file:
        total = csv.reader(file)
        header = next(total)
        entries = list(total)
    total = 0
    for e in entries:
        total += float(e[2])
    return "${:.2f}".format(total)

def returning(dress, quan):
    'Subtracts 10% of item and quantity from the total sales'
    product_dict = {'Prom dress': 200, 'Wedding dress': 300, 'Pageant dress': 150, 
            'Cocktail dress': 100, 'Evening dress': 175, 'Casual dress': 120}
    returned = product_dict[dress] / 10 * quan
    return "${:.2f}".format(returned)

def update_inventory_returning(dress, quan):
    'Updates invenetory for returned item and quantity'
    return None

def rented():
    'Shows all rented items'
    with open('rented.csv', 'r') as file:
        total = file.readlines()[1:]
    return ' '.join(total)

def replaced():
    'Shows all replaced items'
    with open('replacement.csv', 'r') as file:
        total = file.readlines()[1:]
    return ' '.join(total)

if __name__ == '__main__':
    user = input('Customer or Owner?\n')
    if user == 'Customer':
        cust_options = input('What action would you like to take(Enter "Rent, Purchase, or Return")\n')
        if cust_options == 'Rent':
            print('Inventory:\n', view_inventory())
            dress = input('What dress will you be renting?\n')
            quan = int(input('How many?\n'))
            sale, pay = renting(dress, quan)
            write_to_rented(dress, quan, sale)
            print(renting(dress, quan))
        elif cust_options == 'Purchase':
            print('Inventory:\n', view_inventory())
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
        owner_options = input('What action would you like to take(Enter "Rented, Replaced, Rent_sales, or Purchased_sales")\n')
        if owner_options == 'Rented':
            print('Rented:\n', rented())
        elif owner_options == 'Replaced':
            print('Replaced:\n', replaced())
        elif owner_options == 'Rent_sales':
            print('Total Sales Rented:\n', total_sales_rented())
        else:
            print('Total Sales Replaced:\n', total_sales_purchased())
