diccionario = {}
diccionario_historial = {}
diccionario_clave = {}
diccionario_saldo = {}
diccionario_cajero = {}

def CrearCuenta(opcion):
	if opcion == "Usuario":
		cuentasArchivo = open("usuarios.txt")
		cuenta = cuentasArchivo.readlines()
		diccionario_usuario = Splitter(cuenta,0)
		return diccionario_usuario

	elif opcion == "Saldo":
		cuentasArchivo = open("saldo.txt")
		cuenta = cuentasArchivo.readlines()
		diccionario_s = Splitter(cuenta,0)
		return diccionario_s

	elif opcion == "Cajero":
		cuentasArchivo = open("cajero.txt")
		cuenta = cuentasArchivo.readlines()
		diccionario_c = Splitter(cuenta,0)
		return diccionario_c

	elif opcion == "Historial":
		cuentasArchivo = open("historial.txt")
		cuenta = cuentasArchivo.readlines()
		diccionario_h = Splitter(cuenta,0)
		return diccionario_h

def Splitter(cuenta,x):
	diccionario = {}
	cuentaComa = cuenta[0].split(",")
	if len(cuentaComa)> x:
		try:
			cuentaRec =cuentaComa[x].split()
			key,value = cuentaRec
			keyRec = key
			valueRec = int(value)
			diccionario[keyRec] = valueRec
			x+=1
			Splitter(cuenta,x)
		except ValueError:
			cuentaRec =cuentaComa[x].split()
			key,value = cuentaRec
			keyRec = key
			valueRec = value
			diccionario[keyRec] = valueRec
			x+=1
			Splitter(cuenta,x)

		except ValueError()


	else:
		return diccionario

	return diccionario

diccionario_clave = CrearCuenta("Usuario")
diccionario_saldo = CrearCuenta("Saldo")
diccionario_cajero = CrearCuenta("Cajero")
diccionario_historial = CrearCuenta("Historial")

print(diccionario_clave)
print(diccionario_saldo)
print(diccionario_cajero)

