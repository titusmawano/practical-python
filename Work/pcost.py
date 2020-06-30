# pcost.py
#
# Exercise 1.27
import sys

def portfolio_cost(filename):
    cost = 0
    with open(filename, 'rt') as f:
        headers = next(f)
        for line in f:
            r = line.split(',')
            try:
                row = ( r[0], int(r[1]), float(r[2]) )
                cost = cost + row[1] * row[2]
            except ValueError:
                print("nada")
    return cost

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(cost)