'''
	control de Foto de PErfil
'''
class Foto(object):
	"""docstring for Foto"""
	

	def __init__(self, filename,size):
		super(Foto, self).__init__()
		self.filename = filename
		self.size = size
		self.cache_array = []
		self.cache= b''
		self.setCache()

	def setCache(self):
		self.cache_array = []
		self.cache = b''
		with open(self.filename, "rb") as file:
			while True:
				bu = file.read(self.size)		
				if bu == b'':
					break
				self.cache_array.append(bu)
				
		
		file.close()
		return True
	
	def getCache_Array(self):
		self.cache_array.append('fin'.encode())#para saber el final del archivo
		return self.cache_array
	def getCache(self):
		return self.cache

if __name__ == '__main__':
	f = Foto('media/estudiante32.png',200)
	cache = f.getCache()
	foto_archivo = open('foto_name.png','wb')
	foto_archivo.write(cache)
	foto_archivo.close()