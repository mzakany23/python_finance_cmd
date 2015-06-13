import pony.orm as pny

class UploadMixin:
	@pny.db_session
	def get_account(self,type):
		try:
			return Account.get(name=type)
		except:
			return 'name should be an account name'

	@pny.db_session
	def transaction_exists(self,trans,account_name):
		
		if account_name == '53':
			dat = trans[0]
			nam = trans[1]
			amt = trans[2]

		exists = pny.select(t for t in Transaction if t.date == dat and t.name == nam and t.amount == amt).exists()
		
		self.type = account_name
		self.exists = exists

		return self


	def get_csv_file_paths_to_upload(self):
		try:
			return  glob.glob("../files/csv/*.csv") or  glob.glob("../files/csv/*.CSV")
		except:
			return 'There are no csv files in the folder'