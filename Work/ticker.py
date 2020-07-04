# ticker.py

from follow import follow
import csv

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row
            
def parse_stock_data(lines):
    rows = csv.reader(lines)
    #rows = select_columns(rows, [0, 1, 4])
    rows = ([row[index] for index in [0, 1, 4]] for row in rows)

    #rows = convert_types(rows, [str, float, float])
    rows = ([func(val) for func, val in zip([str, float, float], row)] for row in rows)

    #rows = make_dicts(rows, ['name', 'price', 'change'])
    rows = (dict(zip(['name', 'price', 'change'], row)) for row in rows)
    return rows

def ticker(portfile, logfile, fmt):
    import report, tableformat
    formatter = tableformat.create_formatter(fmt)

    portfolio = report.read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile))
    rows = (row for row in rows if row['name'] in portfolio)

    formatter.headings(['name','price','change'])
    for row in rows:
        formatter.row([ row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"])

if __name__ == '__main__':
    import report
    portfolio = report.read_portfolio('Data/portfolio.csv')
    rows = parse_stock_data(follow('Data/stocklog.csv'))
    rows = filter_symbols(rows, portfolio)
    for row in rows:
        print(row)