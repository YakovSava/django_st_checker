try:
	from binder import reader, writer # Rust modules
	OPTIMIZED = True
except ImportError:
	OPTIMIZED = False

class Binder:

	def __init__(self, use_optim:bool=OPTIMIZED):
		self._opt = use_optim

	def read(self, filename:str) -> str:
		if self._opt:
			return reader(filename)
		else:
			with open(filename, 'r', encoding='utf-8') as file:
				return file.read()

	def write(self, filename:str, data:str) -> None:
		if self._opt:
			return writer(filename, data)
		else:
			with open(filename, 'w', encoding='utf-8') as file:
				return file.read()