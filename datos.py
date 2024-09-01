Datos_Basicos = {"nombres": "Juan Carlos",
                 "apellido": "Perez Garcia",
                 "DUI": "022131236-2",
                 "fecha de nacimiento": "11/2/1999",
                 "lugar de nacimiento": "soya city",
                 "nacionalidad": "salvadoreña",
                 "estado civil": "complicado",
                 }

print("\n Detalle del diccionario")
print("=====================================")

print("\nClaves del diccionario: ", Datos_Basicos.keys())
print("\nValores del diccionario: ", Datos_Basicos.values())
print("\nElementos del diccionario: ", Datos_Basicos.items())

#ejemplos practico de los deccionario
print("\nInscripcion del curso")
print("=================================")

print("\nDatos del participante")
print("===============================")

print("DUI:", Datos_Basicos["DUI"])
print("Nombre completo: ",Datos_Basicos["nombres"]+" "+Datos_Basicos["apellido"])
