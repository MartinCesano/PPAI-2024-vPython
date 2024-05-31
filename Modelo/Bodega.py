from typing import List
from RegionVitivinicola import RegionVitivinicola 

class Bodega:
    nombre: str
    descripcion: str
    historia: str
    coordenadasUbicacion: List[str]
    periodoActualizacion: str 
    regionVitivinicola: RegionVitivinicola

    def __init__(self, nombre: str, descripcion: str, historia: str, coordenadasUbicacion: list, periodoActualizacion: str, regionVitivinicola: RegionVitivinicola ):
        self.nombre = nombre
        self.descripcion = descripcion
        self.historia = historia
        self.coordenadasUbicacion = coordenadasUbicacion
        self.periodoActualizacion = periodoActualizacion
        self.regionVitivinicola = regionVitivinicola

    def getNombre(self) -> str:
        return self.nombre
    
    def getDescripcion(self) -> str:
        return self.descripcion

    def getHistoria(self) -> str:
        return self.historia
    
    def obtenerUbicacion(self) -> List[str]:
        nombreRegionVitivinicola = self.regionVitivinicola.getNombre()
        [provincia, pais] = self.regionVitivinicola.getProvincia()
        return [nombreRegionVitivinicola, provincia, pais]

    def getPeriodoActualizacion(self) -> str:
        return self.periodoActualizacion

    def getRegionVitivinicola(self) -> RegionVitivinicola:
        return self.regionVitivinicola

    def setNombre(self, nombre: str):
        self.nombre = nombre

    def setDescripcion(self, descripcion: str):
        self.descripcion = descripcion

    def setHistoria(self, historia: str):
        self.historia = historia

    def setUbicacion(self, coordenadasUbicacion: List[str]):
        self.coordenadasUbicacion = coordenadasUbicacion

    def setPeriodoActualizacion(self, periodoActualizacion: str):
        self.periodoActualizacion = periodoActualizacion

    def setRegionVitivinicola(self, regionVitivinicola: RegionVitivinicola):
        self.regionVitivinicola = regionVitivinicola
