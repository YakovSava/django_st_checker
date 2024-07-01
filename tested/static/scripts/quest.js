var questNumber = 0;
var questions = [
	'Ф.И.О. работника<br>Вводите ФИО полностью и с заглавной буквы и без сокращений',
	'Дата проверки знаний<br>Введите дату в формате "дд.мм.гггг"',
	'Наименование компании<br>Например:<br>- ИП Иванов Иван Иванович<br>- ЗАО "Газмяс"<br>- ООО "Лег"',
	'ФИО Председателя комиссии<br>Вводите ФИО полностью и с заглавной буквы и без сокращений',
	'Должность председателя комиссии',
	'ФИО 1-го члена комиссии<br>Вводите ФИО полностью и с заглавной буквы и без сокращений',
	'Должность 1-го члена комиссии',
	'ФИО 2-го члена комиссии<br>Вводите ФИО полностью и с заглавной буквы и без сокращений',
	'Должность 2-го члена комиссии',
	'Ответственный за электрохозяйство<br>Вводите ФИО полностью и с заглавной буквы и без сокращений',
	'Причина проверки знаний<br>Введите тип инструктажа: внеплановый, первичный и т.д.',
	'Противопожарный инструктаж<br>Введите тип инструктажа: внеплановый, первичный и т.д.',
	'Должность<br>Введите из списка:<br>- Водитель<br>- Машинист крана-манипулятора<br>- Машинист крана автомобильного<br>- Машинист автогидроподъёмника<br>- Машинист экскаватора-погрузчика',
	'№ Программы водитель<br>Введите 2',
	'Группа ЭБ<br>Введите римскими цифрами: "I", "II" или "III"',
	'Стаж работы<br>Введите число'
];
var answer = [];

function destroyGrid() {
	document.getElementById("question-number").remove();
	document.getElementById("answer-input").remove();
	document.getElementById("submit-button").remove();
}

function endQuest() {
	destroyGrid();
	document.getElementById("question-text").innerHTML="Спасибо!";
}

function failureQuest(errs) {
	destroyGrid();
	document.getElementById("question-text").innerHTML=`Вы неправильно заполнили некоторые поля, а именно:<br>${errs}!`;
}

async function sendResults(results) { // AJAX
	let resp = await fetch(`/api/result?data=${results}`);
	let response = await resp.json();

	if (response['result']) {
		endQuest();
		setTimeout(() => { window.location.replace('/') }, 10000); 
	} else {
		failureQuest(response['error']);
		setTimeout(() => { window.location.replace('/quest') }, 10000); 

	}

}

function nextQuest() {
	document.getElementById("question-number").innerHTML=`${questNumber+1} из ${questions.length+1}`;
	if (document.getElementById("answer-input").value == '') {
		alert('Введите значение!');
		return;
	}
	if (questNumber != questions.length) {
		document.getElementById("question-text").innerHTML=questions[questNumber];
		questNumber++;
		answer.push(document.getElementById("answer-input").value);

		document.getElementById("answer-input").value = '';
	} else {
		answer.push(document.getElementById("answer-input").value);
		sendResults(answer).then();
	}
}

document.getElementById("question-number").innerHTML=`${questNumber+1} из ${questions.length+1}`;
document.getElementById("question-text").innerHTML=questions[questNumber];
questNumber++;