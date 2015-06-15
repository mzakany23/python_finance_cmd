import pony.orm as pny
import sys
from pandas import DataFrame
from datetime import datetime, date
import calendar

sys.path.append('../models')
sys.path.append('../')

from all_models import Account,Transaction
from enviornment_variables import DB

class Query:

	@pny.db_session
	def all_transactions(self,name):
		self.frame = pny.select(t for t in Transaction if t.account.name == name)[:]
		return self

	def to_dataframe(self):
		frame = []
		cols = ['date','description', 'amount']
		for x in self.frame:
			frame.append([x.date, x.name[0:20], x.amount])

		return DataFrame(frame,columns=cols)

	@pny.db_session
	def months_transactions(self,month,year=2015):
		last_day_of_month = calendar.monthrange(year,month)[1]
		start = date(year,month,01).strftime("%m/%d/%Y")
		end = date(year,month,last_day_of_month).strftime("%m/%d/%Y")
		db = pny.Database(DB['type'],user=DB['user'],password=DB['password'],host=DB['host'],database=DB['database'])
		query = "* from transaction where to_date(date, 'MM/DD/YYYY') > to_date('%s','MM/DD/YYYY') AND to_date(date, 'MM/DD/YYYY') < to_date('%s','MM/DD/YYYY')" % (start, end)
		return db.select(query)
										
			
		

		