import json

def parseAjaxRequest(isJson,paramater):
	if isJson:
		paramObj=json.loads(paramater)
		return (paramObj["serviceName"],paramObj["data"])
	else:
		return paramater

def encodeAjaxResponse(responseDict):
	if isinstance(responseDict,dict):
		return json.dumps(responseDict)


