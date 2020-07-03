# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(lines, select=None, types=[], has_headers=False, delimiter=',', silence_errors=True):
    '''
    Parse a csv file into a list of records
    '''

    if isinstance(lines, str):
        raise ValueError('Csv is not formed correctly')

    if select and not has_headers:
        raise RuntimeError('Select arguement requires column headers')

    records = []
    rows = csv.reader(lines, delimiter=delimiter)

    headers = next(rows) if has_headers else []
    if select:
        #Find indices of selected names
        indices = [ headers.index(colname) for colname in select]
        headers = select
            
    for rowno, row in enumerate(rows, 1):
        if row:
            if select:
                row = [ row[idx] for idx in indices ] #filter selected columns
            
            try:
                if types:
                    #Apply type casting
                    typed_row = [ func(val) for func, val in zip(types, row)]
                    row[0:len(typed_row)] = typed_row
            except ValueError as e:
                if not silence_errors:
                    print(f'Row {rowno} Could not convert {row}')
                    print(f'Row Reason : {e}')
                
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)

            records.append(record)
                
    return records
