import unittest

import sys
sys.path.append('../lib')
sys.path.append('../')

from enviornment_variables import PATH
from excel import Excel
from query import Query


class TestExcel(unittest.TestCase):

	def setUp(self):
		q = Query()
		fifth_third_transactions = q.get_transactions_by_range('53',5,6)
		self.e = Excel(fifth_third_transactions,PATH)

	def test_grouped_transactions(self):
		self.e.grouped_transactions()

if __name__ == '__main__':
    unittest.main()