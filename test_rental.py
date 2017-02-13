import main 
inventory = main.load_inventory()

def test_view_inventory():
    assert main.view_inventory(inventory) == '''Casual dress, 5, 120
Cocktail dress, 8, 100
Evening dress, 9, 175
Pageant dress, 6, 150
Prom dress, 7, 200
Wedding dress, 10, 300'''

def test_renting():
    assert main.renting(inventory, 'Prom dress', 1) == (101.07, '$121.40')
    assert main.renting(inventory, 'Evening dress', 1) == (101.07, '$118.72')

def test_purchasing():
    assert main.purchasing(inventory, 'Wedding dress', 1) == '321.00'
    assert main.purchasing(inventory, 'Cocktail dress', 2) == '214.00'

def test_returning():
    assert main.returning(inventory, 'Pageant dress', 1) == '$15.00'
    assert main.returning(inventory, 'Casual dress', 3) == '$36.00'
