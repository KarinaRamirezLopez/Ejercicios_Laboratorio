/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package lab10;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
import java.util.Arrays;

public class Alumno implements Serializable {
    private static final long serialVersionUID = 1L;

    private String nombre;
    private String boleta;
    private String correo;
    private String numero_cel;
    private double[][] calificaciones;

    public Alumno(String nombre, String boleta, String correo, String numero_cel, double[][] calificaciones) {
        this.nombre = nombre;
        this.boleta = boleta;
        this.correo = correo;
        this.numero_cel = numero_cel;
        this.calificaciones = calificaciones;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getBoleta() {
        return boleta;
    }

    public void setBoleta(String boleta) {
        this.boleta = boleta;
    }

    public String getCorreo() {
        return correo;
    }

    public void setCorreo(String correo) {
        this.correo = correo;
    }

    public String getNumeroCel() {
        return numero_cel;
    }

    public void setNumeroCel(String numero_cel) {
        this.numero_cel = numero_cel;
    }

    public double[][] getCalificaciones() {
        return calificaciones;
    }

    public void setCalificaciones(double[][] calificaciones) {
        this.calificaciones = calificaciones;
    }

    public void exportarTexto(String nombreArchivo) {
        try (ObjectOutputStream salida = new ObjectOutputStream(new FileOutputStream(nombreArchivo))) {
            salida.writeObject(this);
            System.out.println("Datos exportados exitosamente a " + nombreArchivo);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void importarTexto(String nombreArchivo) {
        try (ObjectInputStream entrada = new ObjectInputStream(new FileInputStream(nombreArchivo))) {
            Alumno alumno = (Alumno) entrada.readObject();
            System.out.println("Datos recuperados exitosamente desde " + nombreArchivo);
            System.out.println("Nombre: " + alumno.getNombre());
            System.out.println("Boleta: " + alumno.getBoleta());
            System.out.println("Correo Electrónico: " + alumno.getCorreo());
            System.out.println("Número Celular: " + alumno.getNumeroCel());
            System.out.println("Calificaciones: " + Arrays.deepToString(alumno.getCalificaciones()));
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        double[][] calificaciones1 = {{101, 8.5}, {102, 9.0}, {103, 7.5}};
        double[][] calificaciones2 = {{101, 7.0}, {102, 8.0}, {103, 6.5}};
        double[][] calificaciones3 = {{101, 9.0}, {102, 8.5}, {103, 8.0}};

        Alumno alumno1 = new Alumno("Juan Pérez", "2CV5", "juan@ejemplo.com", "1234567890", calificaciones1);
        Alumno alumno2 = new Alumno("Karina Ramirez", "3CV2", "karmirez@ipn.com", "9876543210", calificaciones2);
        Alumno alumno3 = new Alumno("Carlos López", "4CV7", "carlos@ejemplo.com", "5678901234", calificaciones3);

        alumno1.exportarTexto("alumno1.txt");
        alumno2.exportarTexto("alumno2.txt");
        alumno3.exportarTexto("alumno3.txt");

        Alumno.importarTexto("alumno1.txt");
        Alumno.importarTexto("alumno2.txt");
        Alumno.importarTexto("alumno3.txt");
    }
}

