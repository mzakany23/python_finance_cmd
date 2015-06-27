import xlsxwriter
import os
from calculations import Calculations

'''
The purpose is to deal with excel
summary,53, and united tabs
summary calculations, fixed,and var expenses
'''

class Excel:
	def __init__(self,dataset,kwargs):
		self.dataset = dataset
		self.path = kwargs['folder'] + kwargs['filename'] + kwargs['extension']
		self.workbook = xlsxwriter.Workbook(self.path)

	def summary(self):
		pass

	def grouped_transactions(self):
		calculation = Calculations(self.dataset)
		
		worksheet = self.workbook.add_worksheet('Groups')

		worksheet.set_column('A:E',30)
		itemset = calculation.grouped_by_occurance().to_dict().iteritems()
		row_count = 2
		bold = self.workbook.add_format()
		bold.set_bold()
		bold.set_bg_color('yellow')
		grey = self.workbook.add_format()
		grey.set_bg_color('grey')

		worksheet.write("A1",'Key',bold)
		worksheet.write("B1",'Date',bold)
		worksheet.write("C1",'Transaction',bold) 
		worksheet.write("D1",'Amount',bold) 
		worksheet.write("E1",'Sum',bold) 
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


				
		
		


