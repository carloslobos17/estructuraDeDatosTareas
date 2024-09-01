temperaturas = []
print(" por favor ingrese 10 temperaturas:")

for i in range(10):

    temperatura = float(input(f"temperaturas {i + 1}:"))
    temperaturas.append(temperatura)

promedio = sum(temperaturas) / len(temperaturas)
print(f"\nel promedio de las temperaturas es {promedio:.2f}")

while True:
    opcion = input("\n¿ver alguna temperatura especifica? (si/no): ").strip().lower()

    if opcion == "si":
        posicion = int(input("ingrese una posicion (1-10) de la temperatura que desear ver "))
        if 1 <= posicion <= 10:
            print(f"la temperatuta en la posicion {posicion} es: {temperaturas[posicion -1]:.2f}")
        else:
            print("posicon fuera de rango. por favor, ingrese un numero entre 1 y 10")

    elif opcion == "no":
        print("Cierre del programa.")
        break
    else:
        print("por favor, ingrese 'si' o 'no'.")