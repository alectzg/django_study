# -------*--------- coding=utf-8 -------*---------
'''
	auther: alec
'''
from datetime import datetime

class Pylogger(object):
	instance = None
	
	def __init(self, logPath):
		self.fp = None
		try:
			if logPath is None:
				logPath = "G://django_serv/"
			self.fp = open(logPath + "/web.log", "a")
		except Exception as err:
			raise err
	
	@classmethod
	def __new__(cls, *args, **kw):
		if cls.instance is None:
			cls.instance = super(Pylogger, cls).__new__(*args, **kw)
			cls.instance.__init(None)
		return cls.instance
	
	
	def __calNow__(self, endTag):
		print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "[{0}]:".format(endTag), file=self.fp,end=" ")
		
	def print_log(self, data):
		print(data, file=self.fp)
		self.fp.flush()
	
	def info(self, data):
		self.__calNow__("info")
		self.print_log(data)
	
	def error(self, data):
		self.__calNow__("info")
		self.print_log(data)
		
		
