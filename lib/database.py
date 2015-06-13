import pony.orm as pny
import pandas as pd  
import glob
import os
import sys

sys.path.append('../models')
sys.path.append('../lib/modules')

from all_models import Account,Transaction
from mixins import UploadMixin


class Database(UploadMixin):
	'''
		uploads,validates,queries
	'''

	def __init__(self,folder_location='../files',):
		'''
			folder_location is where you put the csv files
		'''

		self.dir_location = folder_location

	def upload_file_to_database(self):
		return pd.read_csv("../files/csv/53.csv")

	
	@pny.db_session
	def upload_transaction(self,transaction,account_name):
		trans = self.transaction_exists(transaction,account_name)

		if trans.exists == True:
			return 'Already in the database'
		else:
			if trans.type == '53':
				date = transaction[0]
				name = transaction[1]
				amount = transaction[2]
				account = Account.get(id=1)

				Transaction(date=date,name=name,amount=amount,account=account)

