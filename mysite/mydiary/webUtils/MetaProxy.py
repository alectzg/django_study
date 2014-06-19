#-------- coding=utf-8 --------
'''
Created on 2014年6月17日

@author: alexbeta
'''

class MetaServInstance(type):
    @classmethod
    def nonOp(self, *args, **kw):
        pass
    
    doBeforeOp = nonOp
    doAfterOp = nonOp
    setTransaction = nonOp
    
    @classmethod
    def setBeforeOp(funct):
        doBeforeOp = funct
    
    @classmethod
    def setAfterOp(funct):
        doAfterOp = funct
        
    @classmethod 
    def define_transcation(funct):
        setTransaction = funct
    
    @classmethod
    def __new__(cls, name, bases, mdict):
        
        def doAop(funct):
            obj = object()
            def wrapper(*args, **kw):
                MetaServInstance.doBeforeOp(obj, *args, **kw)
                retValue = funct(*args, **kw)
                MetaServInstance.doAfterOp(obj, *args, **kw)
                return retValue
            return wrapper
        
        for key, attrVal in mdict.items():
            if key == "toDo":
                attrVal = mdict[key]
                mdict[key] = doAop(attrVal)
            mdict["setConnection"] = MetaServInstance.setTransaction
            return super(MetaServInstance, cls).__new__(cls, name, bases, mdict)

def doBusiBefore():
	print("begin Translateion")

def doBusiAfter():
	print("commit Translation!")

MetaServInstance.setBeforeOp(doBusiBefore)
MetaServInstance.setAfterOp(doBusiAfter)
