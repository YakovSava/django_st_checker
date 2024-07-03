from sys import platform
from time import strftime
from random import randint
from docx import Document as _Document
from api.models import Company

class DocError(Exception): pass

class Document:

	def __init__(self, session:str=''):
		# if len(data) != 16:
		# 	raise DocError('Not all data has been transfered!')
		if session == '':
			raise DocError('The user\'s session data has not been transmitted!')
		# self._data = data
		self._session = session

	def _collect_data(self) -> dict:
		# Мне менее больно от этого
		data = Company.objects.filter(session=self._session)
		return {
			"ФИО": data.fcs,
			"фио": data.fcs,
			"Дата протокола": strftime("%d.%m.%y"),
			"Член1": data.fcs_commissions1,
			"Член2": data.fcs_commissions2,
			"Член3": data.fcs_commissions3,
			"Д1": data.commisions_status1,
			"Д2": data.commisions_status2,
			"Д3": data.commisions_status3,
			"Должность": data.status,
			"Причина": data.reason,
			"Компания": data.company_name,
			"номер программы": "20", # For example
			"для кого": data.status+'а',
			"№": '1', # ???
			"№2": '1', # ???????
			"группа": data.electrical_safety_group,
			"группаП": data.electrical_safety_group,
			"Дата ЭБ": f"{randint(1, 30)}.{randint(1, 12).{randint(2025, 2027)}}", # For example
			"ЭНФ": "(энф?)",
			"Инструктаж": data.reason_for_check,
			"Дата ПЭБ": f"{randint(1, 30)}.{randint(1, 12).{randint(2025, 2027)}}", # For example
			"Стаж": data.work_exp
		}

	def _replacement(self, words:dict, filename:str) -> str:
		doc = _Document(filename)
		for paragraph in doc.paragraphs:
			try:
				paragraph.text = paragraph.text.format(**words)
			except KeyError:
				continue
		for table in doc.tables:
			for row in table.rows:
				for cell in row.cells:
					try:
						cell.text = cell.text.format(**words)
					except KeyError:
						continue
		doc.save(filename.split('.')[0]+self._session+'.docx')
		return filename.split('.')[0]+self._session+'.docx'

	def get(self, filename:str) -> str:
		words = self._collect_data()
		return self.convert_to_pdf(self._replacement(words, filename))

	def convert_to_pdf(self, filename:str) -> str:
		pdf_filename = filename.split('.')[0]+'.pdf'
		if platform == 'win32':
			from docx2pdf import convert
			convert(filename, pdf_filename)
		else: # For Linux
			from os import rename, remove
			from subprocess import run

			run(['librepffoce', '--headless', '--convert-to', 'pdf', filename, '--outdir', 'tmp'], check=True)
			rename(f'tmp/{pdf_filename}', pdf_filename)
			remove(f'tmp/pdf_filename')
		return pdf_filename