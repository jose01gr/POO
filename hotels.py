import json

class Hotels():
    def __init__(self, nombre='', direccion='', telefono='', habitaciones='', nroReservas=''):
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._habitaciones = habitaciones
        self._nroReservas = nroReservas
        
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
        
    @nombre.deleter
    def nombre(self):
        del self._nombre
        
    @property
    def direccion(self):
        return self._direccion
    @direccion.setter
    def direccion(self, valor):
        self._direccion = valor
    @direccion.deleter
    def direccion(self):
        del self._direccion
    
    @property
    def telefono(self):
        return self._telefono
    @telefono.setter
    def telefono(self, valor):
        self._telefono = valor
    @telefono.deleter
    def telefono(self):
        del self._telefono
    
    @property
    def habitaciones(self):
        return self._habitaciones
    @habitaciones.setter
    def habitaciones(self, valor):
        self._habitaciones = valor
    @habitaciones.deleter
    def habitaciones(self):
        del self._habitaciones
    
    @property
    def nroReservas(self):
        return self._nroReservas
    @nroReservas.setter
    def nroReservas(self, valor):
        self._nroReservas = valor
    @nroReservas.deleter
    def nroReservas(self):
        del self._nroReservas
    
    def __str__(self):
        return f'Nombre: {self._nombre}, Dirección: {self._direccion}, Teléfono: {self._telefono}, Habitaciones: {self._habitaciones}, Nro. Reservas: {self._nroReservas}'
    
class Hotels_Encoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Hotels):
            return {'nombre': o.nombre, 'direccion': o.direccion, 'telefono': o.telefono, 'habitaciones': o.habitaciones, 'nroReservas': o.nroReservas}
        return json.JSONEncoder.default(self, o)
        
    def desde_json(diccionario):
        return Hotels(diccionario['nombre'], diccionario['direccion'], diccionario['telefono'], diccionario['habitaciones'], diccionario['nroReservas'])
    