from django.conf import settings
import sys
import os.path
import re

def getattr_settings(attrName):
	return getattr(settings,attrName,"")


APP_BASE_DIR = getattr_settings("BASE_DIR")


def __append__(corePath):
			newPath = sys.path
			searchPath = os.path.join(APP_BASE_DIR, re.sub(r'\.', '/', corePath))
			print("search path: ",searchPath)
			appendFlag = True
			for item in newPath:
				if item == searchPath:
					appendFlag = False
			if appendFlag:
				sys.path.append(searchPath)
