from typing import List
from Modelo.Provincia import Provincia

class Pais:
    
    nombre: str
    provincia: List[Provincia]

    def __init__(self, nombre: str):
        self.nombre = nombre
       
    def getNombre(self) -> str:
        return self.nombre

    def getProvincias(self) -> List[Provincia]:
        return self.provincia

    def setNombre(self, nombre: str):
        self.nombre = nombre

    def setProvincias(self, provincias: List[Provincia]):
        self.provincia = provincias

    def agregarProvincia(self, provincia: Provincia):
        self.provincia.append(provincia)