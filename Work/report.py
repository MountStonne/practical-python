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

portfolio = read_portfolio('Data/portfolio.csv')
prices    = read_prices('Data/prices.csv')

cost = 0.0
for a in portfolio:
    cost += a['shares']*a['price']

print('Total cost', cost)

value = 0.0
for b in portfolio:
    value += b['shares']*prices[b['name']]

print('Current value', value)
print('Gain', value - cost)