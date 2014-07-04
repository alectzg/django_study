#-----*---- coding=utf-8 -----*------
from django.http import HttpRequest
from mydiary.webUtils.ServiceFactory import ServInstance_Factory
from mydiary.webUtils.ajaxParser import *
from mydiary.models import service, serv_ext
from mydiary.logger.Pylogger import Pylogger

ServInstanceObj = None

mlogger = Pylogger()

def dealRequest(req):
	request_json = req.REQUEST.get("__post_ajax", "")
	
	'''
	varAjaxJson=req.POST.get("__post_ajax");
	mlogger.info(varAjaxJson);
	'''
	for key in req.POST:
		mlogger.info("parameter {0} >> value {1} ".format(key, req.POST.getlist(key)))
	#return '{"request_json":\'%s\'}' % (request_json)

	serviceName, requestParam = parseAjaxRequest(True, request_json)
	mlogger.info("serviceName: {0} ,parameter :{1} ".format(serviceName,requestParam))
	if serviceName is None or serviceName == "":
		return None
	else:
		serviceObj = service.objects.filter(service_name=serviceName)
		if len(serviceObj) > 0:
			module = serviceObj[0].module
			attrType = serviceObj[0].attrType
			method = serviceObj[0].method
			global ServInstanceObj
			if ServInstanceObj is None:
				ServInstanceObj = ServInstance_Factory()
			busiFunc = ServInstanceObj.gen_serviceInstance(module, method, attrType)
			try:
				
				busiFunc(requestParam)
				requestParam["serviceName"] = serviceName
				return encodeAjaxResponse(requestParam)
			except Exception as err:
				return encodeAjaxResponse({"serivceName":serviceName, "data":{"status":"fail", "error_msg":str(err)}})
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
		
	
