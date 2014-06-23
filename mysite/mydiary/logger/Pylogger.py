# -------*--------- coding=utf-8 -------*---------
'''
	auther: alec
'''
from datatime import datetime

class Pylogger(object):
	instance=None
	
	def __init(self,logPath):
		self.fp=None
		try:
			if logPath is None:
				self.fp=fopen(logPath+"/web.log","aw")
		except err as Exception:
			raise err
	
	def __new__(cls,*args,**kw):
		if cls.instance is None:
			cls.instance=super(Pylogger,cls).__new__(*args,**kw)
			cls.instance.__init(None)
		return cls.instance
	
	
	def __calNow__(self,endTag):
		print(datetime.now.strftime("%Y-%m-%d %H:%M:%S), [{0}]:".fromat(endTag),file=self.fp)
		
	def print_log(self,data):
		print(data,file=self.fp)
		self.fp.flush()
	
	def info(data):
	    self.__calNow__("info")
		self.print_log(data)
	
	def error(data):
		self.__calNow__("info")
		self.print_log(data)
		
		