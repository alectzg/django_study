from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponse
from mydiary.models import service,serv_ext


from mydiary.webUtils.BusiCore import dealRequest

def serviceError(error):
	pass

def do_render_404_error(req):
	return HttpResponse("<h1> page is not exists! <h1>")
	

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
	

def callAjax(req):
	if req.method=="GET":
		return do_render_404_error(req)
	if req.method=="POST":
		'''
		dataContext=dict({ "post_ajax":"haha" })
		return render(req,"corejson.html",dataContext)
		'''		
		try:
			__post_ajax=dealRequest(req)
			#__post_ajax='{"user":"alec","age":20,"language":["python","java","c/c++"]}'
			dataContext=dict({ "post_ajax":__post_ajax })
			return render(req,"corejson.html",dataContext)
		except Exception as err :
			raise err
		
def sendMsg(req):
	dataContext={"msg_subject":"FM clear Alarm notice!","msg_detail":"show me your profile production"}
	return render(req,"msg_template.html",dataContext)
	
def testAjax(req):
	dataContext={};
	return render(req,"testajax.html",{})


		

