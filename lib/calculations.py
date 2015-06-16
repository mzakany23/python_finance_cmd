import sys
import pony.orm as pny
import pandas as pd
from pandas import DataFrame

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

	def summary(self):
		df = self.df
		summed_amount = df['amount'].sum()
		col = [x for x in df.groupby('description').count()['amount']]
		
		new_frame = df.groupby('description').aggregate(sum)
		new_frame['count'] = col
		new_frame['%/whole'] = new_frame['amount']/summed_amount

		return new_frame

	def grouped_by_occurance(self):
		
		rows = {}

		for line in self.df.iterrows():
			date = line[1][0]
			name = line[1][1]
			amount = line[1][2]

			if name in rows.keys():
				rows[name]['grouped_transaction'].append([date,name,amount])
				rows[name]['sum'] += amount
				
			else:
				rows[name] = {
					'grouped_transaction' : [],
					'sum' : 0
				}
				
				rows[name]['grouped_transaction'].append([date,name,amount])
		
		return DataFrame(rows)
	


			
		
		

		
