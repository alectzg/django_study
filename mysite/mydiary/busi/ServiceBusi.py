# ----*---- coding:utf-8 ------*-------
from mydiary.models import service
from mydiary.webUtils.MetaProxy import MetaServInstance
from mydiary.core.dbCore import dbUtilsFactory


class serviceManager(object,metaclass=MetaServInstance):
	def __init__(self):
		pass
	
	def addContact(self,paramDict):
		print("customer wonna add service record" ,paramDict["serviceName"])
		#retDict={"operation_status":"success"}
		paramDict["operation_status"]="success"
	
	def Contact_Operation(self,paramDict):
		if not hasattr(paramDict,"serviceName"):
			raise Exception("serviceName is not exists in request parameters!")
		serviceName=paramDict["serviceName"]
		if serviceName=="queryContact":
			self.queryContact(paramDict)
		else
			pass
	
	def queryContact(self,reqDict):
		dbTools=dbUtilsFactory()
		connTools=dbTools.getDbUtils_Instance(None)
		conn=connTools.getConnection()
		cursor=connTools.getCursor(conn,True)
		cursor.execute("select * from mydiary_telephone_contact");
		resultRows=cursor.fetchall()
	    resultList=[]
		recordItem=None
		for rowItem in resultRows:
			recordItem={}
			for key in rowItem.keys():
				recordItem[key]=rowItem[key]
			resultList.add(recordItem)
		if len(resultList)==1:
			reqDict["data"]=resultList[0]
		else if len(resultList)>1 :
			reqDict["data"]=resultList
		else:
			pass