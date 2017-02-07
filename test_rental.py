import main 

def test_inventory():
    assert main.inventory() == [['Prom dress', ' 7', ' 200'], ['Wedding dress', ' 10', ' 300'], ['Pageant dress', ' 6', ' 150'], 
    ['Cocktail dress', ' 8', ' 100'], ['Evening dress', ' 9', ' 175'], ['Casual dress', ' 5', ' 120']]

def test_view_inventory():
    assert main.view_inventory() == '''
Prom dress, 7, 200
Wedding dress, 10, 300
Pageant dress, 6, 150
Cocktail dress, 8, 100
Evening dress, 9, 175
Casual dress, 5, 120'''

def test_renting():
    assert main.renting('Prom dress', 1) == (101.07, '121.40')
    assert main.renting('Evening dress', 1) == (101.07, '118.72')

def test_purchasing():
    assert main.purchasing('Wedding dress', 1) == '321.00'
    assert main.purchasing('Cocktail dress', 2) == '214.00'

def test_returning():
    assert main.returning('Pageant dress', 1) == '15.00'
    assert main.returning('Casual dress', 3) == '36.00'

# def test_total_sales_rented():
#     assert main.total_sales_rented() == '800.00'

# def test_total_sales_purchased():
#     assert main.total_sales_purchased() == '500.00'