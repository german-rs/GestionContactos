from fuente_contacto_model_class import ContactoModel

class Agenda:
    def __init__(self) -> None:
        self.contacto: list = []  # lista con objetos

    def agregar_contacto(self):
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
        print("Editar contacto")

    def eliminar_contacto(self):
        print("Eliminar contacto")

    def listar_contacto(self):
        print("Listar contactos")
        print("----------------")

        if len(self.contacto) == 0:
            print("No hay contactos registrados.")
        else:
            for contacto in self.contacto:
                print(f"Nombre: {contacto.nombre}")
                print(f"Teléfono: {contacto.telefono}")
                print(f"Correo: {contacto.correo}")
                print(f"Dirección: {contacto.direccion}")
                print("----------------")