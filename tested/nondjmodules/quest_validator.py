from time import strptime

class Validator:

	def __init__(self, answers:list[str]):
		self._q = answers

	def _validate_date(self, date:str) -> bool:
		try:
			print(date)
			strptime(date, '%d.%m.%Y')
		except:
			return False
		else:
			return True

	def _validate_name(self, name:str) -> bool:
		return all(
			[n.startswith(n.upper()[0]) for n in name.split()]
		) and (len(name.split()) == 3)

	def _validate_company(self, company_name:str) -> bool:
		if (company_name.startswith('ИП')):
			return self._validate_name(company_name.split(maxsplit=1)[-1])
		return company_name.startswith(('ООО', 'ЗАО', 'ОАО'))

	def _validate_reason(self, reason:str) -> bool:
		return reason.lower() in [
			'первичный',
			'внеплановый',
			'вводный',
			'целевой',
			'повторный'
		]

	def _validate_status(self, status:str) -> bool:
		return status.lower() in [
			'водитель',
			'машинист крана-манипулятора',
			'машинист крана автомобильного',
			'машинист  автогидроподъемника',
			'машинист экскаватора-погрузчика',
		]

	def _validate_int(self, integer:str) -> bool:
		return integer.isdigit()

	def _validate_rom_int(self, rom_int:str) -> bool:
		return rom_int in ['I', 'II', 'III']

	def validate(self) -> bool:
		print(self._q)
		return [
			self._validate_name(self._q[0]),
			self._validate_date(self._q[1]),
			self._validate_company(self._q[2]),
			self._validate_name(self._q[3]),
			True,
			self._validate_name(self._q[5]),
			True,
			self._validate_name(self._q[7]),
			True,
			self._validate_name(self._q[9]),
			self._validate_reason(self._q[10]),
			self._validate_reason(self._q[11]),
			self._validate_status(self._q[12]),
			self._q[13] == '2',
			self._validate_rom_int(self._q[14]),
			self._validate_int(self._q[15])
		]

	def where(self) -> str:
		for_js = ''
		result = self.validate()
		for_js += '' if result[0] else 'Ошибка в №1: Вы должны ввести исключительно фамилию, имя и отчество, начиная с заглавной буквы через пробелы!<br>'
		for_js += '' if result[1] else 'Ошибка в №2: Вводите время, в формате дд.мм.гггг<br>Например: 01.01.2024<br>'
		for_js += '' if result[2] else 'Ошибка в №3: Введите имя компании в таком виде:<br>- ИП Иванов Иван Иванович<br>- ЗАО "Газмяс"<br>- ООО "Лег"<br>'
		for_js += '' if result[3] else 'Ошибка в №4: Вы должны ввести исключительно фамилию, имя и отчество, начиная с заглавной буквы через пробелы!<br>'
		for_js += '' if result[5] else 'Ошибка в №6: Вы должны ввести исключительно фамилию, имя и отчество, начиная с заглавной буквы через пробелы!<br>'
		for_js += '' if result[7] else 'Ошибка в №8: Вы должны ввести исключительно фамилию, имя и отчество, начиная с заглавной буквы через пробелы!<br>'
		for_js += '' if result[9] else 'Ошибка в №10: Вы должны ввести исключительно фамилию, имя и отчество, начиная с заглавной буквы через пробелы!<br>'
		for_js += '' if result[10] else 'Ошибка в №11: Введите только что-то одно:<br>- "первичный"<br>- "внеплановый"<br>- "вводный"<br>- "целевой"<br>- "повторный<br>'
		for_js += '' if result[11] else 'Ошибка в №12: Введите только что-то одно:<br>- "первичный"<br>- "внеплановый"<br>- "вводный"<br>- "целевой"<br>- "повторный<br>'
		for_js += '' if result[12] else 'Ошибка в №13: <br>- "водитель"<br>- "машинист крана-манипулятора"<br>- "машинист крана автомобильного"<br>- "машинист  автогидроподъемника"<br>- "машинист экскаватора-погрузчика"<br>'
		for_js += '' if result[13] else 'Ошибка в №14: Введите только число 2!<br>'
		for_js += '' if result[14] else 'Ошибка в №15: Введите только "I" или "II" или "III"<br>'
		for_js += '' if result[15] else 'Ошибка в №16: Введите исключительно число!<br>'
		return for_js
