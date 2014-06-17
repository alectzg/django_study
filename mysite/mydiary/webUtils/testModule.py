#-------- coding=utf-8 --------
'''
Created on 2014年6月17日

@author: alexbeta
'''
def doTest(self):
    print("do test for dynamic import")
    print("self",self.attr)

class proxy(object):
    def __init__(self):   
        pass
    def display(self):
        print("proxy display !!")