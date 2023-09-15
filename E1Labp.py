//Dividir dos numeros enteros empleando el metodo de las restas sucesivas
//Calcular la multiplicacion de dos numeros empleando sumas sucesivas 
//Calcular el factorial de un numero a)Es valido emplear la version recursiva, pero ¿Sera la mejor opcion? justifica tu respuesta 

//inicio del programa
# Función para dividir
def dividir(dividendo, divisor):
    cociente = 0
    while dividendo >= divisor:
        dividendo -= divisor
        cociente += 1
    return cociente

# Función para obtener el residuo
def residuo(dividendo, divisor):
    return dividendo

# Función para multiplicar
def multiplicar(a, b):
    resultado = 0
    for i in range(b):
        resultado += a
    return resultado

# Función para calcular el factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Función principal
def main():
    print("\t...Ejercicio de Laboratorio 1...")
    print("°°°Menu°°°")
    print("1. Dividir dos números enteros empleando el método de las restas sucesivas")
    print("2. Calcular una multiplicación de dos números empleando sumas sucesivas")
    print("3. Calcular el factorial de un número")
    print("0. Salir")
    
    opcion = int(input("Ingresa la opción que deseas realizar: "))

    if opcion == 1:
        dividendo = int(input("Ingrese el dividendo: "))
        divisor = int(input("Ingrese el divisor: "))

        if divisor == 0:
            print("Ingresa un divisor diferente de cero.")
        else:
            cociente = dividir(dividendo, divisor)
            residuo_valor = residuo(dividendo, divisor)

            print("Cociente:", cociente)
            print("Residuo:", residuo_valor)
    
    elif opcion == 2:
        num1 = int(input("Ingrese un número: "))
        num2 = int(input("Ingrese un segundo número: "))
        resultado = multiplicar(num1, num2)
        print("El resultado de la multiplicación es:", resultado)
    
    elif opcion == 3:
        numero = int(input("Ingrese un número del cual desea conocer su factorial: "))
        if numero < 0:
            print("No se puede calcular el factorial de un número negativo.")
        else:
            resultado_factorial = factorial(numero)
            print(f"El factorial de {numero} es {resultado_factorial}")
    
    elif opcion == 0:
        print("Adiós...")

    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
