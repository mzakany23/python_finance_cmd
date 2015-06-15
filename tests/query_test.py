import unittest
import sys
sys.path.append('../lib')
import pandas

from query import Query

class TestPythonXL(unittest.TestCase):

	def setUp(self):
		self.q = Query()

	def test_all_transaction_returns_trans_by_account(self):
		assert self.q.all_transactions('53')

	def test_to_data_frame(self):
		assert self.q.all_transactions('53').to_dataframe().__class__ == pandas.core.frame.DataFrame

	def test_grab_months_transactions(self):
		print self.q.months_transactions(6,2015)

if __name__ == '__main__':
    unittest.main()