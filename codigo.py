"""
Autores:
Profesor:
Fecha de entrega
"""
import sys

def Usuario(entrada,x):
	entrada_len = len(entrada)
	if(x < entrada_len):
		if ( 90>= ord(entrada[x]) >= 65 or 122>= ord(entrada[x]) >= 97):
			x +=1
			Usuario(entrada,x)

		elif (48 <= (ord(entrada[x])) <= 57):

			Exp_Num(entrada,x,0)

		else:
			print("No entro")

	else:
		print("Usuario no valido.")
		Usuario(input("Ingrese su usuario: "), 0 )


def Exp_Num(Num,x,n):
	entrada_largo =len(Num)
	ult_entrada = entrada_largo-4
	if (n < 2):
		if (48 <= (ord(Num[x])) <= 57):
			x +=1
			n +=1
			entrada_largo -=1
			Exp_Num(Num,x,n)

		else:
			print("Usuario no valido.")
			Usuario(input("\nIngrese su nombre de usuario:"),0)

	if n == 2:
		if (33<= (ord(Num[x])) >=38 or (ord(Num[x])) == 63 ): 
			print("Entrada exitosa.")
			n +=1
			Menu

		else:
			print("Usuario no valido.")
			Usuario(input("\nIngrese su nombre de usuario:"),0)

	elif n > 2:
		print("Usuario no valido.")
		Usuario(input("\nIngrese su nombre de usuario:"),0)
		
		
		
		
cuentas = {"$VALEN":1234,"!JUANI":5432} #Debe ser una variable global


def Es_pin(entrada_usuario, contador): #Sirve para verificar si la hilera son 4 números
  if len(entrada_usuario) == 4: 
    if contador < 5:
      if 48 <= ord(entrada_usuario[contador-1]) and ord(entrada_usuario[contador-1]) <= 57 :
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
  

def Solicitar_cuenta():
	usuario = input("Digite su nombre de usuario: ")
	password = input("Digite la contraseña: ")
	Acceso_cuenta(usuario,password)


Solicitar_cuenta()

def Menu():
	print("Bienvenido.")

	
Usuario(input("Ingrese su usuario: "), 0 )
