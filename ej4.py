import time
import random
from collections import deque

class Proceso:
    def __init__(self, id, nombre, duracion):
        self.id = id
        self.nombre = nombre
        self.duracion = duracion

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Duración: {self.duracion} ms"

class Microprocesador:
    def __init__(self):
        self.cola_procesos = deque()
        self.proceso_actual = None

    def generar_procesos(self, cantidad=5):
        nombres = ["Carga de Datos", "Compilación", "Renderizado", "Optimización", "Análisis"]
        for i in range(cantidad):
            id = i + 1
            nombre = random.choice(nombres)
            duracion = random.randint(500, 3000)  # Simulación de duración entre 500ms y 3000ms
            self.cola_procesos.append(Proceso(id, nombre, duracion))
        print("\nProcesos generados automáticamente:")
        self.mostrar_procesos_pendientes()

    def ejecutar_todos(self):
        while self.cola_procesos:
            self.proceso_actual = self.cola_procesos.popleft()
            print(f"\nEjecutando proceso: {self.proceso_actual}")
            time.sleep(self.proceso_actual.duracion / 1000)  # Simulación de tiempo de ejecución
            print(f"Proceso finalizado: {self.proceso_actual}")
        print("\nTodos los procesos han sido atendidos.")

    def mostrar_procesos_pendientes(self):
        if self.cola_procesos:
            for proceso in self.cola_procesos:
                print(proceso)
        else:
            print("No hay procesos pendientes.")

# Simulación automática
cpu = Microprocesador()
cpu.generar_procesos(cantidad=5)  # Genera procesos automáticamente
cpu.ejecutar_todos()  # Ejecuta todos los procesos hasta vaciar la colax

#Este código simula la ejecución de procesos en un microprocesador utilizando una cola FIFO. 
# Se generan procesos automáticamente con nombres y duraciones aleatorias, los cuales se almacenan en una cola (deque). 
# A medida que el procesador está disponible, extrae el siguiente proceso en orden de llegada y lo ejecuta, simulando su 
# duración con time.sleep(). Cuando el proceso termina, se marca como finalizado y el siguiente en la cola comienza su ejecución, 
# hasta que no queden más procesos. También incluye funciones para visualizar los procesos pendientes y administrar la ejecución sin 
# intervención manual, acercándose al comportamiento real de un sistema de procesamiento continuo.
#Esta implementación automatiza la asignación y ejecución de tareas, eliminando la necesidad de ingreso manual de datos y reduciendo la interacción del usuario. 
