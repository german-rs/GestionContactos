"""
Sistema de Gestión de Contactos - Módulo Principal

Este módulo contiene el punto de entrada de la aplicación y gestiona
la interfaz de usuario a través de un menú interactivo en consola.

El sistema permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar)
sobre una agenda de contactos con una interfaz visual mejorada mediante tablas
y códigos de color ANSI.

Attributes:
    RESET (str): Código ANSI para resetear formato de texto.
    NEGRITA (str): Código ANSI para texto en negrita.
    ROJO (str): Código ANSI para texto en color rojo.
    VERDE (str): Código ANSI para texto en color verde.
    AMARILLO (str): Código ANSI para texto en color amarillo.

Ejecución:
    Para ejecutar la aplicación desde la terminal:

        python Main.py

Autor:
    German Riveros

Fecha:
    Febrero 2026

Versión:
    1.0
"""

from src.fuentes.fuente_agenda_class import Agenda
from tabulate import tabulate

# Constantes para códigos de color ANSI
RESET = "\033[0m"  # Resetea todos los atributos de formato
NEGRITA = "\033[1m"  # Activa texto en negrita
ROJO = "\033[31m"  # Color rojo para advertencias y errores
VERDE = "\033[32m"  # Color verde para títulos y éxitos
AMARILLO = "\033[33m"  # Color amarillo para información general


def menu():
    """
    Muestra el menú principal del sistema en formato tabla.

    Esta función presenta al usuario las opciones disponibles del sistema
    utilizando la librería tabulate para un formato visual profesional.
    El menú incluye operaciones CRUD y la opción de salir.

    Las opciones disponibles son:
        1. Agregar contacto
        2. Buscar contacto
        3. Editar contacto
        4. Eliminar contacto
        5. Listar contactos
        9. Salir del sistema

    Returns:
        None

    Nota:
        Esta función no captura la entrada del usuario, solo muestra el menú.
        La captura de la opción se realiza en la función main().
    """
    print("\n")
    print(f"{VERDE} Menú del sistema de contactos")
    print(f"=============================== {RESET}")
    print()

    # Preparar datos para el menú en formato lista de listas
    opciones_menu = [
        ["1", "Agregar contacto"],
        ["2", "Buscar contacto"],
        ["3", "Editar contacto"],
        ["4", "Eliminar contacto"],
        ["5", "Listar contactos"],
        ["9", "Salir del sistema"]
    ]

    # Mostrar menú en formato tabla con estilo grid
    print(tabulate(opciones_menu, headers=["Opción", "Acción"], tablefmt="grid"))
    print()


def pausa():
    """
    Pausa la ejecución del programa esperando entrada del usuario.

    Esta función detiene el flujo del programa y espera que el usuario
    presione la tecla Enter para continuar. Útil para permitir que el
    usuario lea los mensajes o resultados antes de que se limpie la pantalla
    o se muestre el siguiente menú.

    Returns:
        None

    Nota:
        El mensaje de pausa se muestra en color amarillo con texto en negrita
        para mayor visibilidad.
    """
    input(f"{AMARILLO}Presione {NEGRITA}enter{RESET}{AMARILLO} para continuar...{RESET}")


def main():
    """
    Función principal que controla el flujo de la aplicación.

    Esta función inicializa el sistema de gestión de contactos y ejecuta
    el bucle principal del programa. Muestra el menú, captura la opción
    del usuario y ejecuta la función correspondiente.

    El bucle continúa hasta que el usuario seleccione la opción 9 (Salir).
    Después de cada operación, se llama a la función pausa() para dar
    tiempo al usuario de leer los resultados.

    Excepciones:
        ValueError: Si el usuario ingresa un valor no numérico.

    Notas importantes:
        - La instancia de Agenda se crea al inicio y persiste durante
          toda la ejecución del programa.
        - Los datos se almacenan en memoria y se pierden al cerrar el programa.
        - Las opciones inválidas muestran un mensaje de error en color rojo.

    Flujo de ejecución:
        1. Se crea una instancia de la clase Agenda
        2. Se muestra el menú principal
        3. Se captura la opción del usuario
        4. Se ejecuta la acción correspondiente
        5. Se pausa para que el usuario lea los resultados
        6. Se repite hasta que se seleccione salir (opción 9)
    """
    # Instanciar la clase Agenda para gestionar los contactos
    agenda = Agenda()

    # Variable para almacenar la opción seleccionada por el usuario
    opcion = ""

    # Bucle principal del programa
    while opcion != 9:
        # Mostrar menú de opciones
        menu()

        # Capturar opción del usuario (convertir a entero)
        opcion = int(input("Seleccione una opción: "))

        # Ejecutar la acción correspondiente según la opción seleccionada
        if opcion == 1:
            # Agregar un nuevo contacto
            agenda.agregar_contacto()
            pausa()
        elif opcion == 2:
            # Buscar un contacto existente
            agenda.buscar_contacto()
            pausa()
        elif opcion == 3:
            # Editar un contacto existente
            agenda.editar_contacto()
            pausa()
        elif opcion == 4:
            # Eliminar un contacto existente
            agenda.eliminar_contacto()
            pausa()
        elif opcion == 5:
            # Listar todos los contactos
            agenda.listar_contacto()
            pausa()
        elif opcion == 9:
            # Salir del sistema
            print("Saliendo del sistema...")
        else:
            # Opción no válida
            print(f"{ROJO}Opción no válida. Por favor, seleccione una opción del menú.{RESET}")


# Punto de entrada del programa
if __name__ == "__main__":
    """
    Punto de entrada principal de la aplicación.

    Esta sección se ejecuta solo cuando el archivo se ejecuta directamente
    (no cuando se importa como módulo). Invoca la función main() para
    iniciar el programa.
    """
    main()