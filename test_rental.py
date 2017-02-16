import main 
inventory = main.load_inventory()

def test_view_inventory():
    'tests the view inventory function on how the inventory is viewed'
    assert main.view_inventory(inventory) == '''Casual dress, 5, 120
Cocktail dress, 8, 100
Evening dress, 9, 175
Pageant dress, 6, 150
Prom dress, 7, 200
Wedding dress, 10, 300'''

def test_renting():
    '''tests the renting function on the outcome when you enter specific dress and quantity 
    (includes 10% deposit fee, rental fee, and tax)'''
    assert main.renting(inventory, 'Prom dress', 1) == (101.07, '$121.40')
    assert main.renting(inventory, 'Evening dress', 4) == (104.28, '$174.90')
    assert main.renting(inventory, 'Casual dress', 3) == (103.21, '$138.52')

def test_purchasing():
    'tests the purchasing function and returns full price for specific item (includes full price and tax)'
    assert main.purchasing(inventory, 'Prom dress', 1) == '214.00'
    assert main.purchasing(inventory, 'Cocktail dress', 2) == '214.00'
    assert main.purchasing(inventory, 'Pageant dress', 5) == '802.50'

def test_returning():
    'tests the returning function and returns the users 10% deposit fee when they return the item'
    assert main.returning(inventory, 'Pageant dress', 1) == '$15.00'
    assert main.returning(inventory, 'Casual dress', 3) == '$36.00'
    assert main.returning(inventory, 'Wedding dress', 5) == '$150.00'
