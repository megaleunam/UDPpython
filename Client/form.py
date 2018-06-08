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

	def getName():
		return self.nombre
	def getLastName():
		return self.apellido
	def getCI():
		return self.ci
	def getDate():
		return self.f_n
	def getPlace():
		return self.lugar_n