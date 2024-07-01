from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render

def index(request):
	return render(request, "auth.html")

def redirect(request):
	return HttpResponsePermanentRedirect('autorization/')
