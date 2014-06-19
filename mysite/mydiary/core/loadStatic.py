from django.conf import settings

def getattr_settings(attrName):
	return getattr(settings,attrName,"")


