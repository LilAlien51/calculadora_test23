def introducirNumeros():
    numero1 = int(input("Introduzca el primer número: "))
    numero2 = int(input("Introduzca el segundo número: "))
    return numero1, numero2

def sumar(a, b):
    print("La suma de", a, "+", b, "=", a + b)

def restar(a, b):
    print("La resta de", a, "-", b, "=", a - b)

def multiplicacion(a, b):
    print("La multiplicación de", a, "x", b, "=", a * b)

def division(a, b):
    print("La división de", a, "/", b, "=", a / b)

def calculadora():
    while True:
        print("""
        Indique la operación a realizar:
        1) Sumar
        2) Restar
        3) Multiplicar
        4) Dividir
        5) Salir de la calculadora
        """)

        eleccion = int(input("Seleccione una opción: "))

        if eleccion in [1, 2, 3, 4]:
            numero1, numero2 = introducirNumeros()

            if eleccion == 1:
                sumar(numero1, numero2)
            elif eleccion == 2:
                restar(numero1, numero2)
            elif eleccion == 3:
                multiplicacion(numero1, numero2)
            elif eleccion == 4:
                division(numero1, numero2)
        elif eleccion == 5:
            print("Hasta Pronto")
            break
        else:
            print("Opción no válida, por favor elija una opción del 1 al 5")
            
            
calculadora()

