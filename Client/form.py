'''
	Formulario de usuario
'''
class Form(object):
	"""formulario for From"""

	def __init__(self):
		super(Form, self).__init__()
		
		self.nombre = input('Introduzca su Nombre: ')
		self.apellido = input('Introduzca su Apelido: ')
		self.ci = input('Introduzca su CI: ')
		self.f_n = input('Introduzca su Fecha de Nacimiento: ')
		self.lugar_n = input('Introduzca su Lugar de Nacimiento: ')		

	def getName(self):
		return self.nombre
	def getLastName(self):
		return self.apellido
	def getCI(self):
		return self.ci
	def getDate(self):
		return self.f_n
	def getPlace(self):
		return self.lugar_n