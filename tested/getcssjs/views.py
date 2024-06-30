from os import getcwd
from django.http import HttpResponse
from nondjmodules.getter import Binder
from nondjmodules.typ import typer

class GET:

	def __init__(self, getter:Binder=Binder()):
		self._get = getter

	def getfile(self, request, site_path:str) -> str:
		return HttpResponse(self._get.read(getcwd()+'/html/'+site_path), content_type=typer(site_path))