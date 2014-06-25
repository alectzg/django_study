# -*- encoding=utf-8 -*-
'''
Created on 2014-6-30

@author: cs0027004059

purpose: 

'''
class A(object):
    def __init__(self):
        self.user="alec"
    
    def display(self):
        print("haha, could you feel my world ?");
        
if __name__ == '__main__':
    import_module=__import__("testMeta",globals(),locals(),fromlist=["mydiary.core"],level=-1)
    dbtools=getattr(import_module,"dbUtils_sqlite_Impl")()
    ab=A()
    getattr(ab, "display")()