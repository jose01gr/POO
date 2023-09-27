import json

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        
class Reservacion:
    def _init_(self, nombre_hotel, fecha_reserva, fecha_llegada, fecha_salida, personas,
                tipo_habitacion, numero_habitacion, estadia, estado_reserva,
                check_in, check_out, precio, pago, notas_adicionales, id_reservacion):
        self._nombre_hotel = nombre_hotel
        self._fecha_reserva = fecha_reserva
        self._fecha_llegada = fecha_llegada
        self._fecha_salida = fecha_salida
        self._numero_habitacion = numero_habitacion
        self._tipo_habitacion = tipo_habitacion
        self._personas = personas
        self._estadia = estadia
        self._precio = precio
        self._pago = pago
        self._notas_adicionales = notas_adicionales
        self._estado_reserva = estado_reserva
        self._check_in = check_in
        self._check_out = check_out
        self._id_reservacion = id_reservacion
        
    class Cola:
        def __init__(self):
            self.frente = None
            self.fin = None
        
        def esta_vacia(self):
            return self.frente is None
        
        def agregar(self, valor):
            nodo_nuevo = Nodo(valor)
            if self.esta_vacia():
                self.frente = nodo_nuevo
            else:
                self.fin.siguiente = nodo_nuevo
                self.fin = nodo_nuevo
        
        def eliminar(self):
            if self.esta_vacia():
                return None
            else:
                valor_eliminado = self.frente.valor
                self.frente = self.frente.siguiente
                if self.frente is None:
                    self.fin = None
                return valor_eliminado
        
        def ver_frente(self):
            if self.esta_vacia():
                return None
            else:
                return self.frente.valor
        
        def recorrer(self):
            if self.esta_vacia():
                print("La cola está vacía")
            else:
                self._recorrer_aux(self.frente)
        
        def _recorrer_aux(self, nodo):
            if nodo is not None:
                print(nodo.valor.nombre)
                self._recorrer_aux(nodo.siguiente)
    