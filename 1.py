'''
Simule el funcionamiento de una cola de impresión en una oficina donde varios empleados envían documentos para ser impresos. 
Cada documento tiene un nombre, el usuario que lo envió y el número de páginas. El sistema debe permitir agregar documentos a la cola, 
procesarlos en orden de llegada y mostrar cuál es el documento que se está imprimiendo actualmente.
'''

cola_de_impresion = []
documento_imprimiendose_actualmente = None

def agregar_documento():
    global cola_de_impresion
    print("\n--- Agregar Nuevo Documento ---")
    nombre_doc = input("Nombre del documento: ")
    usuario_envia = input("Nombre del usuario que envía: ")
    while True:
        try:
            num_paginas = int(input("Número de páginas: "))
            if num_paginas > 0:
                break
            else:
                print("El número de páginas debe ser mayor que cero.")
        except ValueError:
            print("Por favor, ingrese un número válido para las páginas.")

    documento = {
        "nombre": nombre_doc,
        "usuario": usuario_envia,
        "paginas": num_paginas
    }
    cola_de_impresion.append(documento)
    print(f"'{documento['nombre']}' (de {documento['usuario']}) se agregó a la cola.")

def mostrar_estado_impresora():
    global documento_imprimiendose_actualmente

    if documento_imprimiendose_actualmente:
        print(f"\n--- Imprimiendo Ahora ---")
        print(f"Nombre: {documento_imprimiendose_actualmente['nombre']}")
        print(f"Usuario: {documento_imprimiendose_actualmente['usuario']}")
        print(f"Páginas: {documento_imprimiendose_actualmente['paginas']}")
        print(f"-------------------------")
    elif cola_de_impresion:
        siguiente_doc = cola_de_impresion[0]
        print(f"\n--- Próximo a Imprimir ---")
        print(f"Nombre: {siguiente_doc['nombre']}")
        print(f"Usuario: {siguiente_doc['usuario']}")
        print(f"Páginas: {siguiente_doc['paginas']}")
        print(f"--------------------------")
    else:
        print("\nNo hay documentos imprimiéndose ni en la cola.")

def procesar_siguiente():
    global documento_imprimiendose_actualmente
    global cola_de_impresion

    if documento_imprimiendose_actualmente:
        print(f"\n'{documento_imprimiendose_actualmente['nombre']}' terminó de imprimirse.")
        documento_imprimiendose_actualmente = None

    if cola_de_impresion:
        documento_a_imprimir = cola_de_impresion.pop(0)
        documento_imprimiendose_actualmente = documento_a_imprimir
        print(f"\nIniciando impresión de: '{documento_a_imprimir['nombre']}' (Usuario: {documento_a_imprimir['usuario']}, Páginas: {documento_a_imprimir['paginas']})")
    elif not documento_imprimiendose_actualmente:
        print("\nLa cola de impresión está vacía. Nada para procesar.")

def ver_cola_actual():
    global cola_de_impresion
    print("\n--- Cola de Impresión Actual ---")
    if documento_imprimiendose_actualmente:
        print(f"Imprimiendo Ahora: {documento_imprimiendose_actualmente['nombre']} (de {documento_imprimiendose_actualmente['usuario']})")

    if not cola_de_impresion:
        if not documento_imprimiendose_actualmente:
            print("La cola de impresión está completamente vacía.")
        else:
            print("No hay documentos en espera en la cola.")
    else:
        print("Documentos en espera:")
        for i, doc in enumerate(cola_de_impresion):
            print(f"  {i+1}. {doc['nombre']} (Usuario: {doc['usuario']}, Páginas: {doc['paginas']})")
    print("-------------------------------")

def mostrar_menu():
    print("\n--- Menú de Cola de Impresión ---")
    print("1. Agregar documento a la cola")
    print("2. Procesar siguiente documento")
    print("3. Documento que se está imprimiendo actualmente")
    print("4. Ver todos los documentos en la cola")
    print("5. Salir")
    return input("Seleccione una opción: ")

# --- Simulación Interactiva ---
if __name__ == "__main__":

    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            agregar_documento()
        elif opcion == '2':
            procesar_siguiente()
        elif opcion == '3':
            mostrar_estado_impresora()
        elif opcion == '4':
            ver_cola_actual()
        elif opcion == '5':
            print("Saliendo del simulador de cola de impresión.")
            if documento_imprimiendose_actualmente:
                print(f"Advertencia: El documento '{documento_imprimiendose_actualmente['nombre']}' estaba imprimiéndose y no se completó.")
            if cola_de_impresion:
                print(f"Advertencia: Quedaron {len(cola_de_impresion)} documentos en la cola sin procesar.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")