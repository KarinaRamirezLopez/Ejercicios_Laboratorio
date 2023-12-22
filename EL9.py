class SaldoEfectivoInsuficiente(Exception):
    pass

class SaldoCuentaInsuficiente(Exception):
    pass

class Cuenta:
    def __init__(self, nombre, saldo_inicial):
        self.nombre = nombre
        self.saldo = saldo_inicial

    def desplegar_datos(self):
        print(f"Cuenta: {self.nombre}")
        print(f"Saldo disponible: ${self.saldo:.2f}\n")

    def deposito(self, monto):
        self.saldo += monto
        print(f"Depósito exitoso. Nuevo saldo: ${self.saldo:.2f}\n")

    def retiro(self, monto):
        if monto > self.saldo:
            raise SaldoCuentaInsuficiente("Saldo insuficiente para realizar el retiro.")
        self.saldo -= monto
        print(f"Retiro exitoso. Nuevo saldo: ${self.saldo:.2f}\n")

    def transferencia(self, otra_cuenta, monto):
        if monto > self.saldo:
            raise SaldoCuentaInsuficiente("Saldo insuficiente para realizar la transferencia.")
        self.saldo -= monto
        otra_cuenta.deposito(monto)
        print(f"Transferencia exitosa. Nuevo saldo: ${self.saldo:.2f}\n")


class CajeroAutomatico:
    def __init__(self):
        self.efectivo_disponible = 100000

    def autenticar_cuentahabiente(self, cuenta):
        # Aquí podrías implementar la lógica de autenticación
        print(f"Bienvenido, {cuenta.nombre}.\n")

    def realizar_operacion(self, cuenta, operacion, *args):
        try:
            if operacion == "desplegar_datos":
                cuenta.desplegar_datos()
            elif operacion == "deposito":
                cuenta.deposito(*args)
            elif operacion == "retiro":
                self._verificar_efectivo_suficiente(args[0])
                cuenta.retiro(*args)
            elif operacion == "transferencia":
                cuenta.transferencia(*args)
        except SaldoCuentaInsuficiente as e:
            print(f"Error: {e}")
        except SaldoEfectivoInsuficiente as e:
            print(f"Error: {e}")

    def _verificar_efectivo_suficiente(self, monto):
        if monto > self.efectivo_disponible:
            raise SaldoEfectivoInsuficiente("Efectivo insuficiente en el cajero para realizar el retiro.")


# Función para solicitar un número entero al usuario
def obtener_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")


# Ejemplo de uso interactivo
nombre_usuario = input("Ingrese su nombre de usuario: ")
saldo_inicial = obtener_entero("Ingrese el saldo inicial de su cuenta: ")

cuenta_usuario = Cuenta(nombre_usuario, saldo_inicial)
cajero_automatico = CajeroAutomatico()

cajero_automatico.autenticar_cuentahabiente(cuenta_usuario)

while True:
    print("\nOpciones:")
    print("1. Desplegar datos de la cuenta")
    print("2. Realizar depósito")
    print("3. Realizar retiro")
    print("4. Realizar transferencia")
    print("5. Salir")

    opcion = obtener_entero("Ingrese el número de la opción que desea realizar: ")

    if opcion == 1:
        cajero_automatico.realizar_operacion(cuenta_usuario, "desplegar_datos")
    elif opcion == 2:
        monto_deposito = obtener_entero("Ingrese el monto a depositar: ")
        cajero_automatico.realizar_operacion(cuenta_usuario, "deposito", monto_deposito)
    elif opcion == 3:
        monto_retiro = obtener_entero("Ingrese el monto a retirar: ")
        cajero_automatico.realizar_operacion(cuenta_usuario, "retiro", monto_retiro)
    elif opcion == 4:
        nombre_destinatario = input("Ingrese el nombre del destinatario: ")
        cuenta_destinatario = Cuenta(nombre_destinatario, 0)
        monto_transferencia = obtener_entero("Ingrese el monto a transferir: ")
        cajero_automatico.realizar_operacion(cuenta_usuario, "transferencia", cuenta_destinatario, monto_transferencia)
    elif opcion == 5:
        print("Gracias por utilizar el cajero automático. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número válido.")
