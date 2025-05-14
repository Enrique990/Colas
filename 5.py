from collections import deque

class Solicitud:
    def __init__(self, usuario, archivo):
        self.usuario = usuario
        self.archivo = archivo

    def __str__(self):
        return f"Usuario: {self.usuario} | Archivo: {self.archivo}"

class ServidorArchivos:
    def __init__(self):
        self.cola_solicitudes = deque()
        self.en_uso = None  # Guarda la solicitud que está siendo atendida

    def registrar_solicitud(self, usuario, archivo):
        solicitud = Solicitud(usuario, archivo)
        self.cola_solicitudes.append(solicitud)
        print(f" Solicitud registrada: {solicitud}\n")

    def atender_solicitud(self):
        if self.en_uso:
            print(f" El archivo todavía está en uso por {self.en_uso.usuario}.\n")
        elif not self.cola_solicitudes:
            print(" No hay solicitudes pendientes.\n")
        else:
            self.en_uso = self.cola_solicitudes.popleft()
            print(f" Acceso concedido: {self.en_uso}\n")

    def liberar_archivo(self):
        if self.en_uso:
            print(f" Archivo liberado por: {self.en_uso.usuario}\n")
            self.en_uso = None
        else:
            print(" Ningún archivo está siendo accedido actualmente.\n")

    def mostrar_en_uso(self):
        if self.en_uso:
            print(f" Archivo en uso por: {self.en_uso.usuario} | Archivo: {self.en_uso.archivo}\n")
        else:
            print(" Actualmente no hay archivo en uso.\n")

    def mostrar_solicitudes_pendientes(self):
        print("  Solicitudes pendientes:")
        if not self.cola_solicitudes:
            print("  No hay solicitudes en espera.\n")
        else:
            for i, solicitud in enumerate(self.cola_solicitudes, start=1):
                print(f"  {i}. {solicitud}")
            print()

# Menú interactivo
def menu():
    servidor = ServidorArchivos()

    while True:
        print("=== GESTIÓN DE ACCESO A ARCHIVOS EN SERVIDOR ===")
        print("1. Registrar solicitud de acceso")
        print("2. Atender siguiente solicitud")
        print("3. Liberar archivo en uso")
        print("4. Mostrar archivo en uso")
        print("5. Mostrar solicitudes pendientes")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuario = input("Nombre del usuario: ")
            archivo = input("Nombre del archivo: ")
            servidor.registrar_solicitud(usuario, archivo)
        elif opcion == "2":
            servidor.atender_solicitud()
        elif opcion == "3":
            servidor.liberar_archivo()
        elif opcion == "4":
            servidor.mostrar_en_uso()
        elif opcion == "5":
            servidor.mostrar_solicitudes_pendientes()
        elif opcion == "6":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("  Opción inválida. Intente nuevamente.\n")

# Ejecutar menú
if __name__ == "__main__":
    menu()
