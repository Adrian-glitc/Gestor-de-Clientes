
import database as db
class Cliente:
    def __init__(self, id_cliente, nombre, email, telefono):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def __repr__(self):
        return f"Cliente(id_cliente={self.id_cliente}, nombre='{self.nombre}', email='{self.email}', telefono='{self.telefono}')"

class Clientes:
    lista = []

    @staticmethod
    def crear(dni, nombre, apellido):
        cliente = db.Cliente(dni, nombre, apellido)
        Clientes.lista.append(cliente)
        return cliente

    @staticmethod
    def buscar(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente
        return None

    @staticmethod
    def modificar(dni, nombre=None, apellido=None):
        cliente = Clientes.buscar(dni)
        if cliente:
            if nombre:
                cliente.nombre = nombre
            if apellido:
                cliente.apellido = apellido
            return cliente
        return None

    @staticmethod
    def borrar(dni):
        cliente = Clientes.buscar(dni)
        if cliente:
            Clientes.lista.remove(cliente)
            return cliente
        return None
class Clientes:
# Creamos la lista y cargamos los clientes en memoria
    lista = []
    with open("clientes.csv", newline="\n") as fichero:
        reader = csv.reader(fichero, delimiter=";")
        for dni, nombre, apellido in reader:
            cliente = Cliente(dni, nombre, apellido)
            lista.append(cliente)

import helpers
def test_dni_valido(self):
    self.assertTrue(helpers.dni_valido('00A', db.Clientes.lista))
    self.assertFalse(helpers.dni_valido('23223S', db.Clientes.lista))
    self.assertFalse(helpers.dni_valido('F35', db.Clientes.lista))
    self.assertFalse(helpers.dni_valido('48H', db.Clientes.lista))
    
def guardar():
    with open("clientes.csv", "w", newline="\n") as fichero:
        writer = csv.writer(fichero, delimiter=";")
        for c in Clientes.lista:
            writer.writerow((c.dni, c.nombre, c.apellido))
            
def crear(dni, nombre, apellido):
    cliente = Cliente(dni, nombre, apellido)
    Clientes.lista.append(cliente)
    Clientes.guardar() # new
    return cliente
    @staticmethod
def modificar(dni, nombre, apellido):
    for i, cliente in enumerate(Clientes.lista):
        if cliente.dni == dni:
            Clientes.lista[i].nombre = nombre
            Clientes.lista[i].apellido = apellido
            Clientes.guardar() # new
        return Clientes.lista[i]
    @staticmethod
def borrar(dni):
    for i, cliente in enumerate(Clientes.lista):
        if cliente.dni == dni:
            cliente = Clientes.lista.pop(i)
            Clientes.guardar() # new
        return cliente