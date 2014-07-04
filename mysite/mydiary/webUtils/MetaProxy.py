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
    def setBeforeOp(cls,funct):
        cls.doBeforeOp = funct
    
    @classmethod
    def setAfterOp(cls,funct):
        cls.doAfterOp = funct
        
    @classmethod 
    def define_transcation(cls,funct):
        cls.setTransaction = funct
    
    #@classmethod
    def __new__(cls, name, bases, mdict):
        print("cls: ",cls," >> name: ",name)
        def doAop(funct):
            obj = object()
            def wrapper(*args, **kw):
                cls.doBeforeOp(obj, *args, **kw)
                print("do some thing before")
                retValue = funct(*args, **kw)
                cls.doAfterOp(obj, *args, **kw)
                return retValue
            return wrapper
        
        for key, attrVal in mdict.items():
            print("key: ",key)
            if key == "toDo":
                attrVal = mdict[key]
                mdict[key] = doAop(attrVal)
        mdict["setConnection"] = MetaServInstance.setTransaction
        return super(MetaServInstance, cls).__new__(cls, name, bases, mdict)

def doBusiBefore(self,*args,**kw):
	print("begin Translateion")

def doBusiAfter(self,*args,**kw):
	print("commit Translation!")

MetaServInstance.setBeforeOp(doBusiBefore)
MetaServInstance.setAfterOp(doBusiAfter)

if __name__=="__main__":
    class A(metaclass=MetaServInstance):
        def __init__(self):
            print("init A")
            
        def display(self):
            print("lemei");
            return self
            
        def toDo(self):
            print("滚")
            return self
    A().display().toDo().setConnection()
