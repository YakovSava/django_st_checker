from os import mkdir, rmdir, remove, listdir
from os.path import exists
from urllib.parse import unquote
from json import dumps, loads
from shutil import copy
from django.http import HttpResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Users
from api.models import Company
from autorization.models import Company as CompanyData
from nondjmodules.quest_validator import Validator
from nondjmodules.former import Document
from nondjmodules.zipper import zip_path
from nondjmodules.getter import Getter, MIME

def json_resp(dictionary:dict) -> str:
	return HttpResponse(dumps(dictionary))

class API:

	def __init__(self, database:Users=Users, getter:Getter=Getter()):
		self._db = database
		self._get = getter
		if not exists('tmp/'):
			mkdir('tmp/')

	def _validate_auth(self, data:dict) -> bool:
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

	def _create_company(self, company_name:str, company_admin:str) -> list:
		_tmp = CompanyData.objects.values('company_name').distinct()
		if company_name not in map(lambda x: x['company_name'], _tmp):
			if len(list(map(lambda x: x['company_name'], _tmp))) == 3:
				return [False, 'Нельзя зарегестрировать более 3-ёх компаний']
			new_company = CompanyData(
				company_name=company_name,
				company_admin=company_admin,
				is_super_admin=False,
			)
			new_company.save()
			return [True]
		return [True]

	def _to_db(self, data:list, session:str) -> None:
		new_rec = Company(
			fcs=data[0],
			date=data[1],
			company_name=data[2],
			fcs_commissions1=data[3],
			commisions_status1=data[4],
			fcs_commissions2=data[5],
			commisions_status2=data[6],
			fcs_commissions3=data[7],
			commisions_status3=data[8],
			responsible_electrical_safety=data[9],
			reason_for_check=data[10],
			antifire_reason=data[11],
			status=data[12],
			number_of_driver_program=data[13],
			electrical_safety_group=data[14],
			work_exp=data[15],
			session=session
		)
		new_rec.save()

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
			self._to_db(validator_object.return_data(), answer_for_db['session'])
			rsult = self._create_company(answer_for_db['company'], answer_for_db['session'])
			if not rsult[0]:
				return json_resp({'result': False, 'error': rsult[1]})
			new_company = self._db(
				name=answer_for_db['name'],
				company=answer_for_db['company'],
				session=answer_for_db['session'],
				login=answer_for_db['login'],
				password=answer_for_db['password']
			)
			new_company.save()
			return json_resp({'result': True})
		else:
			return json_resp({'result': False, 'error': validator_object.where()})

	@csrf_exempt
	def get_doc(self, request):
		if request.GET['session']:
			_tmp = CompanyData.objects.filter(company_admin=request.GET['session'])
			if len(_tmp) == 1:
				# if _tmp[0].is_super_admin:
				# 	return json_resp({'result': True, 'link': f'/files/nonworker?file={doc.get("./templates/all.docx")}'})
				_tmp = Company.objects.filter(company_name=_tmp[0].company_name)
				try:
					mkdir('tmp/'+_tmp[0].company_name)
				except:
					pass
				for worker in _tmp:
					copy("./templates/all.docx", f"./tmp/{_tmp[0].company_name}/all.docx")
					doc = Document(worker.session)
					print(f"./tmp/{worker.company_name}/all.docx")
					doc.get(f"./tmp/{worker.company_name}/all.docx")
				return json_resp({'result': True, 'link': f'/files/worker?file={zip_path('tmp/'+_tmp[0].company_name)}'})
			else:
				doc = Document(request.GET['session'])
				try:
					copy("./templates/all.docx", "./tmp/all.docx")
				except:
					pass
				return json_resp({'result': True, 'link': f'/files/worker?file={doc.get("./tmp/all.docx")}'})
		else:
			return json_resp({'result': False})

	@csrf_exempt
	def ret_doc(self, request):
		if request.GET['file']:
			file = HttpResponse(self._get.get(request.GET['file']), content_type=eval(f'MIME.{request.GET["file"].split(".")[-1]}'))
			try:
				remove(request.GET['file'])
			except:
				pass
			if exists(request.GET['file'].split('.')[0]):
				rmdir(request.GET['file'].split('.')[0])
			return file
		else:
			return HttpResponse('Error')