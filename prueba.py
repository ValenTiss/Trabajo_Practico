diccionario_historial = {}
diccionario_clave = {}
diccionario_saldo = {}
diccionario_cajero = {}
def CrearCuenta(opcion):
	if opcion == "Usuario":
		cuentasArchivo = open("usuarios.txt")
		cuenta = cuentasArchivo.readlines()
		diccionario_us = Splitter(cuenta,0,diccionario_clave) 
		diccionario_u = EntValue(diccionario_us)
		return diccionario_u

	elif opcion == "Saldo":
		cuentasArchivo = open("saldo.txt")
		cuenta = cuentasArchivo.readlines()
		diccionario_us = Splitter(cuenta,0,diccionario_saldo)
		diccionario_u = EntValue(diccionario_us)
		return diccionario_u

	elif opcion == "Cajero":
		cuentasArchivo = open("cajero.txt")
		cuenta = cuentasArchivo.readlines()
		diccionario_ca = Splitter(cuenta,0,diccionario_cajero)
		return diccionario_ca

	elif opcion == "Historial":
		cuentasArchivo = open("historial.txt")
		cuenta = cuentasArchivo.readlines()
		diccionario_h = Splitter(cuenta,0,diccionario_historial)
		return diccionario_h

def Splitter(cuenta,x,diccionario):
	cuentaComa = cuenta[0].split(",")
	if len(cuentaComa)> x:
		try:
			cuentaRec =cuentaComa[x].split()
			key,value = cuentaRec
			keyRec = key
			valueRec = value
			diccionario[keyRec] = valueRec
			x+=1
			Splitter(cuenta,x,diccionario)
		except ValueError:
			cuentaRec =cuentaComa[x].split(":")
			key,value = cuentaRec
			keyRec = key
			valueRec = value
			diccionario[keyRec] = valueRec
			x+=1
			Splitter(cuenta,x,diccionario)
	else:
		return diccionario

	return diccionario

def EntValue(diccionario):
	diccionario = dict((k, int(v)) for k, v in diccionario.items())
	return diccionario


diccionario_clave = CrearCuenta("Usuario")
diccionario_saldo = CrearCuenta("Saldo")
diccionario_cajero = CrearCuenta("Cajero")
diccionario_historial = CrearCuenta("Historial")
print(diccionario_cajero)