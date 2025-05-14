from collections import deque

# Clase para representar un paciente
class Paciente:
    def __init__(self, nombre, servicio):
        self.nombre = nombre
        self.servicio = servicio

    def __str__(self):
        return f"{self.nombre} ({self.servicio})"

# Clase para gestionar la cola de la farmacia
class Farmacia:
    def __init__(self):
        self.cola = deque()

    def registrar_paciente(self, nombre, servicio):
        paciente = Paciente(nombre, servicio)
        self.cola.append(paciente)
        print(f"\n Paciente registrado: {paciente}")

    def atender_paciente(self):
        if self.cola:
            paciente = self.cola.popleft()
            print(f"\n Atendiendo a: {paciente}")
        else:
            print("\n No hay pacientes en espera.")

    def mostrar_turnos_pendientes(self):
        if self.cola:
            print("\n Turnos pendientes:")
            for i, paciente in enumerate(self.cola, start=1):
                print(f"{i}. {paciente}")
        else:
            print("\n No hay turnos pendientes.")

# Función principal con menú y validaciones
def menu():
    farmacia = Farmacia()

    while True:
        print("\n--- Gestión de Turnos en la Farmacia ---")
        print("1. Registrar nuevo paciente")
        print("2. Atender al siguiente paciente")
        print("3. Mostrar turnos pendientes")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion not in ["1", "2", "3", "4"]:
            print("Opción no válida. Intente de nuevo.")
            continue

        if opcion == "1":
            nombre = input("Ingrese el nombre del paciente: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío.")
                continue

            servicio = input("Ingrese el tipo de servicio (compra, consulta, receta): ").strip().lower()
            if servicio not in ["compra", "consulta", "receta"]:
                print("Servicio no válido. Debe ser: compra, consulta o receta.")
                continue

            farmacia.registrar_paciente(nombre, servicio)

        elif opcion == "2":
            farmacia.atender_paciente()

        elif opcion == "3":
            farmacia.mostrar_turnos_pendientes()

        elif opcion == "4":
            print("Saliendo del sistema.")
            break

# Ejecutar el programa
if __name__ == "__main__":
    menu()
