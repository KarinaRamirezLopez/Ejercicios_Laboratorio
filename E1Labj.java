p//Dividir dos numeros enteros empleando el metodo de las restas sucesivas
//Calcular la multiplicacion de dos numeros empleando sumas sucesivas 
//Calcular el factorial de un numero a)Es valido emplear la version recursiva, pero ¿Sera la mejor opcion? justifica tu respuesta 

//inicio del programa
import java.util.Scanner;

public class Laboratorio1 {
    // Función para dividir
    public static int dividir(int dividendo, int divisor) {
        int cociente = 0;
        while (dividendo >= divisor) {
            dividendo -= divisor;
            cociente++;
        }
        return cociente;
    }

    // Función para obtener el residuo
    public static int residuo(int dividendo, int divisor) {
        return dividendo;
    }

    // Función para multiplicar
    public static int multiplicar(int a, int b) {
        int resultado = 0;

        // Para hacerlo más eficiente, podemos realizar sumas acumulativas
        for (int i = 0; i < b; i++) {
            resultado += a;
        }

        return resultado;
    }

    // Función para calcular el factorial
    public static long factorial(int n) {
        if (n == 0 || n == 1) {
            return 1; // El factorial de 0 y 1 es 1
        } else {
            return n * factorial(n - 1); // Llamada recursiva para calcular el factorial
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("\t...Ejercicio de Laboratorio 1...");
        System.out.println("°°°Menu°°°");
        System.out.println("1. Dividir dos números enteros empleando el método de las restas sucesivas");
        System.out.println("2. Calcular una multiplicación de dos números empleando sumas sucesivas");
        System.out.println("3. Calcular el factorial de un número");
        System.out.println("0. Salir");
        System.out.print("Ingresa la opción que deseas realizar: ");
        int opcion = scanner.nextInt();

        switch (opcion) {
            case 1: // Dividir dos números enteros empleando el método de las restas sucesivas
                int dividendo, divisor;
                System.out.print("Ingrese el dividendo: ");
                dividendo = scanner.nextInt();
                System.out.print("Ingrese el divisor: ");
                divisor = scanner.nextInt();

                if (divisor == 0) {
                    System.out.println("Ingresa un divisor diferente de cero.");
                } else {
                    int cociente = dividir(dividendo, divisor);
                    int residuo = residuo(dividendo, divisor);

                    System.out.println("Cociente: " + cociente);
                    System.out.println("Residuo: " + residuo);
                }
                break;

            case 2: // Calcular una multiplicación de dos números empleando sumas sucesivas
                int num1, num2;
                int resultado;

                System.out.print("Ingrese un número: ");
                num1 = scanner.nextInt();
                System.out.print("Ingrese un segundo número: ");
                num2 = scanner.nextInt();

                resultado = multiplicar(num1, num2);

                System.out.println("El resultado de la multiplicación es: " + resultado);
                break;

            case 3: // Calcular el factorial de un número
                int numero;

                System.out.print("Ingrese un número del cual desee conocer su factorial: ");
                numero = scanner.nextInt();

                if (numero < 0) {
                    System.out.println("No se puede calcular el factorial de un número negativo.");
                } else {
                    long resultadoFactorial = factorial(numero);
                    System.out.println("El factorial de " + numero + " es " + resultadoFactorial);
                }
                break;

            case 0: // Salir
                System.out.println("Adiós...");
                break;

            default:
                System.out.println("Opción no válida.");
                break;
        }

        scanner.close();
    }
}
