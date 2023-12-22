package paquete;

public class Principal {

    public static void imprimirInformacion(Figura figura) {
        System.out.println("Figura de color " + figura.getColor() + ":");
        System.out.println("Perímetro: " + figura.perimetro());
        System.out.println("Área: " + figura.area());
        System.out.println();
    }

    public static void main(String[] args) {
        // Crear instancias de las clases
        Triangulo triangulo = new Triangulo("Rojo", 3, 4, 5);
        Circulo circulo = new Circulo("Azul", 2);
        Rectangulo rectangulo = new Rectangulo("Verde", 4, 6);
        Hexagono hexagono = new Hexagono("Amarillo", 5);

        // Usar polimorfismo para imprimir información de cada figura
        imprimirInformacion(triangulo);
        imprimirInformacion(circulo);
        imprimirInformacion(rectangulo);
        imprimirInformacion(hexagono);
    }
}



