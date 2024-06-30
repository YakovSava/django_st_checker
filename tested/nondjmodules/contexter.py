# import database

class Contexter:
	ADMIN_BUTTONS = '''<div class="buttons">
			<button class="btn">Добавить отчёт</button>
			<button class="btn">Дать доступ</button>
			<button class="btn">Удалить компанию</button>
		</div>'''

	def __init__(self, database:object=None):
		self._db = database # TODO

	def admin(self):
		return {
			"status": "Админ",
			"buttons": self.ADMIN_BUTTONS,
			"company_list": [
				{
					"name": "Олегов О.О.",
					"workers": [
						{
							"name": "Олегов Олег",
							"login": "oleg1",
							"password": "OgoOleg"
						},
						{
							"name": "Иванов Иван",
							"login": "ivan1",
							"password": "ai"
						}
					]
				},
				{
					"name": "ООО \"Лег\"",
					"workers": [
						{
							"name": "Олегов Олег",
							"login": "oleg1",
							"password": "OgoOleg"
						},
						{
							"name": "Иванов Иван",
							"login": "ivan1",
							"password": "ai"
						}
					]
				}
			]
		}

	def worker(self):
		raise NotImplemented