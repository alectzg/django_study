from django.shortcuts import render,render_to_response
from django.http import HttpResponse

def index(req):
	var_welcome="could you feel my world ? welcome to mydiary"
	return HttpResponse("<h1>"+var_welcome+"</h1>")
