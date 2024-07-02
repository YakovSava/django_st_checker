from urllib.parse import unquote
from json import dumps, loads
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
		print(data)
		try:
			data['login'], data['passwd']
		except:
			return {
				'result': False,
				'reason': 'Внутреняя ошибка!'
			}
		user = self._db.objects.filter(login=data['login'])
		if len(user) == 1:
			if data['passwd'] == user[0].password:
				return {
					'result': True,
					'session': user[0].session
				}
			else:
				return {
					'result': False,
					'reason': 'Неверный пароль'
				}
		else:
			return {
				'result': False,
				'reason': 'Неверный логин'
			}

	def _to_normal(self, string:str) -> str:
		return eval('["'+unquote(string).replace(',', '","')+'"]')

	def _to_normal_json(self, data) -> dict:
		return loads(unquote(data['data']))

	@csrf_exempt
	def auth(self, request) -> HttpResponse:
		if request.method != 'GET':
			return HttpResponse('ERROR')
		validates = self._validate_auth(self._to_normal_json(request.GET))
		if validates['result']:
			return json_resp({'result': True, 'session': validates['session']})
		else:
			return json_resp({'result': False, 'reason': validates['reason']})

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