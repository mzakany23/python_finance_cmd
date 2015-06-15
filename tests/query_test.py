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

	def test_get_this_months_transactions(self):
		assert self.q.get_transactions_by_range('53',6,6)	

	def test_get_range_of_transactions(self):
		assert self.q.get_transactions_by_range('53',3,4)

	def test_take_transactions_to_dataframe(self):
		assert self.q.get_transactions_by_range('53',3,4).to_dataframe()

	def test_take_transactions_to_dataframe(self):
		print self.q.get_transactions_by_range('united',4,4).to_dataframe()

if __name__ == '__main__':
    unittest.main()