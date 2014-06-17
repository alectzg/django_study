# --- * --- coding=Utf-8 -----*--
'''
Created on 2014年6月16日

@author: alexbeta
'''
from ModuleCore.ServiceFactory import *
import importlib
import os

class O(object):
    def __init__(self):
        self.attr="hello Johns"
        print("initialize the instance")
    
    @classmethod
    def __new__(cls, *args, **kw):
        print("create class o instance [ ", cls , " ]")
        print("super: ", super(O, cls))
        return super(O, cls).__new__(cls, *args, **kw)
    
    def __call__(self, *args, **kw):
        print("call the object instance as function ")

if __name__ == '__main__':
     # print(type(AopFactory))
     print(type(O))
     print(isinstance(ServInstance_Factory, type))
     # print(isinstance(AopFactory,module))
     module_file="ModuleCore.testModule.py"
     module_name, ext = os.path.splitext(os.path.basename("ModuleCore.testModule.py"))  # 将文件名以点号分开  
     print(os.path.basename(module_file))  
     print(ext)  
     module = __import__(module_name)
     print(module)
     __module = __import__("ModuleCore.testModule")
     print(__module)
     
     __module= importlib.import_module("testModule", "ModuleCore")
     
     #print(testModule)
     func = getattr(__module, "doTest")
     func.__call__(O())
     
     #__module=importlib.import_module("proxy", "ModuleCore.testModule")
     print(getattr(__module,"proxy")())
     getattr(getattr(__module,"proxy")(),"display")()
    
