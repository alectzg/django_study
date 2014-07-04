# ----*---- coding:utf-8 ------*-------

from mydiary.webUtils.MetaProxy import MetaServInstance
from mydiary.core.dbCore import dbUtilsFactory
from mydiary.logger.Pylogger import Pylogger 

mlogger = Pylogger()

class serviceManager(object, metaclass=MetaServInstance):
	def __init__(self):
		pass
	
	def addContact(self, paramDict):
		print("customer wonna add service record" , paramDict["serviceName"])
		# retDict={"operation_status":"success"}
		paramDict["operation_status"] = "success"
	
	def Contact_Operation(self, paramDict):
		for key in paramDict.keys():
			mlogger.info("key: "+key)
		if not paramDict.__contains__("serviceName"):
			raise Exception("serviceName is not exists in request parameters!")
		serviceName = paramDict["serviceName"]
		mlogger.info("serviceName: "+serviceName)
		if serviceName == "Query_Contact_List":
			self.queryContact(paramDict)
		else:
			pass
	
	def queryContact(self, reqDict):
		dbTools = dbUtilsFactory()
		connTools = dbTools.getDbUtils_Instance(None)
		conn = connTools.getConnection()
		cursor = connTools.getCursor(conn, True)
		cursor.execute("select * from mydiary_telephone_contact");
		resultRows = cursor.fetchall()
		resultList = []
		recordItem = None
		for rowItem in resultRows:
			recordItem = {}
			for key in rowItem.keys():
				recordItem[key] = rowItem[key]
			resultList.append(recordItem)
		if len(resultList) == 1:
			reqDict["data"] = resultList[0]
		elif len(resultList) > 1 :
			reqDict["data"] = resultList
		else:
			pass
