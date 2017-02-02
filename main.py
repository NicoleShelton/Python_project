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
    'Calculates rental fees and adds to rented.txt'
    # dress = input('What dress will you be renting?\n')
    # quan = int(input('How many?\n'))
    rent = 100
    tax = 1.07
    product_dict = {'Prom dress': 200, 'Wedding dress': 300, 'Pageant dress': 150, 
            'Cocktail dress': 100, 'Evening dress': 175, 'Casual dress': 120}
    pay = quan * product_dict[dress] / 10 + rent * tax
    return pay

def rent_remove_write(renting):
    # remove from inventory
    # update inventory of total items after rented

    with open('rented.csv', 'a') as file:
        file.writelines(dress + ', ' + str( quan) +  ', ' + str(pay) + '\n')
    
def purchasing(dress, quan):
    'Calculates replacement fee and adds to replacement.txt'
    # dress = input('What dress will you be purchasing?\n')
    # quan = int(input('How many?\n'))
    tax = 1.07
    product_dict = {'Prom dress': 200, 'Wedding dress': 300, 'Pageant dress': 150, 
            'Cocktail dress': 100, 'Evening dress': 175, 'Casual dress': 120}
    total = tax * product_dict[dress] * quan
    return total

# def purchase_remove_write():
#     # remove from inventory
#     # update inventory of total items after purchased
#     with open('replacement.csv', 'a') as file:
#         file.write(dress + ', ' + str( quan) +  ', ' + str(total) + '\n')

# def total_sales():
#     'Calculates the total sales of all rented items'
#     with open('rented.csv', 'r') as file:
#         total = csv.reader(file)
#         header = next(total)
#         entries = list(total)
#     return None
# print(total_sales())

# def returning(dress, quan):
#     'Subtracts 10% of item and quantity from the total sales'
#     return None


# if __name__ == '__main__':
#    user = input('Customer or Owner?\n')
#    if user == 'Customer':
#         cust_options = input('What action would you like to take(Enter "Rent, Return, or Purchase")\n')
#    else:
#        owner_options = input('What action would you like to take(Enter "Rented, Replaced, or Total")\n')  