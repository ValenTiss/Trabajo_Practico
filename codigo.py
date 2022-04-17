"""
Autores:Federico Alfaro y Valentin Tissera Doncini
Profesor:Saul Calderon Ramirez
Fecha de entrega: 19 / 04 /22
"""
import sys
import time

diccionario_historial={"valen1234$":"Esta cuenta es predeterminada \n" , "Fede1234#":"Esta cuenta es predeterminada \n"}
diccionario_clave={"valen1234$":"1234", "Fede5432#":"5432"}
diccionario_saldo={"valen1234$":"1412","Fede1234#":"315"}
diccionario_cajero={"ABC12345":"1,2,5,10,20,50,100"}

#Diccionario que asocia los nombres de usuario con las claves
Cuentas_usr = {"valen1234$":100,"Fede1234#":200} #???
Hist_100 ={1:"10001010",2:"00001010"} #???


#La funcion Usuario se utliza para determinar si los caracteres son letras en minuscula o mayuscula.
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

#Verifica que la contraseña ingresada coincida con la contraseña del usuario
def Verifica_password(password_guardado, password_verificando, contador): 
  
  #si el password_verificando es un número de 4 dígitos
  if Es_pin(password_verificando,0):
    tamano = len(password_verificando)-1  #tamaño de password_verificando -1, se utiliza para definir la condición de parada, representa las posiciones de cada caracter de password_verificando 
    digito_actual = password_guardado%10 + 48 #valor ASCII del último dígito de password_guardado
    nuevo_numero = password_guardado //10 #elimina el último dígito de password_wardado, se usa para el llamado recursivo

    #si no se han recorrido todos los numeros de la contraseña
    if password_guardado > 0 and contador <= tamano:
      digito_verificando = ord(password_verificando[tamano-contador]) #valor ASCII de cada caracter del password digitado por el usuario

      #si el cada dígito de la contraseña del usuario es igual al de la contraseña escrita por el usuario
      if digito_actual == digito_verificando:
        contador += 1
        return Verifica_password(nuevo_numero, password_verificando, contador)
      
      #Algún número digitado no coincide con la contraseña guardada en el sistema
      else:
        return False

    #Se verificó exitosamente cada caracter
    else:
      return True 

  #Los caracteres ingresados no representan un número de 4 dígitos
  return False

#Permite el acceso de la cuenta al menú de opciones
def Acceso_cuenta(usuario,password): 
	cuentas = IngresoCuenta()
	
	#Si el nombre de usuario coincide con algún nombre creado anteriormente
	if usuario in cuentas:
		
		#Si la clave es correcta para el usuario seleccionado
		if(Verifica_password(cuentas[usuario],password,0) ):
				print("Datos ingresados correctamente. \n Menú de opciones: \n")
				
				#Se desplegan las opciones del menú para el usuario
				Menu(input("Ingrese si quiere realizar un retiro(0), depositar dinero en su cuenta(1), ver su saldo actual(2) o ver su historial(3): "),usuario)
				
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
				a=0 #???
				#terminar()???
				
				
	#El nombre de usuario introducido no existe
	else:
		#Se pregunta al que corre el programa si desea volver a introducir sus datos o si desea terminar el programa
		opcion = input("Usuario no valido. \n Presione 1 para volver a introducir sus datos o cualquier otra tecla para terminar \n" )
		
		#Si elige 1
		if ord(opcion) == 49:
			
			#Se vuelve a pedir el nombre de usuario y clave
			Solicitar_cuenta()
  
#Pide el nombre de usuario y contraseña al cliente
def Solicitar_cuenta(): 
	
	#Variable que guarda el nombre de usuario introducido por el usuario para acceder a su cuenta
	usuario = input("Digite su nombre de usuario: ")
	
	#Verifica que el nombre de usuario cumpla la expresión regular y sea un usuario existente
	Usuario(usuario,0)

#Inicio del programa, verifica si se desea ingresar al sistema como banquero o como cliente
def Inicio():  

  #Guarda la opción para saber si el usuario desea ingresar como banquero o como usuario
  banquero_o_usuario = input("Bienvenido al Banco ####. \n Si desea ingresar como banquero presione 1 \n Si desea ingresar como cliente presione 2 \n" ) #Tenemos que elegir el nombre del Banco ------------ 

  #Si el usuario ingresa el número 1 por lo que desea ingresar como banquero
  if ord(banquero_o_usuario) == 49:

    #Se solicita la clave del banquero y se guarda en la variable clave_banquero
    clave_banquero = input("Ingrese la clave para poder ingresar como banquero: ") #La clave es SAUL
	
    #Si la clave del banquero es correcta
    if clave_banquero == "SAUL":
    	a=0 
	   #???
      #Despliega las opciones del banquero	
      #Consola_banquero()	
	
    #La clave del banquero se introdujo de manera incorrecta	
    else:
		
      #Se notifica el error		
      print("Intento sospechoso de entrar al sistema, se ha notificado a las autoridades correspondientes.")

  #Si el usuario ingresa el número 1 por lo que desea ingresar como cliente del banco 
  elif ord(banquero_o_usuario) == 50:
    
    #Se le solicitan los datos al usuario 		
    Solicitar_cuenta()

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
	if len(entrada_usuario) != 0: 
		if contador < len(entrada_usuario):
			if 48 <= ord(entrada_usuario[contador]) <= 57 :
				contador+=1
				return Es_numero(entrada_usuario, contador)
			else:
				return False
		else:
			return True
	return False

	
	
def volver_al_menu(usuario):
	decision=input("Si desea hacer un nuevo retiro presione 0, realizar un depósito presione 1, revisar su saldo presione 2 o ver su historial de transacciones presione 3: ")
	if decision!="0":
		if 48 <=ord(decision) <= 51:
			return Menu(decision,usuario)
		else:
			a=0 #???
			#terminar() ???
	else:
		a=0 #???
		#terminar() ???

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
			print("El saldo del usuario \""+usuario_adm+ "\" es de "+ diccionario_saldo[usuario_adm]+" pesos.")
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
			a=0 #???
			#terminar() ???

	#El parámtero desicion es un string vacío
	else: 
		a=0 #???
		#terminar() ???

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
    print("Fondos insuficientes para realizar esta transacción. Para darle el mejor servicio el Banco #### pone a su dispocisión el servicio CRÉDITO EN LA PALMA DE SU MANO, para saber más acerca de este servicio pregunte en la sucursal más cercana")

#Convierte los string que contienen la cantidad de billetes de cada denominación a un entero donde cada denominación está en el fomato "1,2,5,10,20,50,100" donde en este caso cada número representa el valor del billete, sin embargo, en cada casilla se escribe la cantida de billetes
def convertir_string_a_dinero(string):
  lista_billetes= string.split(",") #Lista que contiene la cantidad de billetes por denominación
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
		disminucion_cajero= str(billete_1)+","+str(billete_2)+","+str(billete_5)+","+str(billete_10)+","+str(billete_20)+","+str(billete_50)+","+str(billete_100) #cantidad de billetes de cada denominación que se están retirando 
		disminucion_cajero_int= convertir_string_a_dinero(disminucion_cajero)
		nuevo_saldo= int(diccionario_saldo[usuario]) - disminucion_cajero_int
		diccionario_saldo[usuario]= str(nuevo_saldo)
		print("Transacción realizada con éxito, el saldo en su cuenta ahora es de "+ diccionario_saldo[usuario] +" pesos")
		tiempo= time.strftime('%d-%m-%Y %H:%M', time.localtime()).split(" ")
		fecha= tiempo[0]
		hora= tiempo[1]
		#Se actualiza el historial
		diccionario_historial[usuario]+= "Se realizó un retiro de   "+ str(disminucion_cajero_int) + " pesos el " + fecha + " a las " + hora + " en el cajero " + cajero + "\n"
		actualizar_cajero_sacando(cajero, disminucion_cajero)

		#Si desea cerrar el programa
		if input("Presione 0 si desea terminar el programa y cualquier otra letra para continuar ")=="0":
			return a==0# ???     terminar()
		#Si desea continuar
		else:
			return volver_al_menu(usuario)
		

	else:
		return print("No es posible realizar el retiro en este cajero debido a la falta de billetes necesarios")


def actualizar_cajero_sacando(cajero, disminucion):
  dinero_actual_cajero=diccionario_cajero[cajero].split(",")
  disminucion= disminucion.split(",")
  billete_1= str(int(dinero_actual_cajero[0])-int(disminucion[0]))
  billete_2= str(int(dinero_actual_cajero[1])-int(disminucion[1]))
  billete_5= str(int(dinero_actual_cajero[2])-int(disminucion[2]))
  billete_10= str(int(dinero_actual_cajero[3])-int(disminucion[3]))
  billete_20= str(int(dinero_actual_cajero[4])-int(disminucion[4]))
  billete_50= str(int(dinero_actual_cajero[5])-int(disminucion[5]))
  billete_100= str(int(dinero_actual_cajero[6])-int(disminucion[6]))
  dinero_actualizado_cajero= billete_1+","+billete_2+","+billete_5+","+billete_10+","+billete_20+","+billete_50+","+billete_100
  diccionario_cajero[cajero]= dinero_actualizado_cajero
  return print("Se ha actualizado exitosamente la cantidad de dinero en el cajero, actualmente se posee: "+diccionario_cajero[cajero]) #??? se puede borrar o escribir mejor

#calcula la cantidad de billetes de 100 que se deben y pueden devolver
def devolver_billete_100(monto, dinero_en_cajero):
  """
  Entradas: Monto (int), dinero_en_cajero (string)
  """
  billetes_100_cajero=  int(dinero_en_cajero.split(",")[6]) #cantidad de billetes de 100 en el cajero
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
  billetes_50_cajero=  int(dinero_en_cajero.split(",")[5]) #cantidad de billetes de 50 en el cajero
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
  billetes_20_cajero=  int(dinero_en_cajero.split(",")[4]) #cantidad de billetes de 20 en el cajero
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
  billetes_10_cajero=  int(dinero_en_cajero.split(",")[3]) #cantidad de billetes de 10 en el cajero
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
  billetes_5_cajero=  int(dinero_en_cajero.split(",")[2]) #cantidad de billetes de 5 en el cajero
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
  billetes_2_cajero=  int(dinero_en_cajero.split(",")[1]) #cantidad de billetes de 2 en el cajero
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
  billetes_1_cajero=  int(dinero_en_cajero.split(",")[0]) #cantidad de billetes de 1 en el cajero
  if monto>=1: #si el dinero a retirar es mayor a 1
    billetes_necesarios= monto // 1  # Posible cantidad de billetes de 1 a retirar
    if billetes_necesarios <= billetes_1_cajero: # si la cantidad de posibles billetes 1 a retirar están en el cajero
      return billetes_necesarios
    else:
      return billetes_1_cajero
  else:
    return 0

def actualizar_cajero_metiendo(cajero, adicion):
  dinero_actual_cajero=diccionario_cajero[cajero].split(",")
  adicion= adicion.split(",")
  billete_1= str(int(dinero_actual_cajero[0])+int(adicion[0]))
  billete_2= str(int(dinero_actual_cajero[1])+int(adicion[1]))
  billete_5= str(int(dinero_actual_cajero[2])+int(adicion[2]))
  billete_10= str(int(dinero_actual_cajero[3])+int(adicion[3]))
  billete_20= str(int(dinero_actual_cajero[4])+int(adicion[4]))
  billete_50= str(int(dinero_actual_cajero[5])+int(adicion[5]))
  billete_100= str(int(dinero_actual_cajero[6])+int(adicion[6]))
  dinero_actualizado_cajero= billete_1+","+billete_2+","+billete_5+","+billete_10+","+billete_20+","+billete_50+","+billete_100
  diccionario_cajero[cajero]= dinero_actualizado_cajero
  return print("Actualizacion exitosa, el cajero cuenta con "+ str(diccionario_cajero[cajero])) #??? se puede borrar o escribir mejor



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
		deposito = billete_1+","+billete_2+","+billete_5+","+billete_10+","+billete_20+","+billete_50+","+billete_100
		actualizar_cajero_metiendo(cajero, deposito)
		diccionario_saldo[usuario]= str(int(diccionario_saldo[usuario])+ convertir_string_a_dinero(deposito))
		deposito_int= convertir_string_a_dinero(deposito)
		print("Se agregaron exitosamente "+str(deposito_int)+" pesos a su cuenta, ahora posee un total de "+ str(diccionario_saldo[usuario]) + " pesos")
		tiempo= time.strftime('%d-%m-%Y %H:%M', time.localtime()).split(" ")
		fecha= tiempo[0]
		hora= tiempo[1]
		#Se actualiza el historial
		diccionario_historial[usuario]+= "Se realizó un depósito de "+str(deposito_int)+ " pesos el " + str(fecha) + " a las " + str(hora) + " en el cajero " + cajero + "\n"
		
		#Si desea cerrar el programa
		if input("Presione 0 si desea terminar el programa y cualquier otra letra para continuar ")=="0":
			return a==0# ???     terminar()
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

def IngresoCuenta():
	cuentas = {}
	cuentasArchivo = open("usuarios.txt")
	for line in cuentasArchivo:
		key, value = line.split()
		cuentas[key] = int(value)

	return cuentas	

Solicitar_cuenta()
