from datetime import datetime
from typing import List
from Modelo.Varietal import Varietal
from Modelo.Bodega import Bodega
from Modelo.Resena import Resena

class Vino:
    
    nombre: str
    añada: int
    imagenEtiqueta: str
    notaDeCataBodega: float
    precio: float
    fechaActualizacion: str
    varietal: list[Varietal]
    bodega: Bodega
    resenas: list[Resena]
    
    
    def __init__(self, nombre: str, añada: int, imagenEtiqueta: str, notaDeCataBodega: float, precio: float, bodega: Bodega, varietal: list[Varietal], resenas: list[Resena]):
        self.nombre = nombre
        self.añada = añada
        self.imagenEtiqueta = imagenEtiqueta
        self.notaDeCataBodega = notaDeCataBodega
        self.precio = precio
        self.bodega = bodega
        self.varietal = varietal
        self.resenas = resenas

#calcularRanking: Obtiene las reseñas que estan en el periodo de fecha ingresado.
    #Args: 
        #datetime: fechaInicio
        #datetime: fechaFin
    #Return: 
        #boolean: devuelve un true si esta en periodo y es de sommelier, false en caso contrario.
    def obtenerResenas(self, fechaInicio:datetime, fechaFin:datetime) -> bool:
        for i in range(len(self.resenas)):
            resena = self.resenas[i]
            if resena.estaEnPeriodo(fechaInicio,fechaFin) and resena.sosDeSommelier():
                return True
        return False
    
#calcularRanking: Calcula el ranking de un vino en base a las reseñas de los sommeliers que se encuentran en el periodo de fecha actual.
    #Args: 
        #ninguno
    #Return: 
        #int: el promedio de las calificaciones del vino en el periodo de fecha actual.
    def calcularRanking(self, fechaInicio:datetime, fechaFin:datetime) -> float:
        puntaje = 0
        contadorReseña = 0
        for resena in self.resenas:
            if resena.estaEnPeriodo(fechaInicio,fechaFin) and resena.sosDeSommelier():
                contadorReseña += 1
                puntaje += resena.getPuntaje()
        if contadorReseña != 0:
            return puntaje/contadorReseña
        else:
            return 0
    #obtenerBodega: Obtiene el nombre y la ubicacion de la bodega del vino.
        #Args: 
            #ninguno
        #Return: 
            #list [nombreBodega, ubicacionBodega]: devuelve el nombre y la ubicacion de la bodega del vino.
    def obtenerBodega(self) -> Bodega:
        nombreBodega = self.bodega.getNombre()
        ubicacionBodega = self.bodega.obtenerUbicacion()
        return [nombreBodega, ubicacionBodega]
    
    #obtenerVarietal: Obtiene el nombre y la ubicacion de la bodega del vino.
        #Args: 
            #ninguno
        #Return: 
            #list [varietalDescripcion]: devuelve las descripciones del varietal que tiene el vino.
    def obtenerVarietal(self) -> Varietal:
        varietalDescripcion = []
        for unvarietal in self.varietal:
            varietalDescripcion.append(unvarietal.getDescripcion())
        return varietalDescripcion

    def getPrecioVino(self) -> float:
         return self.precio

    def getNombreVino(self) -> str:
        return self.nombre

    def getAñada(self) -> int:
        return self.añada

    def getImagenEtiqueta(self) -> str:
        return self.imagenEtiqueta

    def getNotaDeCataBodega(self) -> float:
        return self.notaDeCataBodega

    def getFechaActualizacion(self) -> str:
        return self.fechaActualizacion

    def setNombreVino(self, nombre: str):
        self.nombre = nombre

    def setAñada(self, añada: int):
        self.añada = añada

    def setImagenEtiqueta(self, imagenEtiqueta: str):
        self.imagenEtiqueta = imagenEtiqueta

    def setNotaDeCataBodega(self, notaDeCataBodega: float):
        self.notaDeCataBodega = notaDeCataBodega

    def setPrecioVino(self, precio: float):
        self.precio = precio

    def setFechaActualizacion(self, fechaActualizacion: str):
        self.fechaActualizacion = fechaActualizacion

    def setVarietal(self, varietal: Varietal):
        self.varietal = varietal

    def setBodega(self, bodega: Bodega):
        self.bodega = bodega

    def setResenas(self, resenas: List[Resena]):
        self.resenas = resenas

    def agregarResena(self, resena: Resena):
        self.resenas.append(resena)