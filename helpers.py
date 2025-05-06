import helpers
helpers.limpiar_pantalla()

# Simulated database module for demonstration purposes
class db:
    class Clientes:
        lista = []
        
        @staticmethod
        def buscar(dni):
            for cliente in db.Clientes.lista:
                if cliente.dni == dni:
                    return cliente
            return None
        
        @staticmethod
        def crear(dni, nombre, apellido):
            db.Clientes.lista.append(Cliente(dni, nombre, apellido))
        
        @staticmethod
        def modificar(dni, nombre, apellido):
            cliente = db.Clientes.buscar(dni)
            if cliente:
                cliente.nombre = nombre
                cliente.apellido = apellido
        
        @staticmethod
        def borrar(dni):
            cliente = db.Clientes.buscar(dni)
            if cliente:
                db.Clientes.lista.remove(cliente)
                return True
            return False

class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

# Simulated user input for demonstration purposes
opcion = input("Selecciona una opción (1-6): ")
def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
elif opcion == '6':
    print("Saliendo...\n")
    exit()

if opcion == '1':
    print("Listando los clientes...\n")
    for cliente in db.Clientes.lista:
        print(cliente)

elif opcion == '2':
    print("Buscando un cliente...\n")
    dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
    cliente = db.Clientes.buscar(dni)
    print(cliente) if cliente else print("Cliente no encontrado.")

elif opcion == '3':
    print("Añadiendo un cliente...\n")
    dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
    nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)").capitalize()
    apellido = helpers.leer_texto(2, 30, "Apellido (de 2 a 30 chars)").capitalize()
    db.Clientes.crear(dni, nombre, apellido)
    print("Cliente añadido correctamente.")

elif opcion == '4':
    print("Modificando un cliente...\n")
    dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
    cliente = db.Clientes.buscar(dni)
    if cliente:
        nombre = helpers.leer_texto(2, 30, f"Nombre (de 2 a 30 chars) [{cliente.nombre}]").capitalize()
        apellido = helpers.leer_texto(2, 30, f"Apellido (de 2 a 30 chars) [{cliente.apellido}]").capitalize()
        db.Clientes.modificar(cliente.dni, nombre, apellido)
        print("Cliente modificado correctamente.")
    else:
        print("Cliente no encontrado.")

elif opcion == '5':
    print("Borrando un cliente...\n")
    dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
    print("Cliente borrado correctamente.") if db.Clientes.borrar(dni) else print("Cliente no encontrado.")

elif opcion == '6':
    print("Saliendo...\n")
    break

input("\nPresiona ENTER para continuar...")

import re
def dni_valido(dni, lista):
    if not re.match('[0-9]{2}[A-Z]$', dni):
        print("DNI incorrecto, debe cumplir el formato.")
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print("DNI utilizado por otro cliente.")
            return False
        return True