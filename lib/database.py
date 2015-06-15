import pony.orm as pny
import pandas as pd  
import glob
import os
import sys

sys.path.append('../models')
sys.path.append('../lib/modules')
sys.path.append('../')

from all_models import Account,Transaction
from mixins import UploadMixin
from enviornment_variables import ACCOUNT_NAMES

class Database(UploadMixin):
	'''
		uploads,validates,queries
	'''

	def __init__(self,folder_location='../files',):
		'''
			folder_location is where you put the csv files
		'''

		self.dir_location = folder_location

	def upload_files_to_database(self):
		uploads = self.get_csv_file_paths_to_upload()
		success = False

		if uploads is not False:
			for file in uploads:
				for account in ACCOUNT_NAMES.iteritems():
					name_of_account_in_hash = str(account[0])
					name_of_account_in_files_folder = str(os.path.basename(file).lower())
					
					if name_of_account_in_hash + '.csv' == name_of_account_in_files_folder:
						
						for row in pd.read_csv(file).iterrows():
							data_frame_row = row[1]
							account_hash_options = account[1]

							date = data_frame_row[account_hash_options[0]] 
							description = data_frame_row[account_hash_options[1]]
							amount = data_frame_row[account_hash_options[2]]

							formatted_row = [date,description,amount]
														
							self.upload_transaction(formatted_row,name_of_account_in_hash)

							success = True
						
			return success
					

	
	@pny.db_session
	def upload_transaction(self,transaction,account_name):
		transaction_exists = self.transaction_exists(transaction,account_name)

		if transaction_exists == True:
			return 'Already in the database'
		else:
			date = transaction[0]
			name = transaction[1]
			amount = transaction[2]
			account = Account.get(name=account_name)
			
			Transaction(date=date,name=name,amount=amount,account=account)

