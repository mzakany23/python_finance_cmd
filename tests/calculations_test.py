import unittest
import sys
sys.path.append('../lib')
import pandas

from query import Query
from calculations import Calculations


class TestPythonXL(unittest.TestCase):

	def setUp(self):
		self.q = Query()
		
	def test_all_transaction_value_counts(self):
		queryset = self.q.all_transactions('53')
		qs = Calculations(queryset)
		assert qs.value_counts().__class__ == pandas.core.series.Series


	def test_just_junes_value_counts(self):
		june_transactions = self.q.get_transactions_by_range('53',6,6)
		qs = Calculations(june_transactions)
		assert qs.value_counts().__class__ == pandas.core.series.Series

	def test_sum(self):
		june_transactions = self.q.get_transactions_by_range('53',6,6)
		qs = Calculations(june_transactions)
		assert qs.sum()

	def test_summary(self):
		june_transactions = self.q.get_transactions_by_range('53',4,6)
		qs = Calculations(june_transactions)
		print qs.summary()
		# for record in qs.summary().iteritems():
		# 	print record[0]
		# 	for x in record[1]['grouped_transaction']:
		# 		print x
		# 	print record[1]['sum']



if __name__ == '__main__':
    unittest.main()