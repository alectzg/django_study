import json
import re

def parseAjaxRequest(isJson,paramater):
	if isJson:
		paramater=re.sub(r'\'','"',paramater)
		paramObj=json.loads(paramater)
		return (paramObj["serviceName"],paramObj)
	else:
		return paramater

def encodeAjaxResponse(responseDict):
	if isinstance(responseDict,dict):
		return json.dumps(responseDict)


'''		
reponse_dict={}

reponse_dict["serviceName"]="call_service"
dataDict={}
dataDict["user"]="alec"
dataDict["age"]=20
dataDict["language"]=["java","python",{"key":"value"}]
reponse_dict["data"]=dataDict

jsonResponse=encodeAjaxResponse(reponse_dict);

print("reponse:",jsonResponse)
'''