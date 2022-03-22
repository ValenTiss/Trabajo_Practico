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

def Menu():
	print("Bienvenido.")

	
Usuario(input("Ingrese su usuario: "), 0 )