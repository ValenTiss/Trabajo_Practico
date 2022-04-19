"""
Autores:Federico Alfaro y Valentin Tissera Doncini
Profesor:Saul Calderon Ramirez
Fecha de entrega: 19 / 04 /22
"""
import sys
import time
import random

diccionario_historial = {}
diccionario_clave = {}
diccionario_saldo = {}
diccionario_cajero = {}
clave = "usuarios.txt"
historial = "historial.txt"
cajero = "cajero.txt"
saldo = "saldo.txt"

#La funcion Usuario se utiliza para determinar si los caracteres son letras en minuscula o mayuscula.
def Usuario(entrada,x):
	entrada_len = len(entrada)
	#Se crea una variable para hacer que la funcion sea recursiva.
	if(x < entrada_len):
		#Si el caracter es una letra se le suma 1 a la funcion.
		if ( 90>= ord(entrada[x]) >= 65 or 122>= ord(entrada[x]) >= 97 ):
			x +=1
			Usuario(entrada,x)

		#Si el caracter es un numero se entrada a la funcion Exp_Num.
		elif (48 <= (ord(entrada[x])) <= 57):
			Exp_Num(entrada,x,0)

		#El usuario ingreso un caracter no correcto,es rebotado del sistema.
		else:
			print("Usuario no valido.")
			Usuario(input("Ingrese su usuario: "), 0 )

	#El usuario ingreso una cuenta no valida.
	else:
		print("Usuario no valido.")
		Usuario(input("Ingrese su usuario: "), 0 )
			


#La funcion Exp_Num clasifica los usuarios ingresados por los ultimos 4 caracteres y el ultimo.
def Exp_Num(Num,x,n):
	entrada_largo =len(Num)
	#Se crea una variable para hacer la funcion recursiva por 3 veces maximo.
	if(38 >= ord(Num[entrada_largo-1]) >= 35 or ord(Num[entrada_largo-1]) == 63 or ord(Num[entrada_largo-1]) == 33 ):
		#La variable 3 se ejecuta dos veces verificando que sean numeros.
		if (n<2):
			#Se le suma 1 a la variable n para que la funcion siga su recursividad.
			if (48 <= (ord(Num[x])) <= 57):
				x +=1
				n +=1

				Exp_Num(Num,x,n)
				#El usuario fue aceptado pasa a la funcion Es_pin 
				if (n == 2):
					Acceso_cuenta(Num,input("Ingrese su contraseña: "))
					Es_pin(Num,0)

				#El usuario es rebotado vuelve a la funcion Usuario
				if (n>2):
					print("Usuario no valido.")
					Usuario(input("\nIngrese su nombre de usuario:"),0)

			#El usuario ingreso un caracter no correcto,es rebotado del sistema.
			else:
				print("Usuario no valido.")
				Usuario(input("\nIngrese su nombre de usuario:"),0)
	#Si la variable n para su maximo el usuario es rebotado del sistema.
	else:
		print("Usuario no valido.")
		Usuario(input("\nIngrese su nombre de usuario:"),0)
				

#La función Es_pin verifica si un string contiene únicamente un número de 4 dígitos
def Es_pin(entrada_usuario, contador): 

  #Si la hilera tiene 4 dígitos
  if len(entrada_usuario) == 4: 
		
    #Si el contador no ha registrado los 4 caracteres 	
    if contador < 4:

      #Si cada caracter es un número según la tabla ASCII
      if 48 <= ord(entrada_usuario[contador])  <= 57 :
        contador+=1
	
	#se realiza el llamado recursivo
        return Es_pin(entrada_usuario, contador)
      #El caracter no es un número
      else:
        return False

    #Se verificó que los 4 caracteres son números
    else:
      return True

  #La hilera no tiene 4 dígitos
  return False



#Permite el acceso de la cuenta al menú de opciones
def Acceso_cuenta(usuario,password): 
	
	#Si el nombre de usuario coincide con algún nombre creado anteriormente
	if usuario in diccionario_clave:
		
		#Si la clave es correcta para el usuario seleccionado
		if diccionario_clave[usuario]== int(password):
				print("Datos ingresados correctamente.")
				volver_al_menu(usuario)
				
		#La clave no coincide con la clave del usuario		
		else:
			#Permite al usuario elegir si desea volver a probar con otra clave o terminar terminar el programa
			terminar= input("Presione 1 para volver a introducir su contraseña o cualquier otra tecla para terminar \n")

			#Si terminar no es un string vacío
			if terminar!="":
				#Si el usuario selecciona 1
				if ord(terminar) == 49:
					
					#Se vuelve a desplegar la opción de volver a introducir la clave
					Acceso_cuenta(usuario , input("Contraseña incorrecta \n Ingrese su contraseña nuevamente: "))
	
			#terminar es un string vacío
			else:
				Finalizar()
				
				
	#El nombre de usuario introducido no existe
	else:
		#Se pregunta al que corre el programa si desea volver a introducir sus datos o si desea terminar el programa
		opcion = input("Usuario no valido. \n Presione 1 para volver a introducir sus datos o cualquier otra tecla para terminar \n" )
		
		#Si elige 1
		if ord(opcion) == 49:
			
			#Se vuelve a pedir el nombre de usuario y clave
			Solicitar_cuenta()

#Inicio del programa, verifica si se desea ingresar al sistema como banquero o como cliente
def Inicio():  

  #Guarda la opción para saber si el usuario desea ingresar como banquero o como usuario
  banquero_o_usuario = input("Bienvenido al Banco ValFe. \n Si desea ingresar como banquero presione 1 , si desea ingresar como cliente presione 2 " ) #Tenemos que elegir el nombre del Banco ------------ ???

  #Si el usuario escribió algo
  if banquero_o_usuario == "1":
		
	  #Si el usuario ingresa el número 1 por lo que desea ingresar como banquero
	  if ord(banquero_o_usuario) == 49:

	    #Se solicita la clave del banquero y se guarda en la variable clave_banquero
	    clave_banquero = input("Ingrese la clave para poder ingresar como banquero: ") #La clave es SAUL

	    #Si la clave del banquero es correcta
	    if clave_banquero == "SAUL":
	      #Despliega las opciones del banquero	
	      Consola_banquero()	

	    #La clave del banquero se introdujo de manera incorrecta	
	    else:

	      #Se notifica el error		
	      print("Intento sospechoso de entrar al sistema, se ha notificado a las autoridades correspondientes.")
		
	  else:
	    Finalizar()
  elif banquero_o_usuario == "2":
  	Solicitar_cuenta()

  else:
  	Finalizar()
  	


#Función que se encarga de pedir el nombre de usuario y llamar a la función Usuario(nmb_usr,0) para verificar su existencia
def Solicitar_cuenta():
	
	#Variable que guarda el nombre de usuario recién digitado
	nmb_usr = input("Digite la cuenta: ")
	
	#Se invoca a la función Usuario(nmb_usr,0) que verifica que el nombre de usuario ingresado cumpla con la expresión regular y esté registrado
	Usuario(nmb_usr,0)
	
#Verifica que un string contenga unicamente a un número entero
def Es_numero(entrada_usuario, contador): 
	"""
	Entradas: entrada_usuario (string), contador (0)
  Salidas: True o False
	"""
	entrada_usuario = str(entrada_usuario)
	if len(str(entrada_usuario)) != 0: 
		if contador < len(str(entrada_usuario)):
			if 48 <= ord(entrada_usuario[contador]) <= 57 :
				contador+=1
				return Es_numero(entrada_usuario, contador)
			else:
				return False
		else:
			return True
	return False

	
	
def volver_al_menu(usuario):
	decision=input("Si desea hacer un retiro presione 0, realizar un depósito presione 1, revisar su saldo presione 2 o ver su historial de transacciones presione 3: ")
	if decision =="0":
		return Menu(decision,usuario)
	elif decision =="1":
		return Menu(decision,usuario)
	elif decision =="2":
		return Menu(decision,usuario)
	elif decision =="3":
		return Menu(decision,usuario)



		

#Esta función permite llevar a cabo las opciones del usuario, llamando a otras funciones dependiendo de lo seleccionado por el usuario con anterioridad
def Menu(decision,usuario_adm):
	
	#Si el parámetro decision no es un string vacío
	if decision !="":

		#Si el usuario eligió retiro(0)
		if ord(decision) == 48:

			#Variable que contiene el nombre de un cajero digitado por el usuario
			cajero= input("Ingrese el nombre del cajero en el que desea retirar su dinero: ")
			
			#Si el cajero digitado por el usuario es un cajero existente
			if cajero in diccionario_cajero:

				#Variable que pregunta al usuario el monto a retirar
				monto_string = input("Ingrese el monto en pesos que desea retirar: ")
				
				#Si el monto digitado por el usuario es un número entero
				if Es_numero(monto_string,0):

					#Se invoca el saldo asociado a la cuenta ingresada
					dinero_del_usuario= diccionario_saldo[usuario_adm]

					#Si el string que guarda el saldo del usuario es un número y no tiene errores
					if Es_numero(dinero_del_usuario,0):
						
						#Cantidad de billetes de cada denominación en el cajero seleccionado
						dinero_en_cajero= diccionario_cajero[cajero]
						return retirar_dinero(int(monto_string), usuario_adm, cajero,dinero_en_cajero)

					#El string que guarda el saldo del usuario en el diccionario tiene un error
					else:
						return print("Error en diccionario_saldo, el saldo de la cuenta es: " + dinero_del_usuario)

				#El monto digitado por el usuario no es un número entero
				else:
					raise ValueError("El monto digitado no es un número entero")

			#El cajero digitado no existe
			else:
				print("El cajero solicitado no existe")
				#Se regresa al menu de opciones para el usuario
				return volver_al_menu(usuario_adm)
		
		#Mostrar saldo
		elif ord(decision) == 50:
			print("El saldo del usuario \""+str(usuario_adm)+ "\" es de "+ str(diccionario_saldo[usuario_adm])+" pesos.")
			return volver_al_menu(usuario_adm)
			
		#depositar dinero
		elif ord(decision) == 49:

			#Variable que contiene el nombre de un cajero digitado por el usuario
			cajero= input("Ingrese el nombre del cajero en el que desea retirar su dinero: ")
			
			#Si el cajero digitado por el usuario es un cajero existente
			if cajero in diccionario_cajero:
				return depositar_dinero(usuario_adm, cajero)
		
			#El cajero digitado no existe
			else:
				print("El cajero solicitado no existe")
				#Se regresa al menu de opciones para el usuario
				return volver_al_menu(usuario_adm)

		#Historial
		elif ord(decision) == 51:

			#Despliega el historial del usuario ingresado
			print("El historial del usuario "+ usuario_adm +" es:\n"+diccionario_historial[usuario_adm])
			return volver_al_menu(usuario_adm)


		else:
			Finalizar()

	#El parámtero desicion es un string vacío
	else: 
		Finalizar() 

#--------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Función que se encarga de verificar que el monto en la cuenta del usuario tenga el monto que desea retirar y llama a otras funciones para encargarse del proceso de retirar dinero de la cuenta del usuario y descontar los billetes de los cajeros
"""
def retirar_dinero(monto, usuario, cajero,dinero_en_cajero):
  """
  Entradas: Monto (número natural), usuario (string), dinero_cajero (string)
  Los valores deben estar verificados cuando entran como parámetros
  """
  dinero_del_usuario= int(diccionario_saldo[usuario]) #Se invoca el saldo asociado a la cuenta ingresada
  dinero_en_cajero_int= convertir_string_a_dinero(dinero_en_cajero) # dinero total del cajero en int
  if monto <= dinero_del_usuario: #verifica si el usuario tiene el monto en su cuenta
    if monto  <= dinero_en_cajero_int: #verifica si el cajero tiene el monto ingresado disponible para retirar
      return retirar_dinero_del_cajero(monto, usuario, cajero,dinero_en_cajero) #Se llama a la función que elige la menor cantidad de billetes para devolver 
    else: 
      print("Dinero no disponible en este cajero, por favor desplácese a otro cajero o vuelva en unos días cuando se llenen las reservas")
  else:
    print("Fondos insuficientes para realizar esta transacción. Para darle el mejor servicio el Banco ValFe pone a su dispocisión el servicio CRÉDITO EN LA PALMA DE SU MANO, para saber más acerca de este servicio pregunte en la sucursal más cercana") 

#Convierte los string que contienen la cantidad de billetes de cada denominación a un entero donde cada denominación está en el formato "1.2.5.10.20.50.100" donde en este caso cada número representa el valor del billete, sin embargo, en cada casilla se escribe la cantidad de billetes
def convertir_string_a_dinero(string):
  lista_billetes= string.split(".") #Lista que contiene la cantidad de billetes por denominación
  return int(lista_billetes[0]) + int(lista_billetes[1])*2 + int(lista_billetes[2])*5 + int(lista_billetes[3])*10 + int(lista_billetes[4])*20 + int(lista_billetes[5])*50 + int(lista_billetes[6])*100

#Se encarga de devolver la menor cantidad de billetes, actualiza la cantidad de billetes en el cajero  y dinero disponible del usuario
def retirar_dinero_del_cajero(monto, usuario, cajero,dinero_en_cajero):
	billete_100= devolver_billete_100(monto, dinero_en_cajero)
	monto -= billete_100*100
	billete_50= devolver_billete_50(monto, dinero_en_cajero)
	monto -= billete_50*50
	billete_20= devolver_billete_20(monto, dinero_en_cajero)
	monto -= billete_20*20
	billete_10= devolver_billete_10(monto, dinero_en_cajero)
	monto -= billete_10*10
	billete_5= devolver_billete_5(monto, dinero_en_cajero)
	monto -= billete_5*5
	billete_2= devolver_billete_2(monto, dinero_en_cajero)
	monto -= billete_2*2
	billete_1= devolver_billete_1(monto, dinero_en_cajero)
	monto -= billete_1*1
	if monto==0:
		disminucion_cajero= str(billete_1)+"."+str(billete_2)+"."+str(billete_5)+"."+str(billete_10)+"."+str(billete_20)+"."+str(billete_50)+"."+str(billete_100) #cantidad de billetes de cada denominación que se están retirando 
		disminucion_cajero_int= convertir_string_a_dinero(disminucion_cajero)
		nuevo_saldo= int(diccionario_saldo[usuario]) - disminucion_cajero_int
		diccionario_saldo[usuario]= str(nuevo_saldo)
		print("Transacción realizada con éxito, el saldo en su cuenta ahora es de "+ diccionario_saldo[usuario] +" pesos")
		tiempo= time.strftime('%d-%m-%Y %H horas %M minutos', time.localtime()).split()
		fecha= tiempo[0]
		hora= tiempo[1]
		#Se actualiza el historial
		diccionario_historial[usuario]+= " Se realizó un retiro de   "+ str(disminucion_cajero_int) + " pesos el " + fecha + " a las " + hora + " en el cajero " + cajero + "\n"
		actualizar_cajero_sacando(cajero, disminucion_cajero)

		#Si desea cerrar el programa
		if input("Presione 0 si desea terminar el programa y cualquier otra letra para continuar ")=="0":
			return Finalizar()
		#Si desea continuar
		else:
			return volver_al_menu(usuario)
		

	else:
		return print("No es posible realizar el retiro en este cajero debido a la falta de billetes necesarios")


def actualizar_cajero_sacando(cajero, disminucion):
  dinero_actual_cajero=diccionario_cajero[cajero].split(".")
  disminucion= disminucion.split(".")
  billete_1= str(int(dinero_actual_cajero[0])-int(disminucion[0]))
  billete_2= str(int(dinero_actual_cajero[1])-int(disminucion[1]))
  billete_5= str(int(dinero_actual_cajero[2])-int(disminucion[2]))
  billete_10= str(int(dinero_actual_cajero[3])-int(disminucion[3]))
  billete_20= str(int(dinero_actual_cajero[4])-int(disminucion[4]))
  billete_50= str(int(dinero_actual_cajero[5])-int(disminucion[5]))
  billete_100= str(int(dinero_actual_cajero[6])-int(disminucion[6]))
  dinero_actualizado_cajero= billete_1+"."+billete_2+"."+billete_5+"."+billete_10+"."+billete_20+"."+billete_50+"."+billete_100
  diccionario_cajero[cajero]= dinero_actualizado_cajero 
  return print("Se ha actualizado exitosamente la cantidad de dinero en el cajero, actualmente se posee: "+str(convertir_string_a_dinero(diccionario_cajero[cajero]))+ " pesos") 

#calcula la cantidad de billetes de 100 que se deben y pueden devolver
def devolver_billete_100(monto, dinero_en_cajero):
  """
  Entradas: Monto (int), dinero_en_cajero (string)
  """
  billetes_100_cajero=  int(dinero_en_cajero.split(".")[6]) #cantidad de billetes de 100 en el cajero
  if monto>=100: #si el dinero a retirar es mayor a 100
    billetes_necesarios= monto // 100  # Posible cantidad de billetes de 100 a retirar
    if billetes_necesarios <= billetes_100_cajero: # si la cantidad de posibles billetes 100 a retirar están en el cajero
      return billetes_necesarios
    else:
      return billetes_100_cajero
  else:
    return 0

#calcula la cantidad de billetes de 50 que se deben y pueden devolver
def devolver_billete_50(monto, dinero_en_cajero):
  """
  Entradas: Monto (int), dinero_en_cajero (string)
  """
  billetes_50_cajero=  int(dinero_en_cajero.split(".")[5]) #cantidad de billetes de 50 en el cajero
  if monto>=50: #si el dinero a retirar es mayor a 50
    billetes_necesarios= monto // 50  # Posible cantidad de billetes de 50 a retirar
    if billetes_necesarios <= billetes_50_cajero: # si la cantidad de posibles billetes 50 a retirar están en el cajero
      return billetes_necesarios
    else:
      return billetes_50_cajero
  else:
    return 0

#calcula la cantidad de billetes de 20 que se deben y pueden devolver
def devolver_billete_20(monto, dinero_en_cajero):
  """
  Entradas: Monto (int), dinero_en_cajero (string)
  """
  billetes_20_cajero=  int(dinero_en_cajero.split(".")[4]) #cantidad de billetes de 20 en el cajero
  if monto>=20: #si el dinero a retirar es mayor a 20
    billetes_necesarios= monto // 20  # Posible cantidad de billetes de 20 a retirar
    if billetes_necesarios <= billetes_20_cajero: # si la cantidad de posibles billetes 20 a retirar están en el cajero
      return billetes_necesarios
    else:
      return billetes_20_cajero
  else:
    return 0

#calcula la cantidad de billetes de 10 que se deben y pueden devolver
def devolver_billete_10(monto, dinero_en_cajero):
  """
  Entradas: Monto (int), dinero_en_cajero (string)
  """
  billetes_10_cajero=  int(dinero_en_cajero.split(".")[3]) #cantidad de billetes de 10 en el cajero
  if monto>=10: #si el dinero a retirar es mayor a 10
    billetes_necesarios= monto // 10  # Posible cantidad de billetes de 10 a retirar
    if billetes_necesarios <= billetes_10_cajero: # si la cantidad de posibles billetes 10 a retirar están en el cajero
      return billetes_necesarios
    else:
      return billetes_10_cajero
  else:
    return 0

#calcula la cantidad de billetes de 5 que se deben y pueden devolver
def devolver_billete_5(monto, dinero_en_cajero):
  """
  Entradas: Monto (int), dinero_en_cajero (string)
  """
  billetes_5_cajero=  int(dinero_en_cajero.split(".")[2]) #cantidad de billetes de 5 en el cajero
  if monto>=5: #si el dinero a retirar es mayor a 5
    billetes_necesarios= monto // 5  # Posible cantidad de billetes de 5 a retirar
    if billetes_necesarios <= billetes_5_cajero: # si la cantidad de posibles billetes 5 a retirar están en el cajero
      return billetes_necesarios
    else:
      return billetes_5_cajero
  else:
    return 0


#calcula la cantidad de billetes de 2 que se deben y pueden devolver
def devolver_billete_2(monto, dinero_en_cajero):
  """
  Entradas: Monto (int), dinero_en_cajero (string)
  """
  billetes_2_cajero=  int(dinero_en_cajero.split(".")[1]) #cantidad de billetes de 2 en el cajero
  if monto>=2: #si el dinero a retirar es mayor a 2
    billetes_necesarios= monto // 2  # Posible cantidad de billetes de 2 a retirar
    if billetes_necesarios <= billetes_2_cajero: # si la cantidad de posibles billetes 2 a retirar están en el cajero
      return billetes_necesarios
    else:
      return billetes_2_cajero
  else:
    return 0


#calcula la cantidad de billetes de 1 que se deben y pueden devolver
def devolver_billete_1(monto, dinero_en_cajero):
  """
  Entradas: Monto (int), dinero_en_cajero (string)
  """
  billetes_1_cajero=  int(dinero_en_cajero.split(".")[0]) #cantidad de billetes de 1 en el cajero
  if monto>=1: #si el dinero a retirar es mayor a 1
    billetes_necesarios= monto // 1  # Posible cantidad de billetes de 1 a retirar
    if billetes_necesarios <= billetes_1_cajero: # si la cantidad de posibles billetes 1 a retirar están en el cajero
      return billetes_necesarios
    else:
      return billetes_1_cajero
  else:
    return 0

def actualizar_cajero_metiendo(cajero, adicion):
  dinero_actual_cajero=diccionario_cajero[cajero].split(".")
  adicion= adicion.split(".")
  billete_1= str(int(dinero_actual_cajero[0])+int(adicion[0]))
  billete_2= str(int(dinero_actual_cajero[1])+int(adicion[1]))
  billete_5= str(int(dinero_actual_cajero[2])+int(adicion[2]))
  billete_10= str(int(dinero_actual_cajero[3])+int(adicion[3]))
  billete_20= str(int(dinero_actual_cajero[4])+int(adicion[4]))
  billete_50= str(int(dinero_actual_cajero[5])+int(adicion[5]))
  billete_100= str(int(dinero_actual_cajero[6])+int(adicion[6]))
  dinero_actualizado_cajero= billete_1+"."+billete_2+"."+billete_5+"."+billete_10+"."+billete_20+"."+billete_50+"."+billete_100
  diccionario_cajero[cajero]= dinero_actualizado_cajero
  return print("Actualizacion exitosa, el cajero cuenta con "+ str(convertir_string_a_dinero(diccionario_cajero[cajero]))+ " pesos") 


	#Función que se encarga de registrar los depósitos de dinero del usuario
def depositar_dinero(usuario, cajero):
	"""
  Cada uno de las siguentes variables reciben la cantidad de billetes por cada denominación respectivamente que el usuario desea ingresar
	"""
	billete_100= input("Digite la cantidad de billetes de 100 pesos que desea introducir:")
	billete_50= input("Digite la cantidad de billetes de 50 pesos que desea introducir:")
	billete_20= input("Digite la cantidad de billetes de 20 pesos que desea introducir:")
	billete_10= input("Digite la cantidad de billetes de 10 pesos que desea introducir:")
	billete_5= input("Digite la cantidad de billetes de 5 pesos que desea introducir:")
	billete_2= input("Digite la cantidad de billetes de 2 pesos que desea introducir:")
	billete_1= input("Digite la cantidad de billetes de 1 pesos que desea introducir:")
	if Es_numero(billete_1,0) and Es_numero(billete_2,0) and Es_numero(billete_5,0) and Es_numero(billete_10,0) and Es_numero(billete_20,0) and Es_numero(billete_20,0) and Es_numero(billete_100,0): 
		deposito = billete_1+"."+billete_2+"."+billete_5+"."+billete_10+"."+billete_20+"."+billete_50+"."+billete_100
		actualizar_cajero_metiendo(cajero, deposito)
		diccionario_saldo[usuario]= str(int(diccionario_saldo[usuario])+ convertir_string_a_dinero(deposito))
		deposito_int= convertir_string_a_dinero(deposito)
		print("Se agregaron exitosamente "+str(deposito_int)+" pesos a su cuenta, ahora posee un total de "+ str(diccionario_saldo[usuario]) + " pesos")
		tiempo= time.strftime('%d-%m-%Y %H horas %M minutos', time.localtime()).split(" ")
		fecha= tiempo[0]
		hora= tiempo[1]
		#Se actualiza el historial
		diccionario_historial[usuario]+= "Se realizó un depósito de "+str(deposito_int)+ " pesos el " + str(fecha) + " a las " + str(hora) + " en el cajero " + str(cajero) + "\n"
		
		#Si desea cerrar el programa
		if input("Presione 0 si desea terminar el programa y cualquier otra letra para continuar ")=="0":
			Finalizar()
		#Si desea continuar
		else:
			return volver_al_menu(usuario)
	else:
		continuar= input("Los dígitos introducidos no representan una cantidad de billetes válida, oprima 1 si desea volver a hacer un depósito o cualquier otra tecla para volver al menú principal \n")
		#Si se desea volver a hacer un depósito
		if continuar == "1":
			return depositar_dinero(usuario, cajero) 
		#Se desea volver al menu del usuario
		else:
			return volver_al_menu(usuario)

def depositar_dinero_banquero(usuario, cajero):
	"""
  Cada uno de las siguentes variables reciben la cantidad de billetes por cada denominación respectivamente que el usuario desea ingresar
	"""
	billete_100= input("Digite la cantidad de billetes de 100 pesos que desea introducir:")
	billete_50= input("Digite la cantidad de billetes de 50 pesos que desea introducir:")
	billete_20= input("Digite la cantidad de billetes de 20 pesos que desea introducir:")
	billete_10= input("Digite la cantidad de billetes de 10 pesos que desea introducir:")
	billete_5= input("Digite la cantidad de billetes de 5 pesos que desea introducir:")
	billete_2= input("Digite la cantidad de billetes de 2 pesos que desea introducir:")
	billete_1= input("Digite la cantidad de billetes de 1 pesos que desea introducir:")
	if Es_numero(billete_1,0) and Es_numero(billete_2,0) and Es_numero(billete_5,0) and Es_numero(billete_10,0) and Es_numero(billete_20,0) and Es_numero(billete_20,0) and Es_numero(billete_100,0): 
		deposito = billete_1+"."+billete_2+"."+billete_5+"."+billete_10+"."+billete_20+"."+billete_50+"."+billete_100
		actualizar_cajero_metiendo(cajero, deposito)
		diccionario_saldo[usuario]= str(int(diccionario_saldo[usuario])+ convertir_string_a_dinero(deposito))
		deposito_int= convertir_string_a_dinero(deposito)
		print("Se agregaron exitosamente "+str(deposito_int)+" pesos a su cuenta, ahora posee un total de "+ str(diccionario_saldo[usuario]) + " pesos")
		tiempo= time.strftime('%d-%m-%Y %H horas %M minutos', time.localtime()).split(" ")
		fecha= tiempo[0]
		hora= tiempo[1]
		#Se actualiza el historial
		diccionario_historial[usuario]+= "Se realizó un depósito de "+str(deposito_int)+ " pesos el " + str(fecha) + " a las " + str(hora) + " en el cajero " + str(cajero) + "\n"
		
		#Si desea cerrar el programa
		if input("Presione 0 si desea terminar el programa y cualquier otra letra para continuar ")=="0":
			Finalizar()
		#Si desea continuar
		else:
			return Consola_banquero()
	else:
		continuar= input("Los dígitos introducidos no representan una cantidad de billetes válida, oprima 1 si desea volver a hacer un depósito o cualquier otra tecla para volver al menú principal \n")
		#Si se desea volver a hacer un depósito
		if continuar == "1":
			return depositar_dinero_banquero(usuario, cajero) 
		#Se desea volver al menu del usuario
		else:
			return Consola_banquero()

def Nmb_Cajero(Cajero,contador):
  Cajero_len = len(Cajero)
  if((Cajero_len-1) >= 3):
    if  (90>= ord(Cajero[0]) and ord(Cajero[1]) and ord(Cajero[2]) >= 65):
      contador += 3
      Num_Cajero(Cajero,Cajero_len,contador)

    else:
      print("Nombre de usuario invalido")
      Nmb_Cajero(input("Ingrese nuevamente otro nombre: "),0) 

  else:
    print("Nombre de usuario invalido")
    Nmb_Cajero(input("Ingrese nuevamente otro nombre: "),0) 

def Num_Cajero(Cajero,NmbCajero,x):	 		
	if (NmbCajero != x):
		if (48 <= ord(Cajero[x])<= 57):
			x +=1
			Num_Cajero(Cajero,NmbCajero,x)

		else:
			print("Nombre de usuario invalido")
			Nmb_Cajero(input("Ingrese nuevamente otro nombre: "),0) 
	else:
		print('Creacion de cajero exitosa')

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

#------------
#Esta función despliega las opciones del banquero para poder crear nuevos usuarios y cajeros, además, rellenar los cajeros
def Consola_banquero():	
  desicion= input("Bienvenido banquero \n presione 1 si desea crear un nuevo usuario, 2 si desea crear un nuevo cajero, 3 si desea rellenar de billetes algún cajero: ")

  #Si desicion no es una hilera vacía
  if desicion != "":
    
    #Si el banquero seleccionó 1
    if ord(desicion)==49:
      return crear_usuario()
    
    #Si el banquero seleccionó 2
    elif ord(desicion)==50:
      return crear_cajero()

    #Si el banquero seleccionó 3
    elif ord(desicion)==51:
      #Variable que contiene el nombre de un cajero digitado por el usuario
      cajero= input("Ingrese el nombre del cajero en el que desea retirar su dinero: ")
      
      #Si el cajero digitado por el usuario es un cajero existente
      if cajero in diccionario_cajero:
        return rellenar_cajero(cajero)
    
    else:
    	Finalizar()
  else: 
  	Finalizar()


def crear_usuario():
  #Variable que contiene el nombre de usuario de la cuenta que se desea crear
  posible_usuario= input("Por favor ingrese el nombre de usuario de la cuenta que desea agregar al sistema: ")
  
  #Si el posible nombre de usuario cumple con la expresion regular
  if Aceptar_nombre_usuario(posible_usuario,0,0):
    #Si el nombre de usuario ya existe
    if not(posible_usuario in diccionario_historial):
      
      #Se rellenan los diccionarios
      tiempo= time.strftime('%d-%m-%Y %H horas %M minutos', time.localtime()).split(" ")
      fecha= tiempo[0]
      hora= tiempo[1]
      diccionario_historial[posible_usuario]= "Esta cuenta se creó el "+  fecha + " a las "+ hora + "\n"

      diccionario_clave[posible_usuario]= random.randint(1000, 9999)
      print("La contraseña de esta cuenta va a ser: " +str(diccionario_clave[posible_usuario]))
      
      diccionario_saldo[posible_usuario]= "0"
      print("La cuenta posee un saldo de 0 pesos")
      depositar= input("Si desea realizar un depósito a su cuenta presione 1")
      
      #Si se desea realizar un depósito a la cuenta
      if depositar=="1":
        cajero = input("Ingrese el cajero al que va a realizar la transferencia: ")
        if cajero in diccionario_cajero:
        	return depositar_dinero_banquero(posible_usuario,cajero)
       	else:
        	print("Nombre de cajero incorrecto. Volvera al menu del banquero")
        	Consola_banquero()
      #Si se desea que la cuenta quede sin dinero
      else:
        print("Se regresará al menú del banquero")
        return Consola_banquero()
    #Nombre de usuario ya existe
    else:
        print("Nombre de usuario ya existe. Se regresará al menú para el banquero")
        return Consola_banquero()
  #posible_usuario no cumple con la expresión regular
  else:
    print("Nombre de usuario no válido para su creación debido a que no cumple la expresión regular")
    crear_usuario()


#Crea un nuevo cajero si el nombre de cajero cumple con la expresión regular 
def crear_cajero():

  #Variable que contiene el nombre del cajero que se desea crear
  posible_cajero= input("Por favor ingrese el nombre del cajero que desea agregar al sistema: ")
  
  #Si el posible nombre del cajero cumple con la expresion regular
  if Aceptar_nombre_cajero(posible_cajero,0,0):
    #Si el nombre del cajero ya existe
    if not(posible_cajero in diccionario_cajero):
      
      #Se rellena el diccionarios
      diccionario_cajero[posible_cajero]= "0.0.0.0.0.0.0"
      print("El cajero "+ posible_cajero+ " está vacío, se procede a rellenarlo")
      return rellenar_cajero(posible_cajero)

    #Nombre de usuario ya existe
    else:
        print("Este nombre de cajero ya existe. Se regresará al menú para el banquero")
        return Consola_banquero()
  #posible_cajero no cumple con la expresión regular
  else:
    print("Nombre de cajero no válido para su creación")
    crear_cajero()
    


#Verifica que el nombre para un usuario cumpla con la expresión regular
def Aceptar_nombre_usuario(posible_usuario,exp_regular,contador):  
  terminar = contador== len(posible_usuario)
  if not terminar:  
    if exp_regular == 0:
      if 65<=ord(posible_usuario[contador])<=90 or 97 <= ord(posible_usuario[contador]) <= 122:
        contador+=1
        return Aceptar_nombre_usuario(posible_usuario,exp_regular,contador)
      elif 48<=ord(posible_usuario[contador])<=57:
        exp_regular+=1
        contador+=1
        return Aceptar_nombre_usuario(posible_usuario,exp_regular,contador)
      else:
        return False
    elif exp_regular == 1:
      if 48<=ord(posible_usuario[contador])<=57:
        exp_regular+=1
        contador+=1
        return Aceptar_nombre_usuario(posible_usuario,exp_regular,contador)
      else:
          return False
    elif exp_regular == 2:
      if 48<=ord(posible_usuario[contador])<=57:
        exp_regular+=1
        contador+=1
        return Aceptar_nombre_usuario(posible_usuario,exp_regular,contador)
      else:
        return False
    elif exp_regular == 3:
      if 48<=ord(posible_usuario[contador])<=57:
        exp_regular+=1
        contador+=1
        return Aceptar_nombre_usuario(posible_usuario,exp_regular,contador)
      else:
        return False
    elif exp_regular == 4:
      if ord(posible_usuario[contador])== 33 or ord(posible_usuario[contador])== 35 or ord(posible_usuario[contador])== 36 or ord(posible_usuario[contador])== 38 or ord(posible_usuario[contador])== 63:
        exp_regular+=1
        contador+=1
        return Aceptar_nombre_usuario(posible_usuario,exp_regular,contador)
      else:
        return False
    else:
      return False
  elif len(posible_usuario) > 0 and exp_regular == 5:
    return True
  else:
    return False


#Verifica que el nombre para un cajero cumpla con la expresión regular 
def Aceptar_nombre_cajero(posible_usuario,exp_regular,contador):  
  terminar = contador== len(posible_usuario)
  if not terminar:  
    if exp_regular == 0 or exp_regular == 1 or exp_regular == 2:
      if 65<=ord(posible_usuario[contador])<=90 or 97 <= ord(posible_usuario[contador]) <= 122:
        exp_regular+=1
        contador+=1
        return Aceptar_nombre_cajero(posible_usuario,exp_regular,contador)
      else:
        return False
    elif exp_regular >= 3:
      if 48<=ord(posible_usuario[contador])<=57:
        exp_regular+=1
        contador+=1
        return Aceptar_nombre_cajero(posible_usuario,exp_regular,contador)
      else:
        return False
    else:
      return False
  elif len(posible_usuario) > 0 and exp_regular >= 4:
    return True
  else:
    return False




#Permite ingresar billetes a un cajero existente
def rellenar_cajero(cajero):
  billete_100= input("Digite la cantidad de billetes de 100 pesos que desea introducir:")
  billete_50= input("Digite la cantidad de billetes de 50 pesos que desea introducir:")
  billete_20= input("Digite la cantidad de billetes de 20 pesos que desea introducir:")
  billete_10= input("Digite la cantidad de billetes de 10 pesos que desea introducir:")
  billete_5= input("Digite la cantidad de billetes de 5 pesos que desea introducir:")
  billete_2= input("Digite la cantidad de billetes de 2 pesos que desea introducir:")
  billete_1= input("Digite la cantidad de billetes de 1 pesos que desea introducir:")
  if Es_numero(billete_1,0) and Es_numero(billete_2,0) and Es_numero(billete_5,0) and Es_numero(billete_10,0) and Es_numero(billete_20,0) and Es_numero(billete_20,0) and Es_numero(billete_100,0): 
    deposito = billete_1+"."+billete_2+"."+billete_5+"."+billete_10+"."+billete_20+"."+billete_50+"."+billete_100
    actualizar_cajero_metiendo(cajero, deposito)
    deposito_int= convertir_string_a_dinero(deposito)
    print("Se agregó exitosamente "+str(deposito_int)+" pesos al cajero.")
    print("Se procede a volver al menú del banquero")
    return Consola_banquero()

Inicio()
Finalizar()
