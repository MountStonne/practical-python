# report.py
#
# Exercise 2.7

import fileparse

def read_portfolio(filename):
    '''Read in the holding from a portfolio'''

    with open(filename) as lines:
        return fileparse.parse_csv(filename, select=['name','shares','price'], types=[str,int,float])

def read_prices(filename):
    '''Read the prices into a dict'''
    with open(filename) as lines:
        return dict(fileparse.parse_csv(filename,types=[str,float], has_headers=False))

def make_report(portfolio, prices):
    '''Make a table'''

    rows = []
    for prows in portfolio:
        current_price = prices[prows['name']]
        change = current_price - prows['price']
        holding = (prows['name'], prows['shares'], current_price, change)
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

def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)