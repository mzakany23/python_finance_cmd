import sys
import pony.orm as pny
import pandas as pd

sys.path.append('../models')

from query import Query
from all_models import Account,Transaction

class Calculations:

	@pny.db_session
	def __init__(self,query_set):
		self.df = query_set.to_dataframe()

	def value_counts(self):
		return self.df['description'].value_counts()

	def sum(self):
		return self.df['amount'].sum()

	def mcz(self):
		return self.df['description'].groupby('WEB')
