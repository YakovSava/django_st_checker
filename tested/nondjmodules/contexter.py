from main.models import Users

class Contexter:
	ADMIN_BUTTONS = '''<div class="buttons">
			<button class="btn">Добавить отчёт</button>
			<button class="btn">Дать доступ</button>
			<button class="btn">Удалить компанию</button>
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

	def worker(self):
		raise NotImplemented