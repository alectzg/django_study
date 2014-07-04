# ----*---- coding:utf-8 -------*----
'''
 author: alec
 create: 2014/06/19
'''
#from django.conf import settings
from types import FunctionType


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
                    return getattr(cls.actionProxy, functName)(cls.actionProxy,*args, **kw)
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
        '''
        global database_configs
        sqlite_config=database_configs["default"]
        self.database.file=sqlite_config["NAME"]
        '''
    def getConnection(self):
        print("sqlite3 get connection with python ")
        '''
        conn=sqlite3.connect(self.database.file)
        return conn
        '''
    def getCursor(self,conn,isRowFactory):
        print("get cursor for database api")
        '''
        cursor=conn.cursor()
        if isRowFactory:
            cursor.row_factory=sqlite3.Row
        return cursor
        '''
    def releaseConnection(self, conn):
        print("release connection")
        #conn.close()


if __name__ == '__main__':
    db_meta.setActionProxy(dbUtils_sqlite_Impl())
    dbutilsInstance=dbUtils()
    dbutilsInstance.getCursor()