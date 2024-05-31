import tkinter as tk
from tkinter import messagebox

class PantallaGenerarReporteRankingVino:
    
    def __init__(self, master):
        self.master = master
        self.frameGenerarReporteRankingVinos = None

    def habilitarPantalla(self):
        self.frameGenerarReporteRankingVinos = tk.Frame(self.master)
        self.frameGenerarReporteRankingVinos.config(bg="white")
        self.frameGenerarReporteRankingVinos.pack(fill=tk.BOTH, expand=True)

        font_style = ("Helvetica", 20)

        label_reporte = tk.Label(self.frameGenerarReporteRankingVinos, text="Aquí va el contenido para generar el reporte de ranking de vinos", bg="white", font=font_style)
        label_reporte.pack(pady=20)

        btn_volver = tk.Button(self.frameGenerarReporteRankingVinos, text="Cancelar", command=self.volver, font=font_style)
        btn_volver.pack(pady=10)

    def volver(self):
        respuesta = messagebox.askyesno("Confirmar", "Se perderan los datos del formulario \n ¿Estás seguro de volver al Menu principal de Bonvino?")
        if respuesta:
            self.frameGenerarReporteRankingVinos.pack_forget()
            self.master.frame_principal.pack(fill=tk.BOTH, expand=True)

    def opcionGenerarRankingDeVinos(self):
        self.habilitarPantalla()
    
    def solicitarFechasInicioFin(self):
        pass

    def tomarSeleccionFechaInicio(self):
        pass
    
    def tomarSeleccionFechaFin(self):
        pass

    def mostrarTiposReporte(self,tiposReportes: list ):
        pass
    
    def solicitarSeleccionTipoReporte(self):
        pass

    def tomarSeleccionTipoReporte(self):
        pass
    
    def mostrarTipoVisualizacion(self,):
        pass

    def solicitarFormaVisualizacionReporte(self):
        pass
    
    def tomarFormaVisualizacionReporte(self):
        pass
    
    def solicitarConfirmacionReporte(self):
        pass
    
    def tomarConfirmaciónReporte(self):
        pass
    
    def mostrarConfirmacionReporte(self):
        pass