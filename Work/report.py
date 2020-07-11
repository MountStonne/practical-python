# report.py
#
# Exercise 2.4

import csv

def portfolio_cost(filename):
    '''Read in the holding from a portfolio'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (wor[0], int(row[1]), float(wor[2]))
            portfolio.append(holding)
    return portfolio