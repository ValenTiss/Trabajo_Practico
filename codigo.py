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
<<<<<<< Updated upstream
				n +=1
=======
				n +=1		
>>>>>>> Stashed changes
				Exp_Num(Num,x,n)
				#El usuario fue aceptado pasa a la funcion Es_pin 
				if (n == 2):
<<<<<<< Updated upstream
					Acceso_cuenta(Num,input("Ingrese su contraseña: "))
=======
					Es_pin(Num,0)
>>>>>>> Stashed changes

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
		
		
		
		
<<<<<<< Updated upstream
cuentas = {"valen1234$":1234,"Fede5432#":5432} #Debe ser una variable global
=======
cuentas = {"valen1234$":1234,"Fede1234#":5432} #Debe ser una variable global
>>>>>>> Stashed changes


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
<<<<<<< Updated upstream
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


Solicitar_cuenta()
=======
	password = input("Digite la contraseña: ")
	Acceso_cuenta(usuario,password)


Cuentas_usr = {"valen1234$":100,"Fede1234#":200}
Hist_100 ={1:"10001010",2:"00001010"}



def Menu(decision,usuario_adm):
	if int(decision) == 1:
		cajero_loc = input("Ingrese la localización de su cajero: ")

	if int(decision) == 0:
		#Historial(usuario_adm,0)


"""def Historial(cuenta_his,n):
	cuenta_Xusr = Cuentas_usr[cuenta_his]
	 cuenta_Xusr =Hist_100

	if (n <= 4):
		print(Hist_str(cuenta_Xusr)[n+1])
		Historial(cuenta_his,n)"""





Solicitar_cuenta()


>>>>>>> Stashed changes
