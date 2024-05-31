from datetime import datetime
from Vino import Vino

class Resena:

    comentario: str
    esPremium: bool
    fechaReseña: datetime
    puntaje: float
    vino: Vino
    
    def __init__(self, comentario, esPremium, fechaReseña, puntaje):
        self.comentario = comentario
        self.esPremium = esPremium
        self.fechaReseña = fechaReseña
        self.puntaje = puntaje

    def estaEnPeriodo(self):
        pass

    def sosDeSommelier(self):
        pass

    def getPuntaje(self):
        return self.puntaje