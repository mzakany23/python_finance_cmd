import unittest
import sys
sys.path.append('../lib')
import pandas
import xlsxwriter

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
		june_transactions = self.q.get_transactions_by_range('53',3,6)
		qs = Calculations(june_transactions)
		assert qs.summary().__class__ == pandas.core.frame.DataFrame

	def test_date_range(self):
		june_transactions = self.q.get_transactions_by_range('53',3,6)
		qs = Calculations(june_transactions)
		assert qs.date_range().__class__ == list

	def test_grouped_by_occurance(self):
		workbook = xlsxwriter.Workbook('/Users/mzakany/Desktop/demo.xlsx')
		worksheet = workbook.add_worksheet()
		trans = self.q.get_transactions_by_range('53',3,6)
		qs = Calculations(trans)
		row_count = 2
		itemset = qs.grouped_by_occurance().to_dict().iteritems()
		# for x,y in itemset:
		# 	print x
		# 	for x in y['grouped_transaction']:
		# 		print x

		for x,y in itemset:
			worksheet.write("A%s" % str(row_count),x) 
			row_count += 2
			for row in y['grouped_transaction']:
				worksheet.write("B%s" % str(row_count),row[0]) 
				worksheet.write("C%s" % str(row_count),row[1]) 
				worksheet.write("D%s" % str(row_count),row[2]) 
				row_count += 1
			worksheet.write("E%s" % str(row_count),y['sum']) 
			row_count += 1



	

if __name__ == '__main__':
    unittest.main()