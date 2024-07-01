from urllib.parse import unquote
from json import dumps
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Users
from nondjmodules.quest_validator import Validator

def json_resp(dictionary:dict) -> str:
	return HttpResponse(dumps(dictionary))

class API:

	def __init__(self, database:Users=Users):
		self._db = database

	def _validate_auth(self, data:dict) -> bool:
		try:
			data['login'], data['password']
		except:
			return False
		return True

	def _to_normal(self, string:str) -> str:
		return eval('["'+unquote(string).replace(',', '","')+'"]')

	@csrf_exempt
	def auth(self, request) -> HttpResponse:
		if request.method != 'POST':
			return HttpResponse('ERROR')
		#print(request.POST.get('login'), request.POST.get('password '))
		if self._validate_auth(request.POST):
			return HttpResponse('{"response": true}') # TODO
		else:
			return HttpResponse('{"error": "No data"}')

	@csrf_exempt
	def result(self, request) -> HttpResponse:
		if request.method != 'GET':
			return HttpResponse('ERROR')
		validator_object = Validator(self._to_normal(request.GET['data']))
		if all(validator_object.validate()):
			answer_for_db = validator_object.for_db()
			new_company = self._db(
				name=answer_for_db['name'],
				company=answer_for_db['company'],
				session=answer_for_db['session'],
				is_admin=answer_for_db['is_admin'],
				login=answer_for_db['login'],
				password=answer_for_db['password']
			)
			new_company.save()
			return json_resp({'result': True})
		else:
			return json_resp({'result': False, 'error': validator_object.where()})