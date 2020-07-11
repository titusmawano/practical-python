from .fileparse import parse_csv
from .stock import Stock

class Portfolio:

    def __init__(self):
        self._holdings = []

    @classmethod
    def from_csv(cls, lines, **opts):
        portfolio = cls()
        portdicts = parse_csv(  lines, 
                                select=['name','shares','price'], 
                                types=[str, int, float], 
                                has_headers=True, 
                                **opts)
        for p in portdicts:
            portfolio.append( Stock(**p) )

        return portfolio

    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return len(self._holdings)
    
    def __getitem__(self, index):
        return self._holdings[index]
    
    def __contains__(self, name):
        return any( name == stock.name for stock in self._holdings )

    def append(self, holding):
        self._holdings.append(holding)

    @property
    def total_cost(self):
        return sum( stock.cost for stock in self._holdings )
    
    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for stock in self._holdings:
            total_shares[stock.name] += stock.shares
        return total_shares