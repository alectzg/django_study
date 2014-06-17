#------ coding=utf-8 --------
# generatory service instance
# 动态导入模块，并生成服务实例
import importlib
import re

class ServInstance_Factory(object):
	instance = None
	def __init(self, param):
		pass
	
		# 通过__call__实现singleton
	def __call__(self, *args, **kw):
		if self.instance is None:
			self.instance = super(object, self).__call__(*args, **kw)
		return self.instance
	
	
	def gen_serviceInstance(self, classPath, method, attrType):
		
		def wraper(func):
			def func_ext(*args, **kw):
				return func.__call__(*args, **kw)
			return func_ext
		
		module = None
		if method is None or method == "":
			raise Exception("the module is empty")
		else:
			__class = None
			if attrType == 1:
				__class = re.sub(r'^.*?\.(.*)$', "\\1", classPath)
				classPath = re.sub(r'^(.*?)\.[^\\.]+$', "\\1", classPath)
			module = re.sub(r'^.*?\.(.*)$', "\\1", classPath)
			subPackage = re.sub(r'^(.*?)\.[^\\.]+$', "\\1", classPath)
		__module = importlib.import_module(module, subPackage)
		if attrType == 1:
			func = getattr(getattr(__module, __class)(), method)
			return wraper(func)
		if attrType == 0:
			func = getattr(__module, method)
			return wraper(func)

		
		
		
