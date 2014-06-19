# ----*---- coding:utf-8 ------*-------
from mydiary.models import service
from mydiary.webUtils.MetaProxy import MetaServInstance



class serviceManager(object,metaclass=MetaServInstance):
	def __init__(self):
		pass
	
	def addContact(self,paramDict):
		print("customer wonna add service record" ,paramDict["serviceName"])
		#retDict={"operation_status":"success"}
		paramDict["operation_status"]="success"
	
	