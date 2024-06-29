from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

class API:

	def __init__(self, getter:object=None):
		self._get = getter # TODO

	def _validate_auth(self, data:dict) -> bool:
		try:
			data['login'], data['password']
		except:
			return False
		return True

	@csrf_exempt
	def auth(self, request) -> HttpResponse:
		if request.method != 'POST':
			return HttpResponse('ERROR')
		#print(request.POST.get('login'), request.POST.get('password '))
		if self._validate_auth(request.POST):
			return HttpResponse('{"response": true}') # TODO
		else:
			return HttpResponse('{"error": "No data"}')