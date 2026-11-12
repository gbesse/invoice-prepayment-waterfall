import unittest,copy,json
from invoice_prepayment_waterfall import run
DEMO={'invoice_total': '100.00', 'currency': 'EUR', 'prepayments': [{'id': 'p1', 'amount': '30.00'}, {'id': 'p2', 'amount': '80.00'}]}
class DomainTests(unittest.TestCase):
 def test_overpayment_not_negative_balance(self):
  x=run(DEMO);self.assertEqual(x['balance'],'0.00');self.assertEqual(x['unallocated_prepayment'],'10.00');self.assertEqual(x['allocations'][1]['applied'],'70.00')
 def test_decimal_exact(self):
  x=run(dict(DEMO,prepayments=[{'id':'p1','amount':'30.10'},{'id':'p2','amount':'69.90'}]));self.assertEqual(x['balance'],'0.00');self.assertEqual(x['unallocated_prepayment'],'0.00')
 def test_currency_mismatch(self):
  x=copy.deepcopy(DEMO);x['prepayments'][0]['currency']='USD'
  with self.assertRaises(ValueError):run(x)
