import pickle
import os

class Alumno:
    def __init__(self, nombre, boleta, correo, numero_cel, calificaciones):
        self.nombre = nombre
        self.boleta = boleta
        self.correo = correo
        self.numero_cel = numero_cel
        self.calificaciones = calificaciones

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_boleta(self):
        return self.boleta

    def set_boleta(self, boleta):
        self.boleta = boleta

    def get_correo(self):
        return self.correo

    def set_correo(self, correo):
        self.correo = correo

    def get_numero_cel(self):
        return self.numero_cel

    def set_numero_cel(self, numero_cel):
        self.numero_cel = numero_cel

    def get_calificaciones(self):
        return self.calificaciones

    def set_calificaciones(self, calificaciones):
        self.calificaciones = calificaciones

    def exportar_texto(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'wb') as salida:
                pickle.dump(self, salida)
                print(f'Datos exportados exitosamente a {nombre_archivo}')
        except IOError as e:
            print(e)

    @staticmethod
    def importar_texto(nombre_archivo):
        try:
            with open(nombre_archivo, 'rb') as entrada:
                alumno = pickle.load(entrada)
                print(f'Datos recuperados exitosamente desde {nombre_archivo}')
                print(f'Nombre: {alumno.get_nombre()}')
                print(f'Boleta: {alumno.get_boleta()}')
                print(f'Correo Electrónico: {alumno.get_correo()}')
                print(f'Número Celular: {alumno.get_numero_cel()}')
                print(f'Calificaciones: {alumno.get_calificaciones()}')
        except IOError as e:
            print(e)

if __name__ == "__main__":
    calificaciones1 = [[101, 8.5], [102, 9.0], [103, 7.5]]
    calificaciones2 = [[101, 7.0], [102, 8.0], [103, 6.5]]
    calificaciones3 = [[101, 9.0], [102, 8.5], [103, 8.0]]

    alumno1 = Alumno("Juan Pérez", "2CV5", "juan@ejemplo.com", "1234567890", calificaciones1)
    alumno2 = Alumno("Karina Ramirez", "3CV2", "karmirez@ipn.com", "9876543210", calificaciones2)
    alumno3 = Alumno("Carlos López", "4CV7", "carlos@ejemplo.com", "5678901234", calificaciones3)

    alumno1.exportar_texto("alumno1.pkl")
    alumno2.exportar_texto("alumno2.pkl")
    alumno3.exportar_texto("alumno3.pkl")

    Alumno.importar_texto("alumno1.pkl")
    Alumno.importar_texto("alumno2.pkl")
    Alumno.importar_texto("alumno3.pkl")
