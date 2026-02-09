class ContactoModel:
    """
    Modelo de datos que representa un contacto en la agenda.

    Esta clase encapsula la información básica de un contacto individual,
    incluyendo datos personales y de ubicación.

    Attributes:
        nombre (str): Nombre completo del contacto.
        telefono (str): Número telefónico del contacto.
        correo (str): Dirección de correo electrónico.
        direccion (str): Dirección física o domicilio del contacto.

    Example:
        contacto = ContactoModel("Juan Pérez", "555-1234", "juan@email.com", "Calle 123")
        print(contacto.nombre)
        'Juan Pérez'
    """

    def __init__(self, nombre, telefono, correo, direccion) -> None:
        """
        Inicializa una nueva instancia de ContactoModel.

        Args:
            nombre (str): Nombre completo del contacto.
            telefono (str): Número telefónico del contacto.
            correo (str): Dirección de correo electrónico.
            direccion (str): Dirección física del contacto.

        Returns:
            None
        """
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
