'''
	Formulario de usuario
'''
#from foto import Foto
import pickle # serializar objetos
from datetime import datetime
class Form(object):
	"""formulario for From"""

	def __init__(self):
		super(Form, self).__init__()
		
		self.nombre = input('Introduzca su Nombre: ')
		self.apellido = input('Introduzca su Apelido: ')
		self.ci = input('Introduzca su CI: ')
		self.f_n = input('Introduzca su Fecha de Nacimiento, (dd-mm-aa): ')
		
		self.lugar_n = input('Introduzca su Lugar de Nacimiento: ')
		#url = input('Introduzca la ubicación de su Foto')
		#self.foto = Foto('media/estudiante32.png',400)

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

	def getFotoArray(self):
		#return self.foto.getCache_Array()
		return True

	def getFoto(self):
		return self.foto.getCache()

	def getSerialize(self):
		datos = {'nombre':self.nombre,'apellido':self.apellido,'ci':self.ci,'fecha_n':self.f_n,'lugar_n':self.lugar_n}
		return pickle.dumps(datos)