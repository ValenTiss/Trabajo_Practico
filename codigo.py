"""
Autores:Federico Alfaro y Valentin Tissera Doncini
Profesor:Saul Calderon Ramirez
Fecha de entrega: 19 / 04 /22
"""
import sys

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
	if(38>=ord(Num[entrada_largo-1])>=33 or ord(Num[entrada_largo-1]) == 63):
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
		
		
		
		

cuentas = {"valen1234$":1234,"Fede5432#":5432} #Debe ser una variable global


def Es_pin(entrada_usuario, contador): 
  if len(entrada_usuario) == 4: 
    if contador < 4:
      if 48 <= ord(entrada_usuario[contador]) and ord(entrada_usuario[contador]) <= 57 :
        contador+=1
        return True and Es_pin(entrada_usuario, contador)
      else:
        return False
    else:
      return True
  return False

def Verifica_password(password_guardado, password_verificando, contador): #Verifica que la contraseña ingresada coincida con la contraseña del usuario
  if Es_pin(password_verificando,0):
    tamano = len(password_verificando)-1
    digito_actual = password_guardado%10 + 48
    nuevo_numero = password_guardado //10

    if password_guardado > 0 and contador <= tamano:
      digito_verificando = ord(password_verificando[tamano-contador])

      if digito_actual == digito_verificando:
        contador += 1
        return True and  Verifica_password(nuevo_numero, password_verificando, contador)
      
      else:
        return False
    
    else:
      return True 
  return False


def Acceso_cuenta(usuario,password): #Permite el acceso de la cuenta al menú de opciones
	if usuario in cuentas:
		if(Verifica_password(cuentas[usuario],password,0) ):
				print("Datos ingresados correctamente. \n Menú de opciones: \n")
				Menu(input("Ingrese si quiere realizar un retiro(1) o ver su historial(0): "),usuario)
		else:
			terminar= input("Presione 1 para volver a introducir su contraseña o cualquier otra tecla para terminar \n")	 		
			if ord(terminar) == 49:
				Acceso_cuenta(usuario , input("Contraseña incorrecta \n Ingrese su contraseña nuevamente: "))
	else:
		opcion = input("Usuario no valido. \n Presione 1 para volver a introducir sus datos o cualquier otra tecla para terminar \n" )
		if ord(opcion) == 49:
			Solicitar_cuenta()
  

def Solicitar_cuenta(): #Pide el nombre de usuario y contraseña al cliente
	usuario = input("Digite su nombre de usuario: ")

	Usuario(usuario,0)

def Inicio():  #Inicio del programa, verifica si se desea ingresar al sistema como banquero o como cliente
  banquero_o_usuario = input("Bienvenido al Banco ####. \n Si desea ingresar como banquero presione 1 \n Si desea ingresar como cliente presione 2 \n" ) #Tenemos que elegir el nombre del Banco ------------ 
  if ord(banquero_o_usuario) == 49:
    clave_banquero = input("Ingrese la clave para poder ingresar como banquero: ") #La clave es SAUL
    if clave_banquero == "SAUL":
    	a=0
      #Consola_banquero()	
    else:
      print("Intento sospechoso de entrar al sistema, se ha notificado a las entidades correspondientes.")

  elif ord(banquero_o_usuario) == 50:
    Solicitar_cuenta()


def Solicitar_cuenta():
	nmb_usr = input("Digite la cuenta: ")
	Usuario(nmb_usr,0)


Cuentas_usr = {"valen1234$":100,"Fede1234#":200}
Hist_100 ={1:"10001010",2:"00001010"}



def Menu(decision,usuario_adm):
	if int(decision) == 1:
		cajero_loc = input("Ingrese la localización de su cajero: ")

	if int(decision) == 0:
		a=0
		#Historial(usuario_adm,0)



#def Historial(cuenta_his,n):
#	cuenta_Xusr = Cuentas_usr[cuenta_his]
#	cuenta_Xusr =Hist_100
#
#	if (n <= 4):
#		print(Hist_str(cuenta_Xusr)[n+1])
#		Historial(cuenta_his,n)


def Aceptar_nombre_usuario(posible_usuario,exp_regular,contador):  #Verifica que el nombre para un usuario cumpla con la expresión regular
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

def Aceptar_nombre_cajero(posible_usuario,exp_regular,contador):  #Verifica que el nombre para un cajero cumpla con la expresión regular
  terminar = contador== len(posible_usuario)
  if not terminar:  
    if exp_regular == 0:
      if 65<=ord(posible_usuario[contador])<=90 or 97 <= ord(posible_usuario[contador]) <= 122:
        exp_regular+=1
        contador+=1
        return Aceptar_nombre_cajero(posible_usuario,exp_regular,contador)
      else:
        return False
    elif exp_regular == 1:
      if 65<=ord(posible_usuario[contador])<=90 or 97 <= ord(posible_usuario[contador]) <= 122:
        exp_regular+=1
        contador+=1
        return Aceptar_nombre_cajero(posible_usuario,exp_regular,contador)
      else:
          return False
    elif exp_regular == 2:
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

Solicitar_cuenta()

#--------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Función que se encarga de verificar que el monto en la cuenta del usuario tenga el monto que desea retirar y llama a otras funciones para encargarse del proceso de retirar dinero de la cuenta del usuario y descontar los billetes de los cajeros
"""
def retirar_dinero(monto, dinero_del_usuario, dinero_en_cajero):
  """
  Entradas: Monto (número natural), dinero_del_usuario (int), dinero_cajero (string)
  Los valores deben estar verificados cuando entran como parámetros
  """
  dinero_en_cajero_int= convertir_string_a_dinero(dinero_en_cajero) # dinero total del cajero en int
  if monto <= dinero_del_usuario: #verifica si el usuario tiene el monto en su cuenta
    if monto  <= dinero_en_cajero_int: #verifica si el cajero tiene el monto ingresado disponible para retirar
      retirar_dinero_del_cajero(monto, dinero_en_cajero) #Se llama a la función que elige la menor cantidad de billetes para devolver 
      #------------actualizar historial -------  volver al menú principal
    else: 
      print("Dinero no disponible en este cajero, por favor desplácese a otro cajero o vuelva en unos días cuando se llenen las reservas")
  else:
    print("Fondos insuficientes para realizar esta transacción. Para darle el mejor servicio el Banco #### pone a su dispocisión el servicio CRÉDITO EN LA PALMA DE SU MANO, para saber más acerca de este servicio pregunte en la sucursal más cercana")

#Convierte los string que contienen la cantidad de billetes de cada denominación a un entero donde cada denominación está en el fomato "1,2,5,10,20,50,100" donde en este caso cada número representa el valor del billete, sin embargo, en cada casilla se escribe la cantida de billetes
def convertir_string_a_dinero(string):
  lista_billetes= string.split(",") #Lista que contiene la cantidad de billetes por denominación
  return int(lista_billetes[0]) + int(lista_billetes[1])*2 + int(lista_billetes[2])*5 + int(lista_billetes[3])*10 + int(lista_billetes[4])*20 + int(lista_billetes[5])*50 + int(lista_billetes[6])*100

#Se encarga de devolver la menor cantidad de billetes, actualiza la cantidad de billetes en el cajero  y dinero disponible del usuario
def retirar_dinero_del_cajero(monto, dinero_en_cajero):
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
    #------ actualizar la cantidad de billetes en el cajero  y dinero disponible del usuario
    print(monto)
    print(str(billete_1)+","+str(billete_2)+","+str(billete_5)+","+str(billete_10)+","+str(billete_20)+","+str(billete_50)+","+str(billete_100)) #cantidad de billetes de cada denominación que se están retirando 
    return print("Transacción realizada con éxito, reciba su dinero")
  else:
    print("No es posible realizar el retiro en este cajero debido a la falta de billetes necesarios")

#calcula la cantidad de billetes de 100 que se deben y pueden devolver
def devolver_billete_100(monto, dinero_en_cajero):
  """
  Entradas: Monto (int), dinero_en_cajero (string)
  """
  billetes_100_cajero=  int(dinero_en_cajero.split(",")[6]) #cantidad de billetes de 100 en el cajero
  if monto>100: #si el dinero a retirar es mayor a 100
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
  if monto>50: #si el dinero a retirar es mayor a 50
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
  if monto>20: #si el dinero a retirar es mayor a 20
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
  if monto>10: #si el dinero a retirar es mayor a 10
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
  if monto>5: #si el dinero a retirar es mayor a 5
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
  if monto>2: #si el dinero a retirar es mayor a 2
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
  if monto>1: #si el dinero a retirar es mayor a 1
    billetes_necesarios= monto // 1  # Posible cantidad de billetes de 1 a retirar
    if billetes_necesarios <= billetes_1_cajero: # si la cantidad de posibles billetes 1 a retirar están en el cajero
      return billetes_necesarios
    else:
      return billetes_1_cajero
  else:
    return 0



monto= 4
dinero_del_usuario= 3
dinero_en_cajero= "1,1,1,1,1,1,1"
retirar_dinero(monto, dinero_del_usuario, dinero_en_cajero)
