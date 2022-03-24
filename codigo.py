"""
Autores:
Profesor:
Fecha de entrega
"""
import sys

def Usuario(entrada,x):
	entrada_len = len(entrada)
	if(x < entrada_len):
		if ( 90>= ord(entrada[x]) >= 65 or 122>= ord(entrada[x]) >= 97 ):
			x +=1
			Usuario(entrada,x)

		elif (48 <= (ord(entrada[x])) <= 57):
			Exp_Num(entrada,x,0)

		else:
			print("Usuario no valido.")
			Usuario(input("Ingrese su usuario: "), 0 )

	else:
		print("Usuario no valido.")
		Usuario(input("Ingrese su usuario: "), 0 )


def Exp_Num(Num,x,n):
	entrada_largo =len(Num)

	if(38>=ord(Num[entrada_largo-1])>=33 or ord(Num[entrada_largo-1]) == 63):
		if (n<2):
			if (48 <= (ord(Num[x])) <= 57):
				x +=1
				n +=1
					
				Exp_Num(Num,x,n)
				if (n == 2):
					Exs_Cuenta(Num,0)

				if (n>2):
					print("Usuario no valido.")
					Usuario(input("\nIngrese su nombre de usuario:"),0)


			else:
				print("Usuario no valido.")
				Usuario(input("\nIngrese su nombre de usuario:"),0)
	else:
		print("Usuario no valido.")
		Usuario(input("\nIngrese su nombre de usuario:"),0)
		
		
		
		
cuentas = {"$VALEN":1234,"!JUANI":5432} #Debe ser una variable global


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
				#Menu(input("Ingrese si quiere realizar una transaccion(1) o ver su historial(0): "),usuario)
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
	password = input("Digite la contraseña: ")
	Acceso_cuenta(usuario,password)

def Inicio():  #Inicio del programa, verifica si se desea ingresar al sistema como banquero o como cliente
  banquero_o_usuario = input("Bienvenido al Banco ####. \n Si desea ingresar como banquero presione 1 \n Si desea ingresar como cliente presione 2 \n" ) #Tenemos que elegir el nombre del Banco ------------ 
  if ord(banquero_o_usuario) == 49:
    clave_banquero = input("Ingrese la clave para poder ingresar como banquero: ") #La clave es SAUL
    if clave_banquero == "SAUL":
      #Consola_banquero()
    else:
      print("Intento sospechoso de entrar al sistema, se ha notificado a las entidades correspondientes.")
  elif ord(banquero_o_usuario) == 50:
    Solicitar_cuenta()



def Exs_Cuenta(Usuario,n):
	cuentas ={"valen1234$": "4321"}
	if(ord(cuentas[Usuario][n] ) == ord(Usuario[n])):
		n +=1
		Exs_Cuenta(Usuario,n)

	else:
		print("Usuario inexistente.")
		Usuario(input("\nIngrese su nombre de usuario:"),0)

	

	
Usuario(input("Ingrese su usuario: "), 0 )
