from src.fuentes.fuente_agenda_class import Agenda


def main():
    print("Menú del sistema de contactos")
    print("=============================")
    print()

    # Opciones del menú
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Editar contacto")
    print("4. Eliminar contacto")
    print("5. Listar contactos")
    print("9. Salir del sistema")

    agenda = Agenda()  # Instanciando la clase
    opcion = ""
    while opcion != 9:
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