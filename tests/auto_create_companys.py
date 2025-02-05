from time import sleep
from random import randint, choice
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By

fake = Faker('ru_RU')
url = "http://127.0.0.1:8000/quest/"

companys = ['РАО «Боброва Щербаков и Миронова»', 'НПО «Зимин»', 'ОАО «Якушева Кулакова»', 'ООО «Лазарева»', 'ЗАО «Афанасьева»']

def generator_dict() -> dict:
	return {
		"company": lambda: choice(companys),
		"jobs": fake.job,
		"name": fake.name,
		"rom_num": lambda: "I"*randint(1, 3),
		"stage": lambda: randint(1, 5),
		"date": lambda: f"{randint(1, 30)}.{randint(1, 12)}.{randint(2020, 2024)}",
		"reason": lambda: choice(['первичный', 'внеплановый', 'вводный', 'целевой', 'повторный']),
		"job": lambda: choice(['водитель','машинист крана-манипулятора','машинист крана автомобильного','машинист  автогидроподъемника','машинист экскаватора-погрузчика',])
	}

def generate_lst() -> list:
	gd = generator_dict()
	return [
		gd['name'](),
		gd['date'](),
		gd['company'](),
		gd['name'](),
		gd['jobs'](),
		gd['name'](),
		gd['jobs'](),
		gd['name'](),
		gd['jobs'](),
		gd['name'](),
		gd['reason'](),
		gd['reason'](),
		gd['job'](),
		'2',
		gd['rom_num'](),
		gd['stage']()
	]

def exsist_element(driver, id) -> bool:
	try:
		driver.find_element(By.ID, id)
	except:
		return False
	else:
		return True


def main(driver):
	while True:

		driver.get(url=url)

		for item in generate_lst():
			universal_input = driver.find_element(By.ID, "answer-input")
			universal_input.send_keys(item)

			universal_button = driver.find_element(By.ID, 'submit-button')
			universal_button.click()
			sleep(0.1)
		sleep(2)

if __name__ == '__main__':
	try:
		driver = webdriver.Firefox()
		main(driver)
	except KeyboardInterrupt:
		driver.close()
