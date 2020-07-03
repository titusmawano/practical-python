# pcost.py
#
# Exercise 1.27
import sys, csv
from report import read_portfolio

def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    return portfolio.total_cost

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'Data/portfoliodate.csv'

def main(filename):
    cost = portfolio_cost(filename)
    print(cost)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile')
    main(sys.argv[1])