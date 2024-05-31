from typing import List

class Pais:
    
    nombre: str

    def __init__(self, nombre: str):
        self.nombre = nombre
       
    def getNombre(self) -> str:
        return self.nombre

    def setNombre(self, nombre: str):
        self.nombre = nombre
