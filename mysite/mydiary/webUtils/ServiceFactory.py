#------ coding=utf-8 --------
#generatory service instance
#暂时不支持单方法
import importlib

class ServInstance_Factory(object):
	instance = None
	def __init__():
		pass
	
	# 利用call，实现singleton
	def __call__(self,*args,**kw):
		if self.instance is None:
			self.instance=supper(object,self).__call__(*args,**kw)
		return self.instance
	
	
	def gen_serviceInstance(self,classPath,method):
		instanceObj=None
		subModule=None
		module=None
		if method is None or method=="":
			module=classPath
		else:
			subModule=classPath
			module=method
		importlib.import_module(module,subModule)
		return eval(module+"()")


class MetaServInstance(type):
    
	@classmethod
	def nonOp(self,*args,**kw):
		pass
	
	doBeforeOp=nonOp
	doAfterOp=nonOp
	setTransaction
	
	@classmethod
	def setBeforeOp(funct):
		doBeforeOp=funct
	
	@classmethod
	def setAfterOp(funct):
		doAfterOp=funct
		
	@classmethod 
	def define_transcation(funct)
	    setTransaction=funct
	
	@classmethod
	def __new__(cls,name,bases,mdict):
		
		def doAop(funct):
			obj=new object()
			def wrapper(*args,**kw):
				MetaServInstance.doBeforeOp(obj,*args,**kw)
				retValue=funct(*args,**kw)
				MetaServInstance.doAfterOp(obj,*args,**kw)
				return retValue
			return wrapper
		
		for key,attrVal in mdict.items():
			if key == "toDo":
				attrVal=mdict[key]
				mdict[key]=doAop(attrVal)
			mdict["setConnection"]=setTransaction
			return super(MetaServInstance,self).__new__(self,name,bases,mdict)
		
		
		