# ----*---- coding:utf-8 -------*----
'''
 author: alec
 create: 2014/06/19
'''
#from django.conf import settings
from types import FunctionType


import importlib
import re

import sqlite3

database_configs = None

tmpDict={"DATABASES":"G://django_serv/mysite/mysite.db","DATABASES_UTILS":"mydiary.core.testMeta.dbUtils_sqlite_Impl"}

def getattr_settings(attrName):
    return tmpDict[attrName]

   

class db_meta(type):
    actionProxy = None
    
    @classmethod
    def setActionProxy(cls, operator):
        print("set action proxy ...")
        cls.actionProxy = operator
        print(cls.actionProxy)
    
    def __new__(cls, name, bases, mdict):
        def wrapper(functName, funct):
            def proxy(*args, **kw):
                if hasattr(cls.actionProxy, functName):
                    print("args: ",args[0],"kw: ",kw)
                    args=args[1:]
                    return getattr(cls.actionProxy, functName)(*args, **kw)
                else:
                    return funct(*args, **kw)
            return proxy
        
        for key, item in mdict.items():
            if isinstance(item, FunctionType):
                print("item : " + key)
                mdict[key] = wrapper(key, item)
        return super(db_meta, cls).__new__(cls,name, bases, mdict)
    
class dbUtils(metaclass=db_meta):
    def __init__(self,*args,**kw):
        pass
    
    def getConnection(self):
        pass
    
    def getCursor(self,conn,isRowFactory):
        pass

    def relaseConnction(self, conn):
        pass
    
class dbUtils_sqlite_Impl(object):
    def __init__(self,*args,**kw):
        print("dbUtils sqlite implemention ")
    
    def getConnection(self):
        print("sqlite3 get connection with python ")

    def getCursor(self,conn,isRowFactory):
        print("get cursor with sqlite3")

    def releaseConnection(self, conn):
        print("release connection with sqlite3")

class dbUtilsFactory(object):
    
    instance = None

    def __init(self):
        print("__init dbUtilsFactory")

    def __init__instance(self):
        self.dbUtils_Instance = dict()
        global database_configs
        database_configs = getattr_settings("DATABASES")
        dbUtilsInstance = getattr_settings("DATABASES_UTILS")
        print("database utils instance path: ",dbUtilsInstance)
        if isinstance(dbUtilsInstance, str):
            subPackage = re.sub(r'^(.*)\.\w+$', "\\1", dbUtilsInstance)
            fromList=re.sub(r'^(.*)\.\w+$', "\\1", subPackage)
            module = re.sub(r'^.*\.(\w+)$', "\\1", subPackage)
            implemention=re.sub(r'^.*\.(\w+)$', "\\1", dbUtilsInstance)
            
            print("subPackage: {0} >> module: {1} ".format(subPackage, module))
            import_module = __import__(module,fromlist=[fromList])
            db_meta.setActionProxy(getattr(import_module,implemention)())
        else:
            db_meta.setActionProxy(dbUtilsInstance)

    @classmethod
    def __new__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(dbUtilsFactory, cls).__new__(*args, **kw)
            cls.instance.__init__instance()
        return dbUtilsFactory.instance        
    
    def getDbUtils_Instance(self, key):
        if key is None:
            key = "default"
        if not self.dbUtils_Instance.__contains__(key):
            self.dbUtils_Instance[key] = dbUtils()
        return self.dbUtils_Instance[key]

if __name__ == '__main__':
    print(getattr_settings("DATABASES_UTILS"))
    dbUtilsFactory_instance=dbUtilsFactory()
    dbtools=dbUtilsFactory_instance.getDbUtils_Instance(None)
    dbtools.getConnection()
   
    __import__("testDynamicModule",fromlist=["mydiary.busi"],globals=globals())
    from mydiary.busi import testDynamicModule