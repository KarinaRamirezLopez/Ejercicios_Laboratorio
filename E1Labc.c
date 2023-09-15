//Dividir dos numeros enteros empleando el metodo de las restas sucesivas
//Calcular la multiplicacion de dos numeros empleando sumas sucesivas 
//Calcular el factorial de un numero a)Es valido emplear la version recursiva, pero ¿Sera la mejor opcion? justifica tu respuesta 

//inicio del programa
#include <stdio.h>
#include <stdlib.h> 

//prototipos
int dividir(int, int);
int Residuo(int, int);
int multiplicar(int,int);
long long factorial(int);

int main(){ //Interactua con el usuario
    //variables
    int opcion;
    //menu
    printf("\t...Ejercicio de Laboratorio 1...\n");
    printf("°°°Menu°°°\n");
    printf("1. Dividir dos numeros enteros empleando el metodo de las restas sucesivas\n");
    printf("2. Calcular una multiplicación de dos numeros empleando sumas sucesivas\n");
    printf("3. Calcular el factorial de un numero\n");
    printf("0. Salir\n");
    printf("Ingresa la opción que deseeas realizar: ");
    scanf("%d",&opcion);

    switch (opcion)
    {
    case 1: //Dividir dos numeros enteros empleando el metodo de las restas sucesivas
        int dividendo, divisor;
        printf("Ingrese el dividendo: ");
        scanf("%d", &dividendo);
        printf("Ingrese el divisor: ");
        scanf("%d", &divisor);

        if(divisor == 0){
            printf("Ingresa un numero divisor diferente de cerp.\n");
        } else {
            int cociente = dividir(dividendo, divisor);
            int residuo = Residuo(dividendo, divisor);

            printf("Cociente: %d\n", cociente);
            printf("Residuo: %d\n", residuo);
        }
        break;
    
    case 2: //Calcular una multiplicacion de dos numeros empleando sumas sucesivas
        int num1, num2;
        int resultado;

        printf("Ingrese un numero: ");
        scanf("%d", &num1);
        printf("Ingrese un segundo numero: ");
        scanf("%d", &num2);

        printf("El resultado de la multiplicación es: %d\n", resultado);
        break;

    case 3: //Calcular el factorial de un numero
        int numero;

        printf("Ingrese un numero el cual desee saber su factorial: ");
        scanf("%d", &numero);

        if (numero < 0) {
            printf("No se puede calcular el factorial de un número negativo.\n");
        } else {
            long long resultado = factorial(numero);
            printf("El factorial de %d es %lld\n", numero, resultado);
        }

        break;

    case 0: //Salir 
        printf("Adios...:)");
        break;

    default:
        break;
    }

    return 0;
}

int dividir(int dividendo, int divisor){ //calcula el cociente 
    int cociente = 0;
    while(dividendo >= divisor){
        dividendo -= divisor;
        cociente++;
    }
    return cociente;
}

int Residuo(int dividendo, int divisor){ //Residuo
    return dividendo;
}

int multiplicar(int a, int b) {
    int resultado = 0;

    // Para hacerlo más eficiente, podemos realizar sumas acumulativas
    for (int i = 0; i < b; i++) {
        resultado += a;
    }

    return resultado;
}

long long factorial(int n) {
    if (n == 0 || n == 1) {
        return 1; // El factorial de 0 y 1 es 1
    } else {
        return n * factorial(n - 1); // Llamada recursiva para calcular el factorial
    }
}