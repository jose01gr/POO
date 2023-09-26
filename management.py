import json
from hotels import *
import os

class Management():
    AGREGAR_HOTEL = 1
    CONSULTAR_HOTEL = 1
    SALIR = 0
    
    def __init__(self):
        self._hoteles = []
        self.recuperar_hoteles('hoteles.json')
        
    def __del__(self):
        self.almacenar_hoteles('hoteles.json')
    
    @property
    def hoteles(self):
        return self._hoteles
    
    @hoteles.setter
    def hoteles(self, valor):
        self._hoteles = valor

    @hoteles.deleter
    def hoteles(self):
        del self._hoteles
        
    def recuperar_hoteles(self, ruta):
        with open(ruta, 'r') as archivo:
            datahoteles = json.load(archivo)
        for hotel in datahoteles['hoteles']:
                self.hoteles.append(Hotels_Encoder.desde_json(hotel))
    
    def almacenar_hoteles(self, ruta):
        with open(ruta, 'w') as archivo:
            json.dump({'hoteles':self.hoteles}, archivo, cls=Hotels_Encoder, indent=4)
    
    def agregarHotel(self):
        os.system('cls')
        print('                Agregar Hotel')
        nombre = input('nombre: ')
        direccion = input('direccion: ')
        telefono = input('telefono: ')
        habitaciones = int(input('Habitaciones disponibles: '))
        nroReservas = int(input('numero de reservas: '))
        self.hoteles.append(Hotels(nombre, direccion, telefono, habitaciones, nroReservas))
        
    def consultar_hoteles(self):
        os.system('cls')
        print('                Consultar Hoteles')
        if len(self.libros) == 0:
            for hotel in self.hoteles:
                print(f'{hotel}')
                print('-'*50)
            
    def consultar_hotel(self):
        os.system('cls')
        print('                Consultar Hotel')
        nombre = input('nombre: ')
        for hotel in self.hoteles:
            if hotel.nombre == nombre:
                print(hotel)
                break
        else:
            print('Hotel no encontrado')
    
    def menu(self):
        continuar = True
        while continuar:
            os.system('cls')
            print(f'''
                  {Management.AGREGAR_HOTEL}) Agregar Hotel
                  {Management.CONSULTAR_HOTEL}) Consultar hotel
                  {Management.SALIR}) Salir
                  ''')
            opc = input('Seleccione una opcion')
            try:
                opc = int(opc)
            except:
                opc = -1
            if opc == Management.AGREGAR_HOTEL:
                self.agregarHotel()
            elif opc == Management.CONSULTAR_HOTEL:
                self.consultar_hotel()
            elif opc == Management.SALIR:
                continuar = False
            else:
                os.system('cls')
                print('Opcion no valida')
            input('Presiona enter para continuar')
        input('Presiona Enter para salir')
