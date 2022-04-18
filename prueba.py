diccionario_historial = {}
diccionario_clave = {}
diccionario_saldo = {}
diccionario_cajero = {}
clave = "usuarios.txt"
historial = "historial.txt"
cajero = "cajero.txt"
saldo = "saldo.txt"
def CrearCuenta(opcion):
	if opcion == "Usuario":
		cuentasArchivo = open(clave)
		cuenta = cuentasArchivo.readlines()
		diccionario_us = Splitter(cuenta,0,diccionario_clave) 
		diccionario_u = EntValue(diccionario_us)
		return diccionario_u

	elif opcion == "Saldo":
		cuentasArchivo = open(saldo)
		cuenta = cuentasArchivo.readlines()
		diccionario_us = Splitter(cuenta,0,diccionario_saldo)
		diccionario_u = EntValue(diccionario_us)
		return diccionario_u

	elif opcion == "Cajero":
		cuentasArchivo = open(cajero)
		cuenta = cuentasArchivo.readlines()
		diccionario_ca = Splitter(cuenta,0,diccionario_cajero)
		return diccionario_ca

	elif opcion == "Historial":
		cuentasArchivo = open(historial)
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
			diccionario[keyRec]= valueRec.replace("\\n","\n")
			x+=1

			Splitter(cuenta,x,diccionario)
	else:
		return diccionario

	return diccionario

def EntValue(diccionario):
	diccionario = dict((k, int(v)) for k, v in diccionario.items())
	return diccionario

def Actualizar(filepath,diccionario):
	string = str(diccionario)
	if filepath == historial:
		string = string.replace("'","")
		string = string.replace(":  ",":")
		len_string = len(string)
		abrirDocumento = open(filepath,"w")
		abrirDocumento.write(string[1:len_string-1])
		abrirDocumento.close()


	else:
		string = string.replace("'","")
		string = string.replace(":","")
		len_string = len(string)
		abrirDocumento = open(filepath,"w")
		abrirDocumento.write(string[1:len_string-1])
		abrirDocumento.close()

def Finalizar():
	Act_clave =Actualizar(clave,diccionario_clave)
	Act_saldo = Actualizar(saldo,diccionario_saldo)
	Act_cajero = Actualizar(cajero,diccionario_cajero)
	Act_historial = Actualizar(historial,diccionario_historial)
	

diccionario_clave = CrearCuenta("Usuario")
diccionario_saldo = CrearCuenta("Saldo")
diccionario_cajero = CrearCuenta("Cajero")
diccionario_historial = CrearCuenta("Historial")

Finalizar()
