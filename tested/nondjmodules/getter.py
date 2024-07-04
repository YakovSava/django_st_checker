# Get onli bytes yobj!!!
class Getter:

	def __init__(self, default_mode:str='rb', encoding:str='utf-8'):
		self._def = default_mode
		self._enc = encoding

	def get(self, filename:str) -> bytes or str:
		with open(filename, self._def) as file:
			return file.read()

class MIME: # I'm lazy
	pdf = 'application/pdf'
	zip = 'application/zip'
	doc = 'application/msword'
	excel = 'application/vnd.ms-excel'