from nondjmodules.getter import Binder

class GET:

	def __init__(self, getter:Binder=Binder()):
		self._get = getter

	def getfile(self, request, site_path:str) -> str:
		print('html/'+site_path)
		return self._get.read('html/'+site_path)