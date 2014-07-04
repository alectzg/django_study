# ----*---- coding:utf-8 -------*----
'''
 author: alec
 create: 2014/06/19
'''
# from django.conf import settings
from types import FunctionType
from mydiary.core.loadStatic import getattr_settings
from mydiary.core import loadStatic

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
    class pojo(object):
        def __init__(self):
            self.file=None
    database=pojo()
    def __init__(self, *args, **kw):
        # print("dbUtils sqlite implemention ")
        global database_configs
        if database_configs is None:
            database_configs = getattr_settings("DATABASES")
           
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
        dbUtilsInstance = getattr_settings("DATABASES_UTILS")
        print("database utils instance path: ",dbUtilsInstance)
        if isinstance(dbUtilsInstance, str):
            subPackage = re.sub(r'^(.*)\.\w+$', "\\1", dbUtilsInstance)
            fromList=re.sub(r'^(.*)\.\w+$', "\\1", subPackage)
            module = re.sub(r'^.*\.(\w+)$', "\\1", subPackage)
            implemention=re.sub(r'^.*\.(\w+)$', "\\1", dbUtilsInstance)
            
            print("subPackage: {0} >> module: {1} ".format(subPackage, module))
            loadStatic.__append__(fromList)
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
        DBId=None
        if key is None:
            DBId = "default"
        else:
            DBId=key
        if not self.dbUtils_Instance.__contains__(DBId):
            self.dbUtils_Instance[DBId] = dbUtils()
        return self.dbUtils_Instance[DBId]


if __name__=="__main__":
    print(loadStatic.APP_BASE_DIR)