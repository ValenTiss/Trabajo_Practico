import sys

def Usuario(i = 1):
	username = input("Ingrese su usuario: ")
	username_len = len(username)

	if username_len == 6:
		Verificador(username,0)
		i +=1 

	else:
		print("Usuario no valido.")
		Usuario()


def Verificador(usuario_1,x):
	n =0
	if x <= 4:

		if (65<=(ord(usuario_1[n]))<=90 or 97<= (ord(usuario_1[n]))<= 122):
			n +=1
			x +=1 
			Verificador(usuario_1,x)

			
		else :
			print("Usuario no valido.")
			Usuario()


	elif x <6 and x>4:
		if (65<=(ord(usuario_1[n]))<=90 or 97<= (ord(usuario_1[n]))<= 122):
			n +=1
			x +=1 
			Verificador(usuario_1,x)

			
		else :
			print("Usuario no valido.")
			Usuario()

	elif x == 6:
			
		if (65<=(ord(usuario_1[n]))<=90 or 97<= (ord(usuario_1[n]))<= 122):
			n +=1
			x +=1 
			Verificador(usuario_1,x)

			
		else :
			print("Usuario no valido.")
			Usuario()

	elif x == 7 :
		Cuenta_pass(input("Ingrese su contraseña: "),usuario_1)


def Cuenta_pass(password,username):

	cuentas = {"$VALEN":"1234","!JUANI":"5432"}

	if len(password) == 4:
		if username in cuentas:
			if(cuentas[username] == str(password) ):
					print("Estas adentro de tu cuenta")
					Menu(input("Ingrese si quiere realizar una transaccion(1) o ver su historial(0): "),username)

			else:
				Cuenta_pass(input("Ingrese su contraseña"),username)

		else:
			print("Usuario no valido. ")
			Cuenta_usr(input("Ingrese su username: "))

def Verificador_pass(usuario_1,x):
	n =0
	if x <=6:

		if (65<=(ord(usuario_1[n]))<=90 or 33<= (ord(usuario_1[n]))<= 47 or 97<= (ord(usuario_1[n]))<= 122):
			n +=1
			x +=1 
			Verificador(usuario_1,x)

			
		else :
			print("Usuario no valido.")
			Usuario()

	elif x == 7 :
		Cuenta_pass(input("Ingrese su contraseña: "),usuario_1)
	
def Menu(transacciones,username):
	if(int(transacciones) == 1 ):
		Transaccion(input("Ingrese el tipo de transaccion que desea realizar deposito(D) o retiro(E):" ),username)	





def Transaccion(tipo,username):

	cuentas_mnt ={"$VALEN" :8500} 

	if(tipo == "D"):
		print("Su cuenta  tiene $"+str(cuentas_mnt[username]))
		monto =input("Ingrese el monto deseado: $")
		if (int(monto) > cuentas_mnt[username]):
			print("Monto no aceptable.")
			Transaccion("D",username)

		else: 
			
	else :
		print("Su cuenta  tiene $"+str(cuentas_mnt[username]))
		monto =input("Ingrese el monto deseado: ")
		if (int(monto) > cuentas_mnt[username]):
			print("Monto no aceptable.")
			Transaccion("D",username)




Usuario()

