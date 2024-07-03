function get(name){
   if(name=(new RegExp('[?&]'+encodeURIComponent(name)+'=([^&]*)')).exec(location.search))
      return decodeURIComponent(name[1]);
}

async function downloadDocument() {
	let resp = await fetch(`/api/getDoc?session=${get('session')}`);
	let response = await resp.json();

	window.location.replace(response['link']);
}

async function downloadAllCompany() {
	let resp = await fetch(`/api/getDoc?session=${get('session')}`);
	let response = await resp.json();

	window.location.replace(response['link']);
}

async function adminDownload() {
	alert('Нет, вы не супер-админ!');
}

function toQuest() {
	window.location.replace('/quest');
}