# pcost.py
#
## Exercise 1.27
# cost = 0
# with open('/Users/shuowang/practical-python/Work/Data/portfolio.csv', 'rt') as portfolio:
#     headers = next(portfolio)
#     for line in portfolio:
#         row = line.split(',')
#         shares = float(row[1])
#         price = float(row[2])
#         cost += shares * price

# print('Total cost ', cost)

# Exercise 1.31
# def portfolio_cost(filename):
#     '''
#     Returns the total cost of portfolio
#     '''
#     cost = 0
#     with open('/Users/shuowang/practical-python/Work/Data/' + str(filename), 'rt') as portfolio:
#         headers = next(portfolio)
#         for line in portfolio:
#             try:
#                 row = line.split(',')
#                 shares = float(row[1])
#                 price = float(row[2])
#                 cost += shares * price
#             except ValueError:
#                 print('Bad row:',row)
    
#     print('Total cost', cost)

## Exercise 1.32
import csv
def portfolio_cost(filename):
    cost = 0
    with open('/Users/shuowang/practical-python/Work/Data/' + str(filename), 'rt') as portfolio:
        rows = csv.reader(portfolio)
        headers = next(rows)
        for row in rows:
            try:
                shares = float(row[1])
                price = float(row[2])
                cost += shares * price
            except ValueError:
                print('Bad row:',row)
    print('Total cost', cost)