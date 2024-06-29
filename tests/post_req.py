from requests import post

if __name__ == '__main__':
	resp = post('http://127.0.0.1:8000/api/auth', data={"login": "abc", "password": "abc"})
	print(resp.text)