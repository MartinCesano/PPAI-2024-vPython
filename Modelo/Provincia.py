from typing import List
from .Pais import Pais

class Provincia:
    nombre: str
    pais: Pais

    def __init__(self, nombre: str, pais: Pais):
        self.nombre = nombre
        self.pais = pais

    def getNombre(self) -> str:
        return self.nombre

    def obtenerPais(self) -> Pais:
        return self.pais.getNombre()


    def setNombre(self, nombre: str):
        self.nombre = nombre

    def setPais(self, pais: Pais):
        self.pais = pais
