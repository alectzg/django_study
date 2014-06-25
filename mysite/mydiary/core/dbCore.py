# ----*---- coding:utf-8 -------*----
'''
 author: alec
 create: 2014/06/19
'''
# from django.conf import settings
from types import FunctionType
from mydiary.core.loadStatic import getattr_settings

import re

import sqlite3

database_configs = None

   

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
                    print("args: ", args[0], "kw: ", kw)
                    args = args[1:]
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
    def __init__(self, *args, **kw):
        pass
    
    def getConnection(self):
        pass
    
    def getCursor(self, conn, isRowFactory):
        pass

    def relaseConnction(self, conn):
        pass
    
class dbUtils_sqlite_Impl(object):
    def __init__(self, *args, **kw):
        # print("dbUtils sqlite implemention ")
        global database_configs
        sqlite_config = database_configs["default"]
        self.database.file = sqlite_config["NAME"]
    
    def getConnection(self):
        # print("sqlite3 get connection with python ")
        
        conn = sqlite3.connect(self.database.file)
        return conn

    def getCursor(self, conn, isRowFactory):
        cursor = conn.cursor()
        if isRowFactory:
            cursor.row_factory = sqlite3.Row
        return cursor

    def releaseConnection(self, conn):
        # print("release connection")
        conn.close()

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
            fromList = re.sub(r'^(.*)\.\w+$', "\\1", subPackage)
            module = re.sub(r'^.*\.(\w+)$', "\\1", subPackage)
            implemention = re.sub(r'^.*\.(\w+)$', "\\1", dbUtilsInstance)
            
            print("subPackage: {0} >> module: {1} ".format(subPackage, module))
            import_module = __import__(module, fromlist=[fromList])
            db_meta.setActionProxy(getattr(import_module, implemention)())
        else:
            db_meta.setActionProxy(dbUtilsInstance)

    @classmethod
    def __new__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(dbUtilsFactory, cls).__new__(*args, **kw)
            cls.instance.__init_instance()
        return dbUtilsFactory.instance		
    
    def getDbUtils_Instance(self, key):
        if key is None:
            key = "default"
        if not self.dbUtils_Instance.__contains__(key):
            self.dbUtils_Instance[key] = dbUtils()
        return self.dbUtils_Instance[key]
