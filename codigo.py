import sys

def Usuario(entrada,x = 1):
	if  (65 >=entrada[x]<= 90 or 97 >=entrada[x]<= 122 ):
		x +=1
		Usuario(entrada)

	elif (48 >=entrada[x]<= 57):
		x +=1
		Exp_Num(entrada,x)

	else:
		print("Usuario no valido")
		Usuario(input("\nIngrese su nombre de usuario:"))


def Exp_Num(entrada,x):
	entrada_largo =len(entrada)

	if (48 >=entrada[x]<= 57):
		Exp_Num(entrada)

	if entrada_largo == x:
		if(entrada[x]>) 


Usuario(input("Ingrese su nombre de usuario: "))