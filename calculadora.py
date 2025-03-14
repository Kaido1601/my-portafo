from main import print_hi


def menu():
    print("CALCULADORA SIMPLE")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")

def calculadora():
    while True:
        menu()
        opcion = input("Ingrese una opcion: ")
        if opcion == '5':
            print("Gracias por usar la calculadora")
            break

        try:
            num1 = float(input("ingrese un numero: "))
            num2 = float(input("ingrese un segundo numero: "))
        except ValueErrors:
            print("Error: Ingrese un numero valido")
            continue

        if opcion == '1':
            print(f"La Suma es:{num1+num2}")
        elif opcion == '2':
            print(f"La Resta es:{num1-num2}")
        elif opcion == '3':
            print(f"La Multiplicacion es:{num1*num2}")
        elif opcion == '4':
            if num2 == 0:
                print("Error: No se puede dividir por cero")
            else:
                print(f"La division es: {num1/num2}")
        else:
            print("Error: Ingrese un opcion valida")

calculadora()