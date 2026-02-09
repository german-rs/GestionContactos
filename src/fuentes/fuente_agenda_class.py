"""
Módulo de Gestión de Agenda de Contactos

Este módulo contiene la clase Agenda que gestiona todas las operaciones CRUD
(Crear, Leer, Actualizar, Eliminar) sobre una colección de contactos.

La clase utiliza el modelo ContactoModel para estructurar los datos y
tabulate para presentar la información en formato tabla profesional.

Attributes:
    RESET (str): Código ANSI para resetear formato de texto.
    ROJO (str): Código ANSI para texto en color rojo (advertencias).
    VERDE (str): Código ANSI para texto en color verde (éxitos).
    AMARILLO (str): Código ANSI para texto en color amarillo (información).

Autor:
    German Riveros

Fecha:
    Febrero 2026

Versión:
    1.0
"""

from src.fuentes.fuente_contacto_model_class import ContactoModel
from tabulate import tabulate

# Constantes para códigos de color ANSI
RESET = "\033[0m"  # Resetea todos los atributos de formato
ROJO = "\033[31m"  # Color rojo para advertencias y errores
VERDE = "\033[32m"  # Color verde para mensajes de éxito
AMARILLO = "\033[33m"  # Color amarillo para información general


class Agenda:
    """
    Clase que gestiona una agenda de contactos.

    Esta clase permite realizar operaciones completas de gestión sobre
    una colección de contactos almacenada en memoria. Implementa todas
    las operaciones CRUD con una interfaz de consola mejorada mediante
    tablas y códigos de color.

    Attributes:
        contacto (list): Lista que almacena objetos de tipo ContactoModel.

    Métodos públicos:
        agregar_contacto(): Añade un nuevo contacto a la agenda.
        buscar_contacto(): Busca un contacto por nombre o teléfono.
        editar_contacto(): Modifica los datos de un contacto existente.
        eliminar_contacto(): Elimina un contacto de la agenda.
        listar_contacto(): Muestra todos los contactos en formato tabla.
    """

    def __init__(self) -> None:
        """
        Inicializa una nueva instancia de la clase Agenda.

        Crea una lista vacía que almacenará los objetos ContactoModel
        durante la ejecución del programa.

        Returns:
            None
        """
        self.contacto: list = []  # lista con objetos

    def agregar_contacto(self):
        """
        Añade un nuevo contacto a la agenda.

        Solicita al usuario los datos del contacto (nombre, teléfono, correo
        y dirección), crea una instancia de ContactoModel y la añade a la
        lista de contactos.

        Proceso:
            1. Solicita nombre del contacto
            2. Solicita número de teléfono
            3. Solicita dirección de correo electrónico
            4. Solicita dirección física
            5. Crea un objeto ContactoModel con los datos
            6. Añade el objeto a la lista de contactos
            7. Muestra mensaje de confirmación en verde

        Returns:
            None

        Nota:
            No se realizan validaciones de formato en esta versión.
            Todos los campos aceptan cualquier entrada de texto.
        """
        print("\n")
        print("Agregar contacto")
        print("----------------")

        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")
        direccion = input("Dirección: ")

        # Instanciar la clase ContactoModel con los datos ingresados (Objeto) con el contrato
        # var/obj          class              argumentos
        nuevo_contacto = ContactoModel(nombre, telefono, correo, direccion)
        self.contacto.append(nuevo_contacto)

        print(f"{VERDE}¡Contacto agregado exitosamente!{RESET}")

    def buscar_contacto(self) -> bool:
        """
        Busca un contacto en la agenda por nombre o teléfono.

        Solicita al usuario un criterio de búsqueda (nombre o teléfono) y
        busca coincidencias exactas en la lista de contactos. Si encuentra
        el contacto, muestra todos sus datos.

        Proceso:
            1. Valida que existan contactos en la agenda
            2. Solicita criterio de búsqueda (nombre o teléfono)
            3. Itera sobre la lista de contactos
            4. Compara el criterio con nombre y teléfono de cada contacto
            5. Si encuentra coincidencia, muestra los datos
            6. Si no encuentra, muestra mensaje informativo

        Returns:
            bool: True si encuentra el contacto, False en caso contrario.

        Nota:
            - La búsqueda es case-sensitive (distingue mayúsculas/minúsculas)
            - Solo retorna el primer contacto que coincida
            - Requiere coincidencia exacta del nombre o teléfono
        """
        print("Buscar contacto")
        print("----------------")

        # Validar si hay contactos registrados
        if len(self.contacto) == 0:
            print(f"{ROJO}No hay contactos registrados para buscar.{RESET}")
            return False

        buscar = input("Ingrese el nombre/teléfono del contacto a buscar: ")
        encontrado = False
        for contacto in self.contacto:
            if contacto.nombre == buscar or contacto.telefono == buscar:
                print(f"Nombre: {contacto.nombre}")
                print(f"Teléfono: {contacto.telefono}")
                print(f"Correo: {contacto.correo}")
                print(f"Dirección: {contacto.direccion}")
                encontrado = True
                break
        if not encontrado:
            print("Contacto no encontrado.")

        return encontrado

    def editar_contacto(self):
        """
        Edita los datos de un contacto existente en la agenda.

        Muestra todos los contactos disponibles en formato tabla, solicita
        el identificador del contacto a editar (nombre o teléfono) y permite
        modificar cada campo individualmente. Si el usuario presiona Enter
        sin escribir nada, el campo mantiene su valor actual.

        Proceso:
            1. Valida que existan contactos en la agenda
            2. Muestra tabla con todos los contactos disponibles
            3. Solicita identificador del contacto (nombre o teléfono)
            4. Busca el contacto en la lista
            5. Muestra los datos actuales del contacto en formato tabla
            6. Solicita nuevo valor para cada campo
            7. Actualiza solo los campos que el usuario modifique
            8. Muestra mensaje de confirmación en verde

        Returns:
            None

        Características:
            - Permite editar nombre, teléfono, correo y dirección
            - Presionar Enter mantiene el valor actual del campo
            - Búsqueda por coincidencia exacta de nombre o teléfono
            - Muestra vista previa antes de editar

        Nota:
            Si no se encuentran contactos o el identificador no coincide,
            se muestra un mensaje informativo y termina la función.
        """
        print("\n")
        print("Editar contacto")
        print("----------------")

        # Primero listar todos los contactos
        if len(self.contacto) == 0:
            print("No hay contactos registrados para editar.")
            return

        print("Contactos disponibles:")
        print()

        # Preparar datos para la tabla
        datos_tabla = []
        for contacto in self.contacto:
            datos_tabla.append([
                contacto.nombre,
                contacto.telefono,
                contacto.correo,
                contacto.direccion
            ])

        # Mostrar tabla
        encabezados = ["Nombre", "Teléfono", "Correo", "Dirección"]
        print(tabulate(datos_tabla, headers=encabezados, tablefmt="grid"))
        print()

        # Buscar el contacto a editar
        buscar = input("Ingrese el nombre/teléfono del contacto a editar: ")
        encontrado = False

        for contacto in self.contacto:
            if contacto.nombre == buscar or contacto.telefono == buscar:
                encontrado = True
                print()
                print("Datos actuales del contacto:")

                # Mostrar datos actuales en tabla
                datos_actual = [[
                    contacto.nombre,
                    contacto.telefono,
                    contacto.correo,
                    contacto.direccion
                ]]
                print(tabulate(datos_actual, headers=encabezados, tablefmt="grid"))
                print()

                print("Ingrese los nuevos datos (presione Enter para mantener el valor actual):")

                # Editar cada campo
                nuevo_nombre = input(f"Nuevo nombre (Enter para mantener '{contacto.nombre}'): ")
                if nuevo_nombre:
                    contacto.nombre = nuevo_nombre

                nuevo_telefono = input(f"Nuevo teléfono (Enter para mantener '{contacto.telefono}'): ")
                if nuevo_telefono:
                    contacto.telefono = nuevo_telefono

                nuevo_correo = input(f"Nuevo correo (Enter para mantener '{contacto.correo}'): ")
                if nuevo_correo:
                    contacto.correo = nuevo_correo

                nueva_direccion = input(f"Nueva dirección (Enter para mantener '{contacto.direccion}'): ")
                if nueva_direccion:
                    contacto.direccion = nueva_direccion

                print()
                print(f"{VERDE}¡Contacto editado exitosamente!{RESET}")
                break

        if not encontrado:
            print("Contacto no encontrado.")

    def eliminar_contacto(self):
        """
        Elimina un contacto de la agenda.

        Muestra todos los contactos disponibles en formato tabla, solicita
        el identificador del contacto a eliminar y pide confirmación antes
        de realizar la eliminación definitiva.

        Proceso:
            1. Valida que existan contactos en la agenda
            2. Muestra tabla con todos los contactos disponibles
            3. Solicita identificador del contacto (nombre o teléfono)
            4. Busca el contacto en la lista
            5. Muestra los datos del contacto encontrado en formato tabla
            6. Solicita confirmación (s/n) antes de eliminar
            7. Si el usuario confirma con 's', elimina el contacto
            8. Si el usuario cancela, mantiene el contacto
            9. Muestra mensaje apropiado según la acción realizada

        Returns:
            None

        Características:
            - Requiere confirmación explícita antes de eliminar
            - La confirmación acepta 's' o 'S' (case-insensitive)
            - Cualquier otra entrada cancela la eliminación
            - Muestra vista previa del contacto antes de eliminar

        Nota:
            Esta es una operación destructiva e irreversible. Una vez
            eliminado, el contacto no se puede recuperar ya que los datos
            solo existen en memoria.
        """
        print("\n")
        print("Eliminar contacto")
        print("----------------")

        # Primero listar todos los contactos
        if len(self.contacto) == 0:
            print("No hay contactos registrados para eliminar.")
            return

        print("Contactos disponibles:")
        print()

        # Preparar datos para la tabla
        datos_tabla = []
        for contacto in self.contacto:
            datos_tabla.append([
                contacto.nombre,
                contacto.telefono,
                contacto.correo,
                contacto.direccion
            ])

        # Mostrar tabla
        encabezados = ["Nombre", "Teléfono", "Correo", "Dirección"]
        print(tabulate(datos_tabla, headers=encabezados, tablefmt="grid"))
        print()

        # Buscar el contacto a eliminar
        buscar = input("Ingrese el nombre/teléfono del contacto a eliminar: ")
        encontrado = False

        for contacto in self.contacto:
            if contacto.nombre == buscar or contacto.telefono == buscar:
                encontrado = True
                print()
                print("Contacto encontrado:")

                # Mostrar contacto encontrado en tabla
                datos_encontrado = [[
                    contacto.nombre,
                    contacto.telefono,
                    contacto.correo,
                    contacto.direccion
                ]]
                print(tabulate(datos_encontrado, headers=encabezados, tablefmt="grid"))
                print()

                # Confirmar la eliminación
                confirmacion = input(f"{ROJO}¿Está seguro que desea eliminar este contacto? (s/n): {RESET}")

                if confirmacion.lower() == 's':
                    self.contacto.remove(contacto)
                    print()
                    print(f"{VERDE}Contacto eliminado exitosamente!{RESET}")
                else:
                    print()
                    print("Eliminación cancelada.")
                break

        if not encontrado:
            print("Contacto no encontrado.")

    def listar_contacto(self):
        """
        Lista todos los contactos de la agenda en formato tabla.

        Muestra todos los contactos almacenados en la agenda utilizando
        el formato de tabla profesional proporcionado por la librería
        tabulate. Si no hay contactos, muestra un mensaje informativo.

        Proceso:
            1. Valida si existen contactos en la agenda
            2. Si no hay contactos, muestra mensaje y termina
            3. Si hay contactos, prepara los datos en formato lista de listas
            4. Define los encabezados de la tabla
            5. Muestra la tabla con formato grid

        Returns:
            None

        Formato de tabla:
            La tabla incluye cuatro columnas:
            - Nombre: Nombre completo del contacto
            - Teléfono: Número telefónico
            - Correo: Dirección de email
            - Dirección: Dirección física

        Nota:
            Los contactos se muestran en el orden en que fueron agregados.
            No se aplica ningún tipo de ordenamiento.
        """
        print("Listar contactos")
        print("----------------")

        if len(self.contacto) == 0:
            print("No hay contactos registrados.")
        else:
            # Preparar datos para la tabla
            datos_tabla = []
            for contacto in self.contacto:
                datos_tabla.append([
                    contacto.nombre,
                    contacto.telefono,
                    contacto.correo,
                    contacto.direccion
                ])

            # Definir encabezados
            encabezados = ["Nombre", "Teléfono", "Correo", "Dirección"]

            # Mostrar tabla
            print()
            print(tabulate(datos_tabla, headers=encabezados, tablefmt="grid"))
            print()