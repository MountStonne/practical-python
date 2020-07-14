# report.py
#
# Exercise 2.7

import csv

def read_portfolio(filename):
    '''Read in the holding from a portfolio'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {
                'name' : row[0],
                'shares' : int(row[1]),
                'price' : float(row[2])
            }
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    '''Read the prices into a dict'''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices
def make_report(portfolio, prices):
    '''Make a table'''
    rows = []
    for prows in portfolio:
        current_price = prices[prows['name']]
        change = current_price - prows['price']
        holding = (prows['name'], prows['shares'], current_price, change)
        rows.append(holding)
    return rows

portfolio = read_portfolio('Data/portfolio.csv')
prices    = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

for r in report:
    print(r)