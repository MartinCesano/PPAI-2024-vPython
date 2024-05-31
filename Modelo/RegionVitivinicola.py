from Provincia import Provincia

class RegionVitivinicola:
    
    nombre: str
    descripcion: str
    provincia: Provincia
    
    def __init__(self, nombre: str, descripcion: str, provincia: Provincia):
        self.nombre = nombre
        self.descripcion = descripcion
        self.provincia = provincia

    def getNombre(self) -> str:
        return self.nombre

    def getDescripcion(self) -> str:
        return self.descripcion

    def obtenerProvincia(self) -> Provincia:
        nombreProvincia = self.provincia.getNombre()
        nombrePais = self.provincia.obtenerPais()
        return [nombreProvincia, nombrePais]

    def setNombre(self, nombre: str):
        self.nombre = nombre

    def setDescripcion(self, descripcion: str):
        self.descripcion = descripcion

    def setProvincia(self, provincia: Provincia):
        self.provincia = provincia