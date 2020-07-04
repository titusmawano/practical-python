class Portfolio:

    def __init__(self, holdings):
        self._holdings = holdings

    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return len(self._holdings)
    
    def __getitem__(self, index):
        return self._holdings[index]
    
    def __contains__(self, name):
        return any( name == stock.name for stock in self._holdings )

    @property
    def total_cost(self):
        return sum( stock.cost for stock in self._holdings )
    
    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for stock in self._holdings:
            total_shares[stock.name] += stock.shares
        return total_shares