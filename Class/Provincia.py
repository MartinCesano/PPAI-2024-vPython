from typing import List
from Pais import Pais
from RegionVitivinicola import RegionVitivinicola

class Provincia:
    nombre: str
    pais: Pais
    region: List[RegionVitivinicola]
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

    def obtenerPais(self):
        return self.pais

    def getNombre(self):
        return self.nombre