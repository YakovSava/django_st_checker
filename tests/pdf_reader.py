from os import listdir
from PyPDF2 import PdfReader

pdf = PdfReader('Протоколы/ИП Иванов П.П. Петров Иван Иванович.pdf')
print('Длина: ', len(pdf.pages))
for i in range(len(pdf.pages)):
	print(f'{"-"*20} Страница №{i} {"-"*20}')
	print(pdf.pages[i].extract_text())
	print('-'*50)
	input('Продолжить?')