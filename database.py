
import copy
import unittest
import database as db
class TestDatabase(unittest.TestCase):
    def setUp(self):
    # Se ejecuta antes de cada prueba
        db.Clientes.lista = [
        db.Cliente('15J', 'Marta', 'Pérez'),
        db.Cliente('48H', 'Manolo', 'López'),
        db.Cliente('28Z', 'Ana', 'García')
        ]
    def test_buscar_cliente(self):
        cliente_existente = db.Clientes.buscar('15J')
        cliente_no_existente = db.Clientes.buscar('99X')
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_no_existente)
    def test_crear_cliente(self):
        nuevo_cliente = db.Clientes.crear('39X', 'Héctor', 'Costa')
        self.assertEqual(len(db.Clientes.lista), 4)
        self.assertEqual(nuevo_cliente.dni, '39X')
        self.assertEqual(nuevo_cliente.nombre, 'Héctor')
        self.assertEqual(nuevo_cliente.apellido, 'Costa')
    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar('28Z'))
        cliente_modificado = db.Clientes.modificar('28Z', 'Mariana',
        'Pérez')
        self.assertEqual(cliente_a_modificar.nombre, 'Ana')
        self.assertEqual(cliente_modificado.nombre, 'Mariana')
    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar('48H')
        cliente_rebuscado = db.Clientes.buscar('48H')
        self.assertNotEqual(cliente_borrado, cliente_rebuscado)
    if __name__ == '__main__':
        unittest.main()
        
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
