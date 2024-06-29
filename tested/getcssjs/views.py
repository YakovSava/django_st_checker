

class CSS:

	def __init__(self, getter:object):
		self._get = getter # TODO

	def getfile(self, site_path:str) -> str:
		return self._get.read('hmtl/'+site_path.split('/')[-1])


class JS:

	def __init__(self, getter:object):
		self._get = getter # TODO

	def getfile(self, site_path:str) -> str:
		return self._get.read('hmtl/'+site_path.split('/')[-1])