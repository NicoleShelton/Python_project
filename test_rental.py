import main 

def test_inventory():
    assert main.inventory() == '''Prom dress, 7, 200
                               Wedding dress, 10, 300
                               Pageant dress, 6, 150
                               Cocktail dress, 8, 100
                               Evening dress, 9, 175 
                               Casual dress, 5, 120'''


def test_renting():
    assert main.renting('Prom dress') == 128.40
    assert main.renting('Evening dress') == 144.45

def test_purchasing():
    assert main.purchasing('Wedding dress') == 321
    assert main.purchasing('Cocktail dress') == 214

def test_returning():
    assert main.returning('Pageant dress') == 30
    assert main.returning('Casual dress') == 36

def test_total_sales():
    assert main.total_sales('total') == 800
    assert main.total_sales('total') == 500
