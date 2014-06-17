from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from mydiary.models import *

def index(req):
	var_welcome="could you feel my world ? welcome to mydiary"
	return HttpResponse("<h1>"+var_welcome+"</h1>")

def showService(req,serviceName):
	resultObj=service.ojbects.get(service_name=serviceName)	
	responseStr=None
	if resultObj is None:
		responseStr="service instance is not exist!! "
	else
		responseStr=resultObj["service"]
	return HttpResponse('<p style="color:red" >'+responseStr+'</p>')
