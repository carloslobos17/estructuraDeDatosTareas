while True :
   pregunta = input("Inserte el numero del servicio que necesita \n1. Consulta de notas \n2. Consulta de precios \n3. Horarios de atencion \n4. Adios \n>>").strip().lower()

   if pregunta == "1":
      print("Su promedio de notas es 8.0 ")

   elif pregunta == "2":
      print("El precio de matricula es $110")

   elif pregunta == "3":
      print("De 8am a 4pm")

   elif pregunta == "4":
      print("Hasta luego")
      break

else:
   print("por favor, ingrese un numero")


