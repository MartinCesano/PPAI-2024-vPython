from Provincia import Provincia

class RegionVitivinicola:
    
    nombre: str
    descripcion: str
    provincia: Provincia
    
    def __init__(self, nombre, descripcion, provincia):
        self.nombre = nombre
        self.descripcion = descripcion
        self.provincia = provincia

    def getNombre(self):
        return self.nombre

    def obtenerProvincia(self):
        return self.provincia