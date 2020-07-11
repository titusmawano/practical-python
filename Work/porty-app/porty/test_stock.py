import stock
import unittest

class TestStock(unittest.TestCase):

    def test_create(self):
        s = stock.Stock('GOOG', 12, 14.4)
        self.assertEqual(s.name, 'GOOG')
    
    def test_bad_shares(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
        s.shares = '100'

if __name__ == '__main__':
    unittest.main()