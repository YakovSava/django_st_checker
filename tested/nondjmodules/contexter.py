from main.models import Users

class Contexter:
	SUPER_ADMIN_BUTTONS = '''<div class="buttons">
			<button class="btn" onclick="adminDownload().then();">Скачать отчёт</button>
			<button class="btn" onclick="toQuest();">Пройти опросник</button>
			<button class="btn" onclick="removeCompany();">Удалить компанию</button>
		</div>'''
	ADMIN_BUTTONS = '''<div class="buttons">
			<button class="btn" onclick="downloadAllCompany().then();">Скачать все документы</button>
			<button class="btn" onclick="toQuest();">Пройти опросник</button>
		</div>'''
	WORKER_BUTTONS = '''<div class="buttons">
			<button class="btn" onclick="downloadDocument().then();">Скачать документ</button>
		</div>'''


	def __init__(self, database:Users=Users):
		self._db = database

	def super_admin(self):
		all_companys = self._db.objects.values('company').distinct()
		return {
			"status": "Главный админ",
			"buttons": self.SUPER_ADMIN_BUTTONS,
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

	def admin(self, session:str):
		admin_data = self._db.objects.filter(session=session)[0]
		return {
			"status": f"Админ компании {admin_data.company}",
			"buttons": self.ADMIN_BUTTONS,
			"company_list": [
				{
					"name": admin_data.company,
					"workers": [{
							"name": worker.name,
							"login": worker.login,
							"password": worker.password
						} for worker in self._db.objects.filter(company=admin_data.company)
					]
				}
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