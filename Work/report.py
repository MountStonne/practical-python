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
            record = dict(zip(headers, row))
            holding = {
                'name' : record['name'],
                'shares' : int(record['shares']),
                'price' : float(record['price'])
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
        current_price_label = '$' + str(prices[prows['name']])
        change = current_price - prows['price']
        holding = (prows['name'], prows['shares'], current_price_label, change)
        rows.append(holding)
    return rows

# portfolio = read_portfolio('Data/portfolio.csv')
# prices    = read_prices('Data/prices.csv')
# report = make_report(portfolio, prices)

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(('-' * 10 + ' ') * 4)
    for r in report:
        print('%10s %10d %10s %10.2f' % r)

def portfolio_report(filename_portfolio, filename_price):
    '''Make a report'''
    portfolio = read_portfolio(filename_portfolio)
    prices = read_prices(filename_price)
    report = make_report(portfolio,prices)

    print_report(report)

portfolio_report('Data/portfolio.csv',
                 'Data/prices.csv')