from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render

# Create your views here.
def index(request):
	return HttpResponse('Запрос к авторизации!')

def redirect(request):
	return HttpResponsePermanentRedirect('autorize')
