from datetime import datetime
from ..Interfaces.PantallaGenerarReporteRankingVino import PantallaGenerarReporteRankingVino

class GestorGenerarReporteRankingVino:
    def __init__(self):
        self.vinos_filtrados = []

    def opcionGenerarRankingDeVinos(self):
        pass

    def tomarSeleccionFechas(self, fechaInicio, fechaFin):
        resultadoValidacion = validarFechas(self, fechaInicio, fechaFin)
        PantallaGenerarReporteRankingVino.mostrarTipoReseña(self, )
        return 

    def validarFechas(self, fechaInicio, fechaFin):
        if fechaInicio < fechaFin:
            return True
        else:
            return False

    def tomarSeleccionTipoResena(self):
        pass

    def tomarFormaVisualizacionReporte(self):
        pass

    def tomarConfirmacionReporte(self):
        pass

    def buscarVinosConResenasPorTipoYFecha(self):
        pass

    def calcularCalificacionPromedio(self):
        pass

    def ordenarVinosPorRanking(self):
        pass

    def tomar10PrimerosVinosCalificados(self):
        pass

    def buscarDatos10MejoresVino(self):
        pass

    def generarArchivo(self):
        pass