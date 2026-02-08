# Documentación Técnica - Sistema de Gestión de Contactos

## Índice
1. [Descripción General](#descripción-general)
2. [Estructura del Proyecto](#estructura-del-proyecto)
3. [Arquitectura del Sistema](#arquitectura-del-sistema)
4. [Módulos y Componentes](#módulos-y-componentes)
5. [Dependencias](#dependencias)
6. [Instalación y Configuración](#instalación-y-configuración)
7. [Guía de Ejecución](#guía-de-ejecución)
8. [Funcionalidades Detalladas](#funcionalidades-detalladas)
9. [Características Técnicas](#características-técnicas)
10. [Posibles Mejoras Futuras](#posibles-mejoras-futuras)

---

## Descripción General

Sistema de gestión de contactos desarrollado en Python para entorno de consola/terminal. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una agenda de contactos con una interfaz de usuario en formato de tabla utilizando la librería `tabulate`.

**Versión:** 1.0  
**Lenguaje:** Python 3.x  
**Tipo de Aplicación:** Consola/Terminal  
**Paradigma:** Programación Orientada a Objetos (POO)

---

## Estructura del Proyecto

```
GestionContactos/
│
├── Main.py                                    # Punto de entrada de la aplicación
│
└── src/
    ├── __init__.py                           # Inicializador del paquete src
    └── fuentes/
        ├── __init__.py                       # Inicializador del paquete fuentes
        ├── fuente_contacto_model_class.py   # Modelo de datos (ContactoModel)
        └── fuente_agenda_class.py           # Lógica de negocio (Agenda)
```

### Descripción de Archivos

| Archivo | Propósito | Responsabilidad |
|---------|-----------|-----------------|
| `Main.py` | Archivo principal | Maneja el menú y flujo de la aplicación |
| `fuente_contacto_model_class.py` | Modelo de datos | Define la estructura de un contacto |
| `fuente_agenda_class.py` | Controlador | Gestiona las operaciones sobre los contactos |
| `__init__.py` | Inicializadores | Permite la importación de módulos como paquetes |

---

## Arquitectura del Sistema

El sistema utiliza una arquitectura **MVC simplificada** adaptada para aplicaciones de consola:

```
┌─────────────────────────────────────────────────────────┐
│                        Main.py                          │
│              (Vista + Controlador Principal)            │
│                                                         │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   menu()    │  │   pausa()    │  │    main()    │  │
│  └─────────────┘  └──────────────┘  └──────────────┘  │
└────────────────────────┬────────────────────────────────┘
                         │
                         │ Importa y usa
                         ▼
┌─────────────────────────────────────────────────────────┐
│              fuente_agenda_class.py                     │
│                   (Modelo/Lógica)                       │
│                                                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │              Clase Agenda                        │  │
│  │  - agregar_contacto()                           │  │
│  │  - buscar_contacto()                            │  │
│  │  - editar_contacto()                            │  │
│  │  - eliminar_contacto()                          │  │
│  │  - listar_contacto()                            │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────┘
                         │
                         │ Utiliza
                         ▼
┌─────────────────────────────────────────────────────────┐
│         fuente_contacto_model_class.py                  │
│                   (Modelo de Datos)                     │
│                                                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │          Clase ContactoModel                     │  │
│  │  Atributos:                                      │  │
│  │    - nombre                                      │  │
│  │    - telefono                                    │  │
│  │    - correo                                      │  │
│  │    - direccion                                   │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

### Patrón de Diseño

- **Separación de Responsabilidades:** Cada clase tiene una responsabilidad única
- **Modelo de Datos:** `ContactoModel` encapsula la información de un contacto
- **Lógica de Negocio:** `Agenda` maneja todas las operaciones sobre la colección de contactos
- **Interfaz de Usuario:** `Main.py` gestiona la interacción con el usuario

---

## Módulos y Componentes

### 1. ContactoModel (`fuente_contacto_model_class.py`)

**Propósito:** Representa la estructura de datos de un contacto individual.

**Clase:** `ContactoModel`

**Atributos:**
```python
- nombre: str       # Nombre del contacto
- telefono: str     # Número telefónico
- correo: str       # Dirección de correo electrónico
- direccion: str    # Dirección física
```

**Métodos:**
```python
__init__(self, nombre, telefono, correo, direccion) -> None
    Constructor que inicializa un contacto con los datos proporcionados.
```

**Código:**
```python
class ContactoModel:
    def __init__(self, nombre, telefono, correo, direccion) -> None:
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
```

---

### 2. Agenda (`fuente_agenda_class.py`)

**Propósito:** Gestionar la colección de contactos y todas las operaciones CRUD.

**Clase:** `Agenda`

**Atributos:**
```python
- contacto: list    # Lista que almacena objetos de tipo ContactoModel
```

**Constantes de Color:**
```python
RESET = "\033[0m"      # Resetea formato
ROJO = "\033[31m"      # Color rojo para advertencias
VERDE = "\033[32m"     # Color verde para éxitos
AMARILLO = "\033[33m"  # Color amarillo para información
```

**Métodos:**

#### `__init__(self) -> None`
Constructor que inicializa la lista de contactos vacía.

#### `agregar_contacto(self)`
- **Descripción:** Permite agregar un nuevo contacto a la agenda
- **Entrada:** Solicita al usuario: nombre, teléfono, correo, dirección
- **Proceso:** Crea una instancia de `ContactoModel` y la agrega a la lista
- **Salida:** Mensaje de confirmación en color verde

#### `buscar_contacto(self) -> bool`
- **Descripción:** Busca un contacto por nombre o teléfono
- **Validación:** Verifica que haya contactos registrados
- **Entrada:** Nombre o teléfono a buscar
- **Proceso:** Itera sobre la lista comparando nombre y teléfono
- **Salida:** Muestra los datos del contacto si se encuentra
- **Retorno:** `True` si encuentra el contacto, `False` en caso contrario

#### `editar_contacto(self)`
- **Descripción:** Permite modificar los datos de un contacto existente
- **Validación:** Verifica que haya contactos registrados
- **Proceso:**
  1. Lista todos los contactos en formato tabla
  2. Solicita identificador (nombre o teléfono)
  3. Muestra datos actuales en formato tabla
  4. Permite editar campo por campo (Enter mantiene valor actual)
- **Salida:** Mensaje de confirmación en color verde

#### `eliminar_contacto(self)`
- **Descripción:** Elimina un contacto de la agenda
- **Validación:** Verifica que haya contactos registrados
- **Proceso:**
  1. Lista todos los contactos en formato tabla
  2. Solicita identificador (nombre o teléfono)
  3. Muestra el contacto encontrado en formato tabla
  4. Pide confirmación (s/n) antes de eliminar
- **Salida:** Mensaje de confirmación o cancelación

#### `listar_contacto(self)`
- **Descripción:** Muestra todos los contactos registrados
- **Validación:** Verifica que haya contactos registrados
- **Proceso:** Prepara los datos y los muestra en formato tabla
- **Salida:** Tabla formateada con todos los contactos

---

### 3. Main (`Main.py`)

**Propósito:** Punto de entrada de la aplicación, gestiona el menú principal y el flujo del programa.

**Constantes de Color:**
```python
RESET = "\033[0m"      # Resetea formato
NEGRITA = "\033[1m"    # Texto en negrita
ROJO = "\033[31m"      # Color rojo
VERDE = "\033[32m"     # Color verde
AMARILLO = "\033[33m"  # Color amarillo
```

**Funciones:**

#### `menu()`
- **Descripción:** Muestra el menú principal de opciones
- **Formato:** Utiliza `tabulate` con estilo "grid" para presentar las opciones
- **Opciones disponibles:**
  - 1: Agregar contacto
  - 2: Buscar contacto
  - 3: Editar contacto
  - 4: Eliminar contacto
  - 5: Listar contactos
  - 9: Salir del sistema

#### `pausa()`
- **Descripción:** Pausa la ejecución esperando que el usuario presione Enter
- **Propósito:** Permite al usuario leer los mensajes antes de limpiar la pantalla
- **Formato:** Mensaje en amarillo con texto en negrita

#### `main()`
- **Descripción:** Función principal que controla el flujo de la aplicación
- **Proceso:**
  1. Instancia un objeto de la clase `Agenda`
  2. Entra en un bucle while hasta que el usuario seleccione salir (opción 9)
  3. Muestra el menú
  4. Captura la opción del usuario
  5. Ejecuta la función correspondiente
  6. Llama a `pausa()` después de cada operación
- **Validación:** Muestra mensaje de error si la opción no es válida

---

## Dependencias

### Librerías de Python Estándar

| Librería | Versión | Uso |
|----------|---------|-----|
| `typing` | Incluida | Type hints (anotaciones de tipo) |

### Librerías de Terceros

| Librería | Versión Mínima | Instalación | Uso |
|----------|----------------|-------------|-----|
| `tabulate` | 0.8.0+ | `pip install tabulate` | Formateo de tablas en consola |

---

## Instalación y Configuración

### Requisitos Previos

- **Python:** Versión 3.7 o superior
- **pip:** Gestor de paquetes de Python
- **Sistema Operativo:** Windows, macOS o Linux
- **IDE (opcional):** PyCharm, VS Code, o cualquier editor de texto

### Pasos de Instalación

#### 1. Clonar o Descargar el Proyecto

```bash
# Si usas Git
git clone <url-del-repositorio>

# O descargar manualmente y extraer en una carpeta
```

#### 2. Navegar al Directorio del Proyecto

```bash
cd GestionContactos
```

#### 3. Verificar la Versión de Python

```bash
python --version
# o
python3 --version
```

Debe mostrar Python 3.7 o superior.

#### 4. Instalar Dependencias

**Opción A: Usando pip directamente**
```bash
pip install tabulate
```

**Opción B: Si tienes un archivo requirements.txt**
```bash
pip install -r requirements.txt
```

**Opción C: Usando PyCharm**
1. Abre `Preferences` → `Project: GestionContactos` → `Python Interpreter`
2. Click en el botón `+`
3. Busca `tabulate`
4. Click en `Install Package`

#### 5. Verificar la Instalación

```bash
pip show tabulate
```

Deberías ver información sobre el paquete instalado.

#### 6. Verificar la Estructura de Archivos

Asegúrate de que existan los archivos `__init__.py`:

```
src/__init__.py
src/fuentes/__init__.py
```

Si no existen, créalos (pueden estar vacíos):

```bash
# En Linux/Mac
touch src/__init__.py
touch src/fuentes/__init__.py

# En Windows
type nul > src\__init__.py
type nul > src\fuentes\__init__.py
```

---

## Guía de Ejecución

### Ejecutar la Aplicación

#### Desde la Terminal/Consola

**En la raíz del proyecto, ejecuta:**

```bash
python Main.py
```

O en algunos sistemas:

```bash
python3 Main.py
```

#### Desde PyCharm

1. Abre el proyecto en PyCharm
2. Haz clic derecho sobre `Main.py`
3. Selecciona `Run 'Main'`

O simplemente presiona: `Ctrl + Shift + F10` (Windows/Linux) o `Cmd + Shift + R` (Mac)

### Flujo de Uso

#### 1. Inicio de la Aplicación

Al ejecutar, verás el menú principal:

```
 Menú del sistema de contactos
===============================

+----------+---------------------+
| Opción   | Acción              |
+==========+=====================+
| 1        | Agregar contacto    |
+----------+---------------------+
| 2        | Buscar contacto     |
+----------+---------------------+
| 3        | Editar contacto     |
+----------+---------------------+
| 4        | Eliminar contacto   |
+----------+---------------------+
| 5        | Listar contactos    |
+----------+---------------------+
| 9        | Salir del sistema   |
+----------+---------------------+

Seleccione una opción:
```

#### 2. Agregar un Contacto (Opción 1)

```
Agregar contacto
----------------
Nombre: Juan Pérez
Teléfono: 555-1234
Correo: juan@email.com
Dirección: Calle Principal 123

¡Contacto agregado exitosamente!
```

#### 3. Listar Contactos (Opción 5)

```
Listar contactos
----------------

+---------------+-----------+-------------------+----------------------+
| Nombre        | Teléfono  | Correo            | Dirección            |
+===============+===========+===================+======================+
| Juan Pérez    | 555-1234  | juan@email.com    | Calle Principal 123  |
+---------------+-----------+-------------------+----------------------+
```

#### 4. Buscar un Contacto (Opción 2)

```
Buscar contacto
----------------
Ingrese el nombre/teléfono del contacto a buscar: Juan Pérez
Nombre: Juan Pérez
Teléfono: 555-1234
Correo: juan@email.com
Dirección: Calle Principal 123
```

#### 5. Editar un Contacto (Opción 3)

```
Editar contacto
----------------
Contactos disponibles:

+---------------+-----------+-------------------+----------------------+
| Nombre        | Teléfono  | Correo            | Dirección            |
+===============+===========+===================+======================+
| Juan Pérez    | 555-1234  | juan@email.com    | Calle Principal 123  |
+---------------+-----------+-------------------+----------------------+

Ingrese el nombre/teléfono del contacto a editar: Juan Pérez

Datos actuales del contacto:

+---------------+-----------+-------------------+----------------------+
| Nombre        | Teléfono  | Correo            | Dirección            |
+===============+===========+===================+======================+
| Juan Pérez    | 555-1234  | juan@email.com    | Calle Principal 123  |
+---------------+-----------+-------------------+----------------------+

Ingrese los nuevos datos (presione Enter para mantener el valor actual):
Nuevo nombre (Enter para mantener 'Juan Pérez'): Juan Carlos Pérez
Nuevo teléfono (Enter para mantener '555-1234'): 
Nuevo correo (Enter para mantener 'juan@email.com'): juanc@email.com
Nueva dirección (Enter para mantener 'Calle Principal 123'): 

¡Contacto editado exitosamente!
```

#### 6. Eliminar un Contacto (Opción 4)

```
Eliminar contacto
----------------
Contactos disponibles:

+--------------------+-----------+-------------------+----------------------+
| Nombre             | Teléfono  | Correo            | Dirección            |
+====================+===========+===================+======================+
| Juan Carlos Pérez  | 555-1234  | juanc@email.com   | Calle Principal 123  |
+--------------------+-----------+-------------------+----------------------+

Ingrese el nombre/teléfono del contacto a eliminar: 555-1234

Contacto encontrado:

+--------------------+-----------+-------------------+----------------------+
| Nombre             | Teléfono  | Correo            | Dirección            |
+====================+===========+===================+======================+
| Juan Carlos Pérez  | 555-1234  | juanc@email.com   | Calle Principal 123  |
+--------------------+-----------+-------------------+----------------------+

¿Está seguro que desea eliminar este contacto? (s/n): s

Contacto eliminado exitosamente!
```

#### 7. Salir del Sistema (Opción 9)

```
Seleccione una opción: 9
Saliendo del sistema...
```

---

## Funcionalidades Detalladas

### 1. Gestión de Contactos

#### Agregar Contacto
- **Campos requeridos:** Nombre, Teléfono, Correo, Dirección
- **Validaciones:** Ninguna (versión actual acepta cualquier entrada)
- **Almacenamiento:** En memoria (lista de Python)

#### Buscar Contacto
- **Criterios de búsqueda:** Nombre exacto o Teléfono exacto
- **Case-sensitive:** Sí (debe coincidir exactamente)
- **Retorno:** Primer contacto que coincida

#### Editar Contacto
- **Búsqueda:** Por nombre o teléfono
- **Edición:** Campo por campo con opción de mantener valor actual
- **Funcionalidad:** Presionar Enter sin escribir mantiene el valor original

#### Eliminar Contacto
- **Búsqueda:** Por nombre o teléfono
- **Confirmación:** Requiere confirmación explícita (s/n)
- **Operación:** Elimina el contacto de la lista en memoria

#### Listar Contactos
- **Formato:** Tabla formateada con todos los campos
- **Orden:** Orden de inserción
- **Validación:** Muestra mensaje si no hay contactos

### 2. Interfaz de Usuario

#### Menú Principal
- **Formato:** Tabla con opciones numeradas
- **Colores:** Verde para títulos
- **Navegación:** Entrada numérica

#### Mensajes de Estado
- **Éxito:** Color verde (✓)
- **Error/Advertencia:** Color rojo
- **Información:** Color amarillo

#### Pausa entre Operaciones
- **Función:** `pausa()`
- **Propósito:** Dar tiempo al usuario para leer mensajes
- **Formato:** Mensaje en amarillo con instrucción

### 3. Validaciones

#### Validaciones Implementadas
- ✅ Verificación de lista vacía antes de buscar/editar/eliminar
- ✅ Confirmación antes de eliminar
- ✅ Validación de opción de menú válida

#### Validaciones Pendientes (Mejoras Futuras)
- ❌ Formato de correo electrónico
- ❌ Formato de número telefónico
- ❌ Campos obligatorios
- ❌ Duplicados

---

## Características Técnicas

### Almacenamiento de Datos

**Tipo:** En memoria (volatile)
- Los datos se almacenan en una lista de Python
- Los datos se pierden al cerrar la aplicación
- No hay persistencia en disco

**Estructura de datos:**
```python
self.contacto = [
    ContactoModel("Juan", "123", "j@e.com", "Calle 1"),
    ContactoModel("María", "456", "m@e.com", "Calle 2"),
    ...
]
```

### Colores ANSI en Terminal

**Códigos de escape ANSI utilizados:**

```python
RESET = "\033[0m"      # Resetea todos los atributos
NEGRITA = "\033[1m"    # Activa negrita
ROJO = "\033[31m"      # Texto rojo
VERDE = "\033[32m"     # Texto verde
AMARILLO = "\033[33m"  # Texto amarillo
```

**Compatibilidad:**
- ✅ Linux/Unix/macOS: Soporte nativo
- ✅ Windows 10+: Soporte nativo en terminal moderna
- ⚠️ Windows 7/8: Puede requerir configuración adicional

### Formato de Tablas

**Librería:** `tabulate`

**Estilo utilizado:** `grid`

**Ejemplo de salida:**
```
+----------+-----------+
| Columna1 | Columna2  |
+==========+===========+
| Dato1    | Dato2     |
+----------+-----------+
```

**Otros estilos disponibles:**
- `plain`: Sin bordes
- `simple`: Bordes mínimos
- `github`: Estilo Markdown
- `fancy_grid`: Bordes con caracteres Unicode

### Manejo de Errores

**Estrategia actual:**
- Mensajes informativos para el usuario
- Sin excepciones explícitas
- Validaciones básicas

**Ejemplo:**
```python
if len(self.contacto) == 0:
    print(f"{ROJO}No hay contactos registrados.{RESET}")
    return
```

---

## Posibles Mejoras Futuras

### 1. Persistencia de Datos

#### Opción A: Archivos JSON
```python
import json

def guardar_contactos(self):
    with open('contactos.json', 'w') as f:
        json.dump([c.__dict__ for c in self.contacto], f)

def cargar_contactos(self):
    with open('contactos.json', 'r') as f:
        data = json.load(f)
        self.contacto = [ContactoModel(**d) for d in data]
```

#### Opción B: Base de Datos SQLite
```python
import sqlite3

# Crear tabla
CREATE TABLE contactos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    telefono TEXT NOT NULL,
    correo TEXT,
    direccion TEXT
);
```

#### Opción C: CSV
```python
import csv

def exportar_csv(self):
    with open('contactos.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Nombre', 'Teléfono', 'Correo', 'Dirección'])
        for c in self.contacto:
            writer.writerow([c.nombre, c.telefono, c.correo, c.direccion])
```

### 2. Validaciones Mejoradas

```python
import re

def validar_email(email):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None

def validar_telefono(telefono):
    patron = r'^\d{3}-\d{4}$|^\d{7,}$'
    return re.match(patron, telefono) is not None
```

### 3. Búsqueda Mejorada

```python
# Búsqueda parcial
def buscar_contacto_parcial(self, termino):
    resultados = []
    for contacto in self.contacto:
        if (termino.lower() in contacto.nombre.lower() or 
            termino in contacto.telefono):
            resultados.append(contacto)
    return resultados

# Búsqueda case-insensitive
if contacto.nombre.lower() == buscar.lower():
    # encontrado
```

### 4. Ordenamiento

```python
# Ordenar por nombre
self.contacto.sort(key=lambda x: x.nombre)

# Ordenar por múltiples criterios
self.contacto.sort(key=lambda x: (x.nombre, x.telefono))
```

### 5. Exportación/Importación

```python
def exportar_contactos(self, formato='json'):
    if formato == 'json':
        # exportar a JSON
    elif formato == 'csv':
        # exportar a CSV
    elif formato == 'txt':
        # exportar a texto plano
```

### 6. Interfaz Gráfica (GUI)

**Opciones:**
- **tkinter:** Librería estándar de Python
- **PyQt5/PySide6:** Interfaces más modernas
- **Kivy:** Multiplataforma (incluyendo móviles)

### 7. Testing

```python
import unittest

class TestAgenda(unittest.TestCase):
    def setUp(self):
        self.agenda = Agenda()
    
    def test_agregar_contacto(self):
        # test
    
    def test_buscar_contacto(self):
        # test
```

### 8. Logging

```python
import logging

logging.basicConfig(
    filename='agenda.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info('Contacto agregado: Juan Pérez')
```

### 9. Configuración Externa

```python
# config.ini
[COLORES]
exito = verde
error = rojo
info = amarillo

[FORMATO]
tabla = grid
```

### 10. Autenticación

```python
# Sistema de usuarios con contraseñas
class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = hash(password)
```

---

## Conclusión

Este sistema de gestión de contactos es una aplicación educativa que demuestra:

- ✅ Programación Orientada a Objetos
- ✅ Separación de responsabilidades
- ✅ Operaciones CRUD completas
- ✅ Interfaz de usuario en consola
- ✅ Uso de librerías de terceros
- ✅ Código estructurado y mantenible

**Autor:** [Tu Nombre]  
**Fecha:** Febrero 2026  
**Versión:** 1.0

---

## Contacto y Soporte

Para preguntas, sugerencias o reporte de errores:
- **Email:** [german.riveross@gmail.com]
- **GitHub:** [https://github.com/german-rs/GestionContactos]

---

**Fin de la Documentación Técnica**