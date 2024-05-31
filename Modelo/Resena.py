from datetime import datetime

class Resena:

    comentario: str
    esDeSommelier: bool
    fechaResena: datetime
    puntaje: float
    
    def __init__(self, comentario: str, esDeSommelier: bool, fechaResena: datetime, puntaje: float):
        self.comentario = comentario
        self.esDeSommelier = esDeSommelier
        self.fechaResena = fechaResena
        self.puntaje = puntaje

    def estaEnPeriodo(self, fechaInicio: datetime, fechaFin: datetime):
        return fechaInicio <= self.fechaResena <= fechaFin

    def sosDeSommelier(self):
        return self.esDeSommelier

    def getPuntaje(self):
        return self.puntaje
    
    def getComentario(self) -> str:
        return self.comentario

    def getEsDeSommelier(self) -> bool:
        return self.esDeSommelier

    def getFechaResena(self) -> datetime:
        return self.fechaResena


    def setComentario(self, comentario: str):
        self.comentario = comentario

    def setEsDeSommelier(self, esDeSommelier: bool):
        self.esDeSommelier = esDeSommelier

    def setFechaResena(self, fechaResena: datetime):
        self.fechaResena = fechaResena

    def setPuntaje(self, puntaje: float):
        self.puntaje = puntaje

