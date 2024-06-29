from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, "auth.html")

def redirect(request):
	return HttpResponsePermanentRedirect('autorize')
