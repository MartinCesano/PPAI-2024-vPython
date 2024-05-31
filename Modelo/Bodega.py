class Bodega:
    def __init__(self, nombre, descripcion, historia, coordenadasUbicacion, periodoActualizacion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.historia = historia
        self.coordenadasUbicacion = coordenadasUbicacion
        self.periodoActualizacion = periodoActualizacion
        

    def getNombre(self):
        return self.nombre

    def obtenerUbicacion(self):
        return self.coordenadasUbicacion