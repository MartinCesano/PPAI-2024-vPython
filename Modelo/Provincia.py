from typing import List
from Pais import Pais
from RegionVitivinicola import RegionVitivinicola

class Provincia:
    nombre: str
    pais: Pais
    region: List[RegionVitivinicola]

    def __init__(self, nombre: str, pais: Pais):
        self.nombre = nombre
        self.pais = pais

    def getNombre(self) -> str:
        return self.nombre

    def obtenerPais(self) -> Pais:
        nombrePais = self.pais.getNombre()
        return self.pais

    def getRegiones(self) -> List[RegionVitivinicola]:
        return self.region

    def setNombre(self, nombre: str):
        self.nombre = nombre

    def setPais(self, pais: Pais):
        self.pais = pais

    def setRegiones(self, regiones: List[RegionVitivinicola]):
        self.region = regiones

    def agregarRegion(self, region: RegionVitivinicola):
        self.region.append(region)