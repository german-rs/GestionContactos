from src.fuentes.fuente_contacto_model_class import ContactoModel
from tabulate import tabulate

class Agenda:
    def __init__(self) -> None:
        self.contacto: list = []  # lista con objetos

    def agregar_contacto(self):
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

        print("Contacto agregado exitosamente.")

    def buscar_contacto(self) -> bool:
        print("\n")
        print("Buscar contacto")
        print("----------------")

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
        print("\n")
        print("Editar contacto")
        print("----------------")

        # Primero listar todos los contactos
        if len(self.contacto) == 0:
            print("No hay contactos registrados para editar.")
            return

        print("Contactos disponibles:")
        print()
        for contacto in self.contacto:
            print(f"Nombre: {contacto.nombre}")
            print(f"Teléfono: {contacto.telefono}")
            print(f"Correo: {contacto.correo}")
            print(f"Dirección: {contacto.direccion}")
            print("----------------")

        # Buscar el contacto a editar
        buscar = input("Ingrese el nombre/teléfono del contacto a editar: ")
        encontrado = False

        for contacto in self.contacto:
            if contacto.nombre == buscar or contacto.telefono == buscar:
                encontrado = True
                print()
                print("Datos actuales del contacto:")
                print(f"Nombre actual: {contacto.nombre}")
                print(f"Teléfono actual: {contacto.telefono}")
                print(f"Correo actual: {contacto.correo}")
                print(f"Dirección actual: {contacto.direccion}")
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
                print("Contacto editado exitosamente.")
                break

        if not encontrado:
            print("Contacto no encontrado.")

    def eliminar_contacto(self):
        print("\n")
        print("Eliminar contacto")
        print("----------------")

        # Primero listar todos los contactos
        if len(self.contacto) == 0:
            print("No hay contactos registrados para eliminar.")
            return

        print("Contactos disponibles:")
        print()
        for contacto in self.contacto:
            print(f"Nombre: {contacto.nombre}")
            print(f"Teléfono: {contacto.telefono}")
            print(f"Correo: {contacto.correo}")
            print(f"Dirección: {contacto.direccion}")
            print("----------------")

        # Buscar el contacto a eliminar
        buscar = input("Ingrese el nombre/teléfono del contacto a eliminar: ")
        encontrado = False

        for contacto in self.contacto:
            if contacto.nombre == buscar or contacto.telefono == buscar:
                encontrado = True
                print()
                print("Contacto encontrado:")
                print(f"Nombre: {contacto.nombre}")
                print(f"Teléfono: {contacto.telefono}")
                print(f"Correo: {contacto.correo}")
                print(f"Dirección: {contacto.direccion}")
                print()

                # Confirmar la eliminación
                confirmacion = input("¿Está seguro que desea eliminar este contacto? (s/n): ")

                if confirmacion.lower() == 's':
                    self.contacto.remove(contacto)
                    print()
                    print("Contacto eliminado exitosamente.")
                else:
                    print()
                    print("Eliminación cancelada.")
                break

        if not encontrado:
            print("Contacto no encontrado.")

    def listar_contacto(self):
        print("\n")
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