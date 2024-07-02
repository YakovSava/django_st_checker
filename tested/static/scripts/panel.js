async function downloadDocument() {
	let resp = await fetch(`/api/getDoc?session=${url.searchParams('session')}`);
	let response = await resp.json();

	window.location.replace(response['url']);
}

async function adminDownload() {
	let resp = await fetch(`/api/getDoc?session=admin`);
	let response = await resp.json();

	window.location.replace(response['url'])
}

function toQuest() {
	window.location.replace('/quest');
}

function removeCompany() {
	// TODO
}