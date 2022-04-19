
diccionario_cajero = {"ABC12345":"1.2.5.10.20.50.100"}

def actualizar_cajero_metiendo(cajero, adicion):
  dinero_actual_cajero=diccionario_cajero[cajero].split(".")
  adicion= adicion.split(".")
  print(dinero_actual_cajero)
  billete_1= str(int(dinero_actual_cajero[0])+int(adicion[0]))
  billete_2= str(int(dinero_actual_cajero[1])+int(adicion[1]))
  billete_5= str(int(dinero_actual_cajero[2])+int(adicion[2]))
  billete_10= str(int(dinero_actual_cajero[3])+int(adicion[3]))
  billete_20= str(int(dinero_actual_cajero[4])+int(adicion[4]))
  billete_50= str(int(dinero_actual_cajero[5])+int(adicion[5]))
  billete_100= str(int(dinero_actual_cajero[6])+int(adicion[6]))
  dinero_actualizado_cajero= billete_1+"."+billete_2+"."+billete_5+"."+billete_10+"."+billete_20+"."+billete_50+"."+billete_100
  diccionario_cajero[cajero]= dinero_actualizado_cajero
  return print("Actualizacion exitosa, el cajero cuenta con "+ diccionario_cajero[cajero]) #??? se puede borrar o escribir mejor

actualizar_cajero_metiendo("ABC12345","1.2.43.5.7.6.4")

