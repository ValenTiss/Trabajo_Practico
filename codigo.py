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
					Menu()

				if (n>2):
					print("Usuario no valido.")
					Usuario(input("\nIngrese su nombre de usuario:"),0)


			else:
				print("Usuario no valido.")
				Usuario(input("\nIngrese su nombre de usuario:"),0)
	else:
		print("Usuario no valido.")
		Usuario(input("\nIngrese su nombre de usuario:"),0)


def Menu():
	print("Bienvenido.")

	
Usuario(input("Ingrese su usuario: "), 0 )