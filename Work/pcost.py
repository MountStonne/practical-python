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

## Exercise 1.32 & 1.33
import report
import sys
def portfolio_cost(filename):
    
    portfolio = report.read_portfolio(filename)
    return sum([s['shares']*s['price'] for s in portfolio])

def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfoliofile' % args[0])
    filename = args[1]
    print('Total cost:', portfolio_cost(filename))

if __name__ == '__main__':
    import sys
    main(sys.argv)
