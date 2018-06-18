import xmlrpc.client
from form import Form #Formulario 

formulario = Form()
nombre = formulario.getName()
apellido = formulario.getLastName()
ci = formulario.getCI()
f_n = formulario.getDate()
lugar_n = formulario.getPlace()
foto = formulario.getFoto()
#f_array = formulario.getFotoArray() #bytes de la foto 
#array de bytes de la foto

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
#multicall = xmlrpc.client.MultiCall(proxy)

try:

	with open(foto, "rb") as handle:
		buf = xmlrpc.client.Binary(handle.read())
	
	result = proxy.formulario(nombre,apellido,ci,f_n,lugar_n,buf)

except xmlrpc.client.Fault as err:
    print("A fault occurred")
    print("Fault code: %d" % err.faultCode)
    print("Fault string: %s" % err.faultString)

with open("avatar_foto.png", "wb") as handle1:
    	handle1.write(proxy.foto().data)

print("respuesta: ", result)