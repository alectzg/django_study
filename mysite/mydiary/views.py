from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from mydiary.models import service,serv_ext

def index(req):
	var_welcome="could you feel my world ? welcome to mydiary"
	return HttpResponse("<h1>"+var_welcome+"</h1>")


def showService(req,serviceName):
	resultObj=service.objects.filter(service_name=serviceName)
	responseStr=None
	if resultObj is None or len(resultObj)<=0:
		responseStr="service instance is not exist!! "
	else:
		responseStr=resultObj[0].service_name
	return HttpResponse('<p style="color:red" >'+responseStr+'</p>')
