from collections import deque

class Llamada:
    def __init__(self, nombre_cliente, motivo):
        self.nombre_cliente = nombre_cliente
        self.motivo = motivo

    def __str__(self):
        return f"Cliente: {self.nombre_cliente} | Motivo: {self.motivo}"

class CentroAtencion:
    def __init__(self):
        self.cola_llamadas = deque()

    def registrar_llamada(self, nombre_cliente, motivo):
        llamada = Llamada(nombre_cliente, motivo)
        self.cola_llamadas.append(llamada)
        print(f" Llamada registrada: {llamada}\n")

    def atender_llamada(self):
        if not self.cola_llamadas:
            print(" No hay llamadas en espera.\n")
        else:
            llamada = self.cola_llamadas.popleft()
            print(f" Atendiendo llamada: {llamada}\n")

    def mostrar_llamadas_en_espera(self):
        print(" Llamadas en espera:")
        if not self.cola_llamadas:
            print("  No hay llamadas en la cola.\n")
        else:
            for i, llamada in enumerate(self.cola_llamadas, start=1):
                print(f"  {i}. {llamada}")
            print()

# --- Menú interactivo ---
def menu():
    centro = CentroAtencion()

    while True:
        print("=== CENTRO DE ATENCIÓN AL CLIENTE ===")
        print("1. Registrar llamada")
        print("2. Atender llamada")
        print("3. Mostrar llamadas en espera")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del cliente: ")
            motivo = input("Ingrese el motivo de la llamada: ")
            centro.registrar_llamada(nombre, motivo)
        elif opcion == "2":
            centro.atender_llamada()
        elif opcion == "3":
            centro.mostrar_llamadas_en_espera()
        elif opcion == "4":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print(" Opción no válida. Intente nuevamente.\n")

# Ejecutar menú
if __name__ == "__main__":
    menu()
