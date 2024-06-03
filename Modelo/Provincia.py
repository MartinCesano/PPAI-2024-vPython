from typing import List
from Modelo.RegionVitivinicola import RegionVitivinicola

class Provincia:
    nombre: str
    region: List[RegionVitivinicola]

    def __init__(self, nombre: str, region: List[RegionVitivinicola]):   
        self.nombre = nombre
        self.region = region

    def getNombre(self) -> str:
        return self.nombre


    def getRegiones(self) -> List[RegionVitivinicola]:
        return self.region

    def setNombre(self, nombre: str):
        self.nombre = nombre


    def setRegiones(self, regiones: List[RegionVitivinicola]):
        self.region = regiones

    def agregarRegion(self, region: RegionVitivinicola):
        self.region.append(region)