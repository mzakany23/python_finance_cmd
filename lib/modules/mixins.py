import pony.orm as pny
import sys
import glob
import os

sys.path.append('../../models')
sys.path.append('../../')

from all_models import Account,Transaction
import enviornment_variables 

class UploadMixin:
	@pny.db_session
	def get_account(self,type):
		try:
			return Account.get(name=type)
		except:
			return False

	@pny.db_session
	def transaction_exists(self,trans,account_name):		
		return pny.select(t for t in Transaction if t.date == trans[0] and t.name == trans[1] and t.amount == trans[2]).exists()
	
	def get_csv_file_paths_to_upload(self):
		try:
			return  glob.glob("../files/csv/*.csv") or  glob.glob("../files/csv/*.CSV")
		except:
			return 'There are no csv files in the folder'