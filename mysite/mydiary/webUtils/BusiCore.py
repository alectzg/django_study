#-----*---- coding=utf-8 -----*------
from django.http import HttpRequest
from mydiary.webUtils.ServiceFactory import ServInstance_Factory
from mydiary.webUtils.ajaxParser import *
from mydiary.models import service,serv_ext

ServInstanceObj=None

def dealRequest(req):
	request_json=req["__post_ajax"]
	#return '{"request_json":\'{0}\'}'.format(request_json)

	serviceName,requestParam=parseAjaxRequest(True,request_json)
	if serviceName is None or serviceName == "":
		return null
	else:
		serviceObj=service.objects.filter(service_name=serviceName)
		if len(serviceObj)>0:
			module=serviceObj.module
			attrType=serviceObj.attrType
			method=serviceObj.method
			if ServInstanceObj is None:
				ServInstanceObj=ServInstance_Factory()
			busiFunc=ServInstanceObj.gen_serviceInstance(module,method,attrType)
			try:
				busiFunc(requestParam)
				requestParam["serviceName"]=serviceName
				return encodeAjaxResponse(requestParam)
			except err as Exception:
				return encodeAjaxResponse({"serivceName":serviceName,data:{"status":"fail","error_msg":str(err)}})
			return requestParam
		else:
			raise Exception("sorry,service [{1}] is not exist!".format(serviceName))
	
'''
def queryService_Define(serviceName):
	record=service.object.filter(service_name=ServiceName)
	if record is None:
		return None
	else:
'''		
		
	
