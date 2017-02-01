import main 

def test_inventory():
    assert main.inventory() == '''
Prom dress, 7, 200
Wedding dress, 10, 300
Pageant dress, 6, 150
Cocktail dress, 8, 100
Evening dress, 9, 175 
Casual dress, 5, 120'''


def test_renting():
    assert main.renting('Prom dress', 1) == 127.0
    assert main.renting('Evening dress', 1) == 124.5

def test_purchasing():
    assert main.purchasing('Wedding dress', 1) == 321.0
    assert main.purchasing('Cocktail dress', 2) == 214.0

def test_returning():
    assert main.returning('Pageant dress, 1') == 30.0
    assert main.returning('Casual dress, 3') == 36.0

def test_total_sales(rented):
    assert main.total_sales('total') == 800.0
    assert main.total_sales('total') == 500.0
