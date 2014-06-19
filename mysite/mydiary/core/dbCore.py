# ----*---- coding:utf-8 -------*----
'''
 author: alec
 create: 2014/06/19
'''
from django.conf import settings
from types import FunctionType
from mydiary.core.loadStatic import getattr_settings

import importlib
import re

database_configs = None

   

class db_meta(type):
    actionProxy = None
    
    @classmethod
    def setActionProxy(cls, operator):
        print("set action proxy ...")
        cls.actionProxy = operator
        print(cls.actionProxy)
    
    '''
    def __new__(cls, name, bases, mdict):
        def wrapper(functName, funct):
            print(cls)
            print(cls.actionProxy)
            if hasattr(cls.actionProxy, functName):
                return getattr(cls.actionProxy, functName)
            else:
                return funct
        for key, item in mdict.items():
            if isinstance(item,FunctionType):
                print("item : "+key)
                mdict[key] = wrapper(key, item)
        return super(db_meta, cls).__new__(cls,name, bases, mdict)
    '''
    def __new__(cls, name, bases, mdict):
        
        def wrapper(functName, funct):
            def proxy(*args, **kw):
                if hasattr(cls.actionProxy, functName):
                    return getattr(cls.actionProxy, functName)(*args, **kw)
                else:
                    return funct(*args, **kw)
            return proxy
        
        for key, item in mdict.items():
            if isinstance(item, FunctionType):
                print("item : " + key)
                mdict[key] = wrapper(key, item)
        return super(db_meta, cls).__new__(cls, name, bases, mdict)
    
class dbUtils(metaclass=db_meta):
    def __init__(self):
        pass
    
    def getConnection(self):
        pass

    def relaseConnction(self, conn):
        pass

class dbUtils_sqlite_Impl(object):
    def __init__(self):
        print("dbUtils sqlite implemention ")
    
    def getConnection(self):
        print("sqlite3 get connection with python ")
    
    def releaseConnection(self, conn):
        print("release connection")

class dbUtilsFactory(object):
    
    instance = None

    def __init(self):
        print("__init dbUtilsFactory")

    def __init__instance(self):
        self.dbUtils_Instance = dict()
        global database_configs
        database_configs = getattr_settings("DATABASES")
        dbUtilsInstance = getattr_settings("DATABASES_UTILS")
        if isinstance(dbUtilsInstance, str):
            subPackage = re.sub(r'^(.*)\.\w+$', "\\1", dbUtilsInstance)
            module = re.sub(r'^.*\.(\w+)$', "\\1", dbUtilsInstance)
            import_module = importlib.import_module(module, subPackage)
            db_meta.setActionProxy(import_module)
        else:
            db_meta.setActionProxy(dbUtilsInstance)

    @classmethod
    def __new__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(dbUtilsFactory, cls).__new__(*args, **kw)
        return dbUtilsFactory.instance		
	
	def getDbUtils_Instance(self, key):
		if key is None:
			key = "default"
		if not self.dbUtils_Instance.__contains__(key):
			self.dbUtils_Instance[key] = dbUtils()
		return self.dbUtils_Instance[key]
