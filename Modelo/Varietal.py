class Varietal:
    
    descripcion: str
    porcentajeComposicion: int

    def __init__(self, descripcion: str, porcentajeComposicion: int):
        self.descripcion = descripcion
        self.porcentajeComposicion = porcentajeComposicion

    def getDescripcion(self):
        return self.descripcion

    def getPorcentajeComposicion(self) -> int:
        return self.porcentajeComposicion

    def setDescripcion(self, descripcion: str):
        self.descripcion = descripcion

    def setPorcentajeComposicion(self, porcentajeComposicion: int):
        self.porcentajeComposicion = porcentajeComposicion

