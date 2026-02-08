from src.fuentes.fuente_agenda_class import Agenda
from tabulate import tabulate

RESET = "\033[0m"
NEGRITA = "\033[1m"
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"


def menu():
    print("\n")
    print( f"{VERDE} Menú del sistema de contactos")
    print(f"=============================== {RESET}")
    print()

    # Preparar datos para el menú
    opciones_menu = [
        ["1", "Agregar contacto"],
        ["2", "Buscar contacto"],
        ["3", "Editar contacto"],
        ["4", "Eliminar contacto"],
        ["5", "Listar contactos"],
        ["9", "Salir del sistema"]
    ]

    # Mostrar menú en tabla
    print(tabulate(opciones_menu, headers=["Opción", "Acción"], tablefmt="grid"))
    print()

def pausa():
    input(f"{AMARILLO}Presione {NEGRITA}enter{RESET}{AMARILLO} para continuar...{RESET}")

def main():

    agenda = Agenda()  # Instanciando la clase
    opcion = ""
    while opcion != 9:
        menu()

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            agenda.agregar_contacto()
            pausa()
        elif opcion == 2:
            agenda.buscar_contacto()
            pausa()
        elif opcion == 3:
            agenda.editar_contacto()
            pausa()
        elif opcion == 4:
            agenda.eliminar_contacto()
            pausa()
        elif opcion == 5:
            agenda.listar_contacto()
            pausa()
        elif opcion == 9:
            print("Saliendo del sistema...")
        else:
            print(f"{ROJO}Opción no válida. Por favor, seleccione una opción del menú.{RESET}")


if __name__ == "__main__":
    main()