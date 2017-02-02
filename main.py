import csv

def inventory():
    'Shows the inventory for all the items in stock'
    with open('inventory.csv') as file:
       inventory = csv.reader(file)
       header = next(inventory)
       entries = list(inventory)
    return entries
       
print(inventory())

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
dress = input('What dress will you be renting?\n')
quan = int(input('How many?\n'))
pay = renting(dress, quan)
print(pay)
write_to_rented(dress, quan, pay)


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
dress = input('What dress will you be purchasing?\n')
quan = int(input('How many?\n'))
total = purchasing(dress, quan)
print(total)
write_to_replacement(dress, quan, total)

# def total_sales_rented():
#     'Calculates the total sales of all rented items'
#     with open('rented.csv', 'r') as file:
#         total = csv.reader(file)
#         header = next(total)
#         entries = list(total)
#     return None
# print(total_sales())

# def total_sales_purchased():
#     'Calculates the total sales of all purchased items'
#     with open('replacement.csv', 'r') as file:
#         total = csv.reader(file)
#         header = next(total)
#         entries = list(total)
#     return None
# print(total_sales())

# def returning(dress, quan):
#     'Subtracts 10% of item and quantity from the total sales'
#     return None

# def update_inventory_returning():
#     'Updates invenetory for returned item and quantity'
#     return None

# def rented():
#     'Shows all rented items'
#     with open('rented.csv', 'r') as file:
#          total = csv.reader(file)
#          header = next(total)
#          entries = list(total)
#     return entries
# print('Rented:', rented())

# def replaced():
#     'Shows all replaced items'
#     with open('replacement.csv', 'r') as file:
#          total = csv.reader(file)
#          header = next(total)
#          entries = list(total)
#     return entries
# print('Replaced:', replaced())

# if __name__ == '__main__':
#    user = input('Customer or Owner?\n')
#    if user == 'Customer':
#         cust_options = input('What action would you like to take(Enter "Rent, Return, or Purchase")\n')
#    else:
#        owner_options = input('What action would you like to take(Enter "Rented, Replaced, or Total")\n')  