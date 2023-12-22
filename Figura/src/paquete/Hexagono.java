package paquete;


public class Hexagono extends Figura {
    private double lado;

    public Hexagono(String color, double lado) {
        super(color);
        this.lado = lado;
    }

    @Override
    public double perimetro() {
        return 6 * lado;
    }

    @Override
    public double area() {
        return (3 * Math.sqrt(3) * Math.pow(lado, 2)) / 2;
    }}

