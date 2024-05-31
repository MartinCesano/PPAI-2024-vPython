from typing import List
from Provincia import Provincia

class Pais:
    
    nombre: str
    provincia: List[Provincia]

    def __init__(self, nombre):
        self.nombre = nombre


    def getNombre(self):
        return self.nombre


        