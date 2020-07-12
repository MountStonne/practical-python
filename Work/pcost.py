# pcost.py
#
# Exercise 1.27

cost = 0
with open('/Users/shuowang/practical-python/Work/Data/portfolio.csv', 'rt') as portfolio:
    headers = next(portfolio)
    for line in portfolio:
        row = line.split(',')
        shares = float(row[1])
        price = float(row[2])
        cost += shares * price

print('Total cost ', cost)