from src.fuentes.fuente_agenda_class import Agenda
from tabulate import tabulate

def menu():
    print("\n")
    print("Menú del sistema de contactos")
    print("=============================")
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


def main():

    agenda = Agenda()  # Instanciando la clase
    opcion = ""
    while opcion != 9:
        menu()
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            agenda.agregar_contacto()
        elif opcion == 2:
            agenda.buscar_contacto()
        elif opcion == 3:
            agenda.editar_contacto()
        elif opcion == 4:
            agenda.eliminar_contacto()
        elif opcion == 5:
            agenda.listar_contacto()
        elif opcion == 9:
            print("Saliendo del sistema...")
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")


if __name__ == "__main__":
    main()