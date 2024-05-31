from datetime import datetime
from Varietal import Varietal
from Bodega import Bodega
from Resena import Resena
class Vino:
    
    nombre: str
    añada: int
    imagenEtiqueta: str
    notaDeCataBodega: float
    precio: float
    fechaActualizacion: datetime
    varietal: Varietal
    bodega: Bodega
    resena: Resena
    
    def __init__(self, nombre, añada, imagenEtiqueta, notaDeCataBodega, precio, bodega, varietal):
        self.nombre = nombre
        self.añada = añada
        self.imagenEtiqueta = imagenEtiqueta
        self.notaDeCataBodega = notaDeCataBodega
        self.precio = precio
        self.bodega = bodega
        self.varietal = varietal

    def obtenerResena(self):
        pass

    def calcularRanking(self):
        pass

    def obtenerBodega(self):
        return self.bodega

    def obtenerVarietal(self):
        return self.varietal

    def getPrecio(self):
        return self.precio

    def getNombreVino(self):
        return self.nombre