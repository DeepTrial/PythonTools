import xlrd
from xlrd import open_workbook
from xlutils.copy import copy


class Excel:
	def __init__(self,filename=None):
		self.fileName=filename
		self.workBook=None
		self.workBook_copy=None
		self.sheetNames=None

	def load(self,filename=None):
		if self.fileName==None:
			self.fileName=filename

		if self.fileName!=None:
			self.workBook = open_workbook(self.fileName)
			self.sheetNames = self.workBook.sheet_names()

	def readfile(self,row,col,sheetIndex):
		sheetList=self.workBook.sheets()
		print(sheetList[sheetIndex].cell_value(row,col))

	def modify(self,sheetIndex,row,col,content):
		self.workBook_copy = copy(self.workBook)
		self.workBook_copy.get_sheet(sheetIndex).write(row,col,content)

	def savefile(self):
		if self.workBook_copy!=None:
			self.workBook_copy.save(self.fileName)


if __name__=="__main__":

	excelPipe=Excel("test.xls")
	excelPipe.load()
	excelPipe.readfile(0,1,0)
	excelPipe.modify(0,5,5,"Deeptrial")
	excelPipe.savefile()
