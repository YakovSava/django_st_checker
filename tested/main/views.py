from django.shortcuts import render
from nondjmodules.contexter import Contexter

class MAIN:

	def __init__(self, con:Contexter=Contexter()):
		self._con = con

	def admin(self, request):
		return render(request, 'panel.html', context=self._con.admin())

	def worker(self, request):
		return render(request, 'panel.html', context=self._con.worker())

	def questions(self, request):
		return render(request, 'quest.html')