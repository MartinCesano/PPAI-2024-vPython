import json
import pandas as pd
from datetime import datetime
from Modelo.Vino import Vino 
from tkinter import messagebox

class GestorGenerarReporteRankingVino:
    def __init__(self,pantalla):
        self.pantalla = pantalla
        self.fechaInicio = datetime
        self.fechaFin = datetime
        self.tiposReportes = ["Reseñas normales", "Reseñas de Sommelier", "Reseñas de Amigos"]
        self.tipoReporteSeleccionado = str
        self.tipoVisualizacion = ["Excel", "PDF", "Pantalla"] 
        self.tipoVisualizacionSeleccionada = str
        self.confirmacionReporte = bool
        self.vinosFiltradosPorResena = list[Vino]
        self.vinosFiltradosPorResenaConPromedio = list
        self.vinosRankeados = list
        self.vinosRanking10 = list
        self.datosVinosRankeados = json
    
    def convertir_fecha(self,fecha_str):
        # Convertir la cadena de texto a un objeto datetime
        fecha = datetime.strptime(fecha_str, '%m/%d/%y')
        
        # Formatear la fecha a "dd/mm/yy" y convertir a objeto datetime
        fecha_formateada_str = fecha.strftime('%d/%m/%y')
        fecha_formateada = datetime.strptime(fecha_formateada_str, '%d/%m/%y')
        return  fecha_formateada
    
    def opcionGenerarRankingDeVinos(self):
        self.pantalla.solicitarFechasInicioFin()
        self.pantalla.mostrarYSolicitarTiposReportes(self.tiposReportes)
        self.pantalla.solicitarFormaVisualizacion(self.tipoVisualizacion)
        self.pantalla.solicitarConfirmacionReporte()

    def tomarSeleccionFechaInicioFin(self,fechaInicio, fechaFin):
        if self.validarFechas(self.convertir_fecha(fechaInicio), self.convertir_fecha(fechaFin)):
            self.fechaInicio = self.convertir_fecha(fechaInicio)
            self.fechaFin = self.convertir_fecha(fechaFin)

            print("Fechas seleccionadas: ", self.fechaInicio, self.fechaFin)
        else:
            messagebox.showerror("Error", "La fecha de inicio debe ser menor a la fecha de fin.")
    
    def tomarSeleccionTipoReporte(self, tipoReporteSeleccionado: str):
        print("Tipo de reporte seleccionado: ", tipoReporteSeleccionado)
        self.tipoReporteSeleccionado = tipoReporteSeleccionado
    
    def tomarFormaVisualizacionReporte(self, tipoVisualizacionSeleccionada: str):
        print("Forma de visualización seleccionada: ", tipoVisualizacionSeleccionada)
        self.tipoVisualizacionSeleccionada = tipoVisualizacionSeleccionada
    
    def tomarConfirmacionReporte(self):
        print("Reporte generado con éxito.")
        self.vinosFiltradosPorResena = self.buscarVinosConResenasPorTipoYFecha(self.fechaInicio, self.fechaFin, self.vinosFiltradosPorResena)
        self.vinosFiltradosPorResenaConPromedio = self.calcularCalificacionPromedio(self.vinosFiltradosPorResena)
        self.vinosRankeados = self.ordenarVinosPorRanking(self.vinosFiltradosPorResenaConPromedio)
        self.vinosRanking10 = self.tomar10PrimerosVinosCalificados(self.vinosRankeados)
        self.datosVinosRankeados = self.buscarDatos10MejoresVinos(self.vinosRanking10)
        self.generarArchivo()

    def validarFechas(self, fechaInicio, fechaFin):
        if fechaInicio < fechaFin:
            return True
        else:
            return False

    def tomarSeleccionTipoResena(self):
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
        vinosRanking10 = vinosFiltradosPorResenaConPromedio[:10]
        return vinosRanking10

#Toma la lista de los 10 vinos mejores rankeados y busca los datos
    #Args: 
        #list: vinosRankeados
    #Return: 
        #json: Con los datos de los 10 vinos mejores rakeados
    def buscarDatos10MejoresVinos(self, vinosRanking10: list):
        datosVinosRankeados = []
        for vino in vinosRanking10:
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
        return True

    def getTiposReportes(self):
        return self.tiposReportes
    
   