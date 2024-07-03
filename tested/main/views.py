from django.shortcuts import render
from main.models import Users
from api.models import Company
from autorization.models import Company as CompanyData
from nondjmodules.contexter import Contexter

class MAIN:

	def __init__(self, con:Contexter=Contexter()):
		self._con = con

	def admin(self, request):
		return render(request, 'panel.html', context=self._con.admin(request.GET['session']))

	def worker(self, request):
		return render(request, 'panel.html', context=self._con.worker(request.GET['session']))
	
	def superadmin(self, request):
		return render(request, 'panel.html', context=self._con.super_admin())

	def questions(self, request):
		return render(request, 'quest.html')

	def universal(self, request):
		_tmp = CompanyData.objects.filter(company_admin=request.GET['session'])
		if len(_tmp) == 1:
			if _tmp[0].is_super_admin:
				return self.super_admin(request)
			return self.admin(request)
		else:
			return self.worker(request)
		