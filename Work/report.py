#!/usr/bin/env python3
# report.py
#
# Exercise 2.4
import csv, sys, tableformat
from fileparse import parse_csv
from stock import Stock
from portfolio import Portfolio

def read_portfolio(filename):
    with open(filename) as f:
        portdicts = parse_csv(f, select=['name','shares','price'], types=[str, int, float], has_headers=True)
    portfolio = Portfolio( [ Stock(p['name'], p['shares'], p['price']) for p in portdicts] )
    return portfolio

def read_prices(filename):
    with open(filename) as f:
        prices = dict(parse_csv(f, types=[str, float]))
    return prices

def make_report(portfolio, prices):
    report = []
    for holding in portfolio:
        report.append( (holding.name, holding.shares, holding.price, prices[holding.name] - holding.price) )
    return report

def print_report(report, formatter):
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f'{price:0.2f}',  f'{change:0.2f}']
        formatter.row(rowdata)

def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)

    print_report(report, tableformat.create_formatter(fmt))

def main(portfolio_filename, prices_filename, fmt):
    portfolio_report(portfolio_filename, prices_filename, fmt)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile format')
    main(sys.argv[1], sys.argv[2], sys.argv[3])