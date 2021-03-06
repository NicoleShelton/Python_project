import csv
import pickle

def load_inventory():
    'Loads up the inventory'
    try:
        with open('inventory.pickle', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return [['Prom dress', 7, 200], ['Wedding dress', 10, 300], ['Pageant dress', 6, 150], ['Cocktail dress', 8, 100], ['Evening dress', 9, 175], ['Casual dress', 5, 120]]

def save_inventory(inventory):
    'Saves the inventory'
    with open('inventory.pickle', 'wb') as file:
        pickle.dump(inventory, file)

class Items:
    def __init__(self, dress, quan, cost):
        self.dress = dress
        self.quan = quan
        self.cost = cost

def inventory_items(inventory, dress, quan, cost):
    'Adds item to inventory list'
    items = Items(dress, quan, cost)
    inventory.append(items)

def view_inventory(inventory):
    'Shows the user the items in stock and prices as a string'
    inven = sorted(inventory)
    return '\n'.join(map(str, inven)).replace('[', '').replace(']', '').replace("'", '').replace("'", '')

def renting(inventory, dress, quan):
    'Calculates rental fees'
    rent = 100
    tax = 1.07
    for item in inventory:
        if item[0] == dress:
            pay = tax * quan * item[2] / 10 + rent
    sale = quan * tax + rent
    return sale, '${:.2f}'.format(pay)

def remove_update_inventory(inventory, dress, quan):
    'Removes item from inventory then updates it with remaining items'
    for data in inventory:
        if data[0] == dress and data[1] >= quan:
            data[1] -= quan
            return True
    return False

def write_to_rented(dress, quan, sale):
    'Writes rented item into rented.csv'
    with open('rented.csv', 'a') as file:
        rent = csv.writer(file)
        rent.writerow([dress, quan, sale])

def mega_rent(dress, quan):
    'adds only the sale amount without deposit from renting() to rented.csv'
    sale, rent = renting(dress, quan)
    print('${:.2f}'.format(rent))
    write_to_rented(dress, quan, sale)

def purchasing(inventory, dress, quan):
    'Calculates replacement fee'
    tax = 1.07
    for item in inventory:
        if item[0] == dress:
            total = tax * item[2] * quan
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

def returning(inventory, dress, quan):
    'Subtracts 10% of item and quantity from the total sales'
    for item in inventory:
        if item[0] == dress:
            returned = item[2] / 10 * quan
    return "${:.2f}".format(returned)

def update_inventory_returning(inventory, dress, quan):
    'Updates inventory for returned item and quantity'
    for data in inventory:
        if data[0] == dress:
            data[1] += quan
    return data
    
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

def add_new(inventory, dress, quan, cost):
    'Adds new item to inventory list'
    item = dress, quan, cost
    inventory.append(list(item))
    return inventory

def add_quan(inventory, dress, quan):
    'Adds quantity to items'
    for data in inventory:
        if data[0] == dress:
            data[1] += quan
    return data

def wipe_inv():
    'Wipes invnetory (Not being called)'
    with open('inventory.pickle', 'wb') as file:
        file.close()

def main():
    inventory = load_inventory()
    while True:
        user = input('Please type "c" if you are a Customer or "o" if you are an Owner (Q to quit)\n')
        if user == 'c':
            print('Welcome to Rent the Dress! Please select an option.')
            cust_options = input('What action would you like to take(Enter "1" = Inventory, "2" = Rent, "3" = Purchase, or "4" = Return")\n')
            if cust_options == '1':
                print('Inventory:\n', view_inventory(inventory))
            elif cust_options == '2' or cust_options == 'rent':
                print('Inventory:\n', view_inventory(inventory))
                dress = input('What dress will you be renting?\n')
                quan = int(input('How many?\n'))
                if remove_update_inventory(inventory, dress, quan) and quan > 0:
                    sale, pay = renting(inventory, dress, quan)
                    write_to_rented(dress, quan, sale)
                    print(sale, pay)
                else:
                    print('Sorry, invalid entry!')
            elif cust_options == '3' or cust_options == 'purchase':
                print('Inventory:\n', view_inventory(inventory))
                dress = input('What dress will you be purchasing?\n')
                quan = int(input('How many?\n'))
                if remove_update_inventory(inventory, dress, quan) and quan > 0:
                    total = purchasing(inventory, dress, quan)
                    write_to_replacement(dress, quan, sale)
                    print(total)
                else:
                    print('Sorry, invalid entry!')
            elif cust_options == '4' or cust_options == 'return':
                dress = input('What dress will you be returning?\n')
                quan = int(input('How many?\n'))
                update_inventory_returning(inventory, dress, quan)
                print(returning(inventory, dress, quan))
        elif user == 'o':
            owner_options = input('What action would you like to take(Enter "1" = Rented, "2" = Replaced, "3" = Add Dress, "4" = Add Quan, "5" = Rent Sales, or "6" = Purchased Sales")\n')
            if owner_options == '1':
                print('Rented:\n', rented())
            elif owner_options == '2':
                print('Replaced:\n', replaced())
            elif owner_options == '3':
                dress = input('What kind of dress?\n').capitalize()
                quan = int(input('How many total of the ' + dress + '?\n'))
                cost = int(input('What is the price of the ' + dress + '?\n'))
                print(add_new(inventory, dress, quan, cost))
            elif owner_options == '4':
                dress = input('Which dress do you want to add quantity to?\n').capitalize()
                quan = int(input('How many?\n'))
                print(add_quan(inventory, dress, quan))
                print(inventory)
            elif owner_options == '5':
                print('Total Sales Rented:\n', total_sales_rented())
            elif owner_options == '6':
                print('Total Sales Replaced:\n', total_sales_purchased())
        elif user == 'Q' or user == 'q':
            print('Have a great day!')
            break
    save_inventory(inventory)

if __name__ == '__main__':
    main()