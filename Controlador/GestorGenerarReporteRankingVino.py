import json
import pandas as pd
from datetime import datetime
from Interfaz.PantallaGenerarReporteRankingVino import PantallaGenerarReporteRankingVino
from Modelo.Vino import Vino # type: ignore

class GestorGenerarReporteRankingVino:
    def __init__(self):
        self.tiposReportes = ["Reseñas normales", "Reseñas de Sommelier", "Reseñas de Amigos"]
        self.tipoVisualizacion = ["Excel", "PDF", "Pantalla"] 
        self.vinosFiltradosPorResena = list[Vino]
        self.vinosFiltradosPorResenaConPromedio = []
        self.fechaInicio = datetime
        self.fechaFin = datetime
        self.datosVinosRankeados = json
        ##opcionesReseña = ""
        ##tipoReseñaSeleccionada = ""

    def opcionGenerarRankingDeVinos(self):
        pass

    def tomarSeleccionFechas(self, fechaInicio, fechaFin):
        resultadoValidacion = self.validarFechas(self, fechaInicio, fechaFin)
        reportes = self.getTiposReportes()
        PantallaGenerarReporteRankingVino.mostrarTipoReseña(self, reportes)

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

#Busca y guarda los vinos que se encuentran en el rango de fecha seleccionado y que son de Sommelier
    #Args: 
        #datetime: fechaInicio, 
        #datetime: fechaFin, 
        #list[vino]: vinosFiltradosPorResena
    #Return: 
        #list: lista con los vinos filtrados que cumplen con lo solicitado
    def buscarVinosConResenasPorTipoYFecha(self, fechaInicio: datetime, fechaFin: datetime, vinos: list[Vino]):
        vinosFiltradosPorResena = list[Vino]
        for vino in vinos:
            estaEnPeriodoYEsSomelier = vino.obtenerResenas(self, fechaInicio, fechaFin)
            if estaEnPeriodoYEsSomelier:
                vinosFiltradosPorResena.append(vino)
        return vinosFiltradosPorResena

#calcula la calificacion promedio de las reseñas que esten en periodo y que sean de sommelier de cada vino
    #Args: #
        #vinosFiltradosPorReseña
    #Return: 
        #list: lista con tuplas (vino, puntaje) de los vinos que habían sido filtrados
    def calcularCalificacionPromedio(self, vinosFiltradosPorResena: list):
        vinosFiltradosPorResenaConPromedio = []
        for vino in vinosFiltradosPorResena:
            puntaje = vino.calcularRanking() ##devuelve el promedio de las calificaciones
            vinosFiltradosPorResenaConPromedio.append((vino, puntaje))
        return vinosFiltradosPorResenaConPromedio

#Toma la lista de vinos filtrados por reseña con promedio y los ordena segun el ranking    
    def ordenarVinosPorRanking(self, vinosFiltradosPorResenaConPromedio: list):
        vinosFiltradosPorResenaConPromedio.sort(key=lambda x: x[0], reverse=True)
        return vinosFiltradosPorResenaConPromedio
    
#Toma la lista vinos filtrados por resena con promedio y selecciona los 10 mejores vinos  
    def tomar10PrimerosVinosCalificados(self, vinosFiltradosPorResenaConPromedio: list):
        vinosRankeados = vinosFiltradosPorResenaConPromedio[:10]
        return vinosRankeados

#Toma la lista de los 10 vinos mejores rankeados y busca los datos
    #Args: 
        #list: vinosRankeados
    #Return: 
        #json: Con los datos de los 10 vinos mejores rakeados
    def buscarDatos10MejoresVinos(self, vinosRankeados: list):
        datosVinosRankeados = []
        for vino in vinosRankeados:
            datos_vino = {
                "nombreVino": vino.getNombre(),
                "varietales": vino.obtenerVarietal(),
                "precioVino": vino.getPrecio(),
                "nombreBodega": vino.obtenerBodega().getNombre(),
                "nombreRegion": vino.obtenerBodega().getRegionVitivinicola().getnombre(),
                "nombreProvincia": vino.obtenerBodega().getRegionVitivinicola().getProvincia().getNombre(),
                "nombrePais": vino.obtenerBodega().getRegionVitivinicola().getProvincia().getPais().getNombre(),
            }
            datosVinosRankeados.append(datos_vino)
        return json.dumps(datosVinosRankeados)

    def generarArchivo(self):
        # Convertir el JSON a un DataFrame de Pandas
        df = pd.DataFrame(self.datosVinosRankeados)
        
        # Exportar el DataFrame a un archivo Excel
        df.to_excel("ReporteRankingDeVinos.xlsx", index=False)

    def getTiposReportes(self):
        return self.tiposReportes