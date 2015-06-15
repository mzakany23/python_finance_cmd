import pony.orm as pny
import sys
from pandas import DataFrame
from datetime import datetime, date
import calendar
import re

sys.path.append('../models')
sys.path.append('../')

from all_models import Account,Transaction
from enviornment_variables import DB, DESCRIPTION_LENGTH

class Query:

	@pny.db_session
	def all_transactions(self,name):
		self.frame = pny.select(t for t in Transaction if t.account.name == name)[:]
		return self
											
	@pny.db_session
	def get_transactions_by_range(self,account,month_from,month_to=None,year=2015):
		if month_to is None:
			month_to = datetime.today().month

		account_id = Account.get(name=account).id
		last_day_of_month = calendar.monthrange(year,month_to)[1]

		
		start = date(year,month_from,01).strftime("%m/%d/%Y")
		end = date(year,month_to,last_day_of_month).strftime("%m/%d/%Y")

		db = pny.Database(DB['type'],user=DB['user'],password=DB['password'],host=DB['host'],database=DB['database'])
		
		frame = "* from transaction where to_date(date, 'MM/DD/YYYY') > to_date('%s','MM/DD/YYYY') AND to_date(date, 'MM/DD/YYYY') < to_date('%s','MM/DD/YYYY') AND account = %s" % (start, end, account_id)
		
		self.frame = db.select(frame)

		return self


	def to_dataframe(self):
		frame = []
		cols = ['date','description', 'amount']
		regex = re.compile(r"\X{0,10}[0-9]{0,10}", re.IGNORECASE)
		for x in self.frame:
			description = regex.sub('',x.name)
			frame.append([x.date, description[0:DESCRIPTION_LENGTH], x.amount])

		return DataFrame(frame,columns=cols)











