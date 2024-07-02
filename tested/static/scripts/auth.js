async function check(data) {
	console.log(data);

	let resp = await fetch(`/api/auth?data=${data}`);
	let response = await resp.json();

	console.log(response);

	if (response['result']) {
		window.location.replace(`/worker?session=${response['session']}`);
	} else {
		alert(response['reason']);
	}
}

function send() {
	let login = document.getElementById("login").value;
	let passwd = document.getElementById("password").value;
	console.log(password);
	if ((login == '') || (password = '')) {
		alert('Введите оба поля');
	} else {
		console.log(passwd);
		check(JSON.stringify({login: login, passwd: passwd})).then();
	}
}