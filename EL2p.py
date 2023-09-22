"""
    Ejercicio de Laboratorio 2
    Ramirez López Karina
"""

while True:
    print("...Ejercicio de Laboratorio 2")
    print("1.Convertir una cadena de caracteres a mayusculas")
    print("2.Calcular el cubo de un numero")
    print("3.Resolver una ecuación de segundo grado")
    print("0. Salir")

    opcion = input("Elije una opcion: ")

    if opcion == "1":
        try:
            def convertir_mayus_n(cadena):# Función normal
                return cadena.upper()

            convertir_mayus_l = lambda cadena: cadena. upper()

            cadena = input("Ingrese una cadena de caracteres: ")

            resultado_n = convertir_mayus_n(cadena)
            print("Resultado (Función normal): ", resultado_n)

            resultado_l = convertir_mayus_l(cadena)
            print("Resultado (Función lambda): ", resultado_l)
        
        except ValueError:
            print("Ingrese una cadena válida:)")

    elif opcion == "2":
        try:
            def cubo_n(x):
                return x ** 3

            cubo_l = lambda x: x ** 3

            x = float(input("Ingrese un número: "))

            resultadoc_n = cubo_n(x)
            print("Resultado (Funcion normal): ", resultadoc_n)

            resultadoc_l = cubo_l(x)
            print("Resultado (Funcion lambda): ", resultadoc_l)

        except ValueError:
            print("Ingrese un número válido:)")

    elif opcion == "3":
        try:
            ecu = lambda a, b, c: ((-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a) if (b ** 2 - 4 * a * c) >= 0 else None,
            (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a) if (b ** 2 - 4 * a * c) >= 0 else None)
        

            print("Ingresa los valores")
            
            a = float(input("Ingresa el valor de a: "))
            b = float(input("Ingresa el valor de b: "))
            c = float(input("Ingresa el valor de c: "))
            
            discriminante = b ** 2 - 4 * a * c
            
            if discriminante < 0:
                print("No existe una solución")
            else:
                solucion1 = (-b + discriminante ** 0.5) / (2 * a)
                solucion2 = (-b - discriminante ** 0.5) / (2 * a)
    
                print("Las soluciones son (Función normal):", solucion1, "y", solucion2)
                
                soluciones_lambda = ecu(a, b, c)
                if None in soluciones_lambda:
                    print("Las soluciones (Función lambda) no son válidas.")
                else:
                    print("Las soluciones (Función lambda):", soluciones_lambda)
                
        except ValueError:
            print("Ingrese números válidos.")


    elif opcion == "0":
        print("Baiii...")
        break

    else:
        print("Ingrese una opción válida:)")


