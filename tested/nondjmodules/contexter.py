from main.models import Users

class Contexter:
	ADMIN_BUTTONS = '''<div class="buttons">
			<button class="btn" onclick="adminDownload().then();">Скачать отчёт</button>
			<button class="btn" onclick="toQuest();">Пройти опросник</button>
			<button class="btn" onclick="removeCompany();">Удалить компанию</button>
		</div>'''
	WORKER_BUTTONS = '''<div class="buttons">
			<button class="btn" onclick="downloadDocument().then();">Скачать документ</button>
		</div>'''


	def __init__(self, database:Users=Users):
		self._db = database

	def admin(self):
		all_companys = self._db.objects.values('company').distinct()
		return {
			"status": "Админ",
			"buttons": self.ADMIN_BUTTONS,
			"company_list": [
				{
					"name": company['company'],
					"workers": [{
							"name": worker.name,
							"login": worker.login,
							"password": worker.password
						} for worker in self._db.objects.filter(company=company['company'])
					]
				} for company in all_companys
			]
		}

	def worker(self, session:str):
		worker_data = self._db.objects.filter(session=session)[0]
		return {
			"status": worker_data.name,
			"buttons": self.WORKER_BUTTONS,
			"company_list": [
				{
					"name": worker_data.company,
					"workers": [{
							"name": worker_data.name,
							"login": worker_data.login,
							"password": worker_data.password
						}
					]
				}
			]
		}