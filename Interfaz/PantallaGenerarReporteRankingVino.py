import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from tkinter import ttk

class PantallaGenerarReporteRankingVino:
    
    def __init__(self, master ):
        self.master = master
        self.gestor = None

    def setGestor(self, gestor):
        self.gestor = gestor

    def habilitarPantalla(self):
        self.frameGenerarReporteRankingVinos = tk.Frame(self.master)
        self.frameGenerarReporteRankingVinos.config(bg="white")
        self.frameGenerarReporteRankingVinos.pack(fill=tk.BOTH, expand=True)

        font_style = ("Helvetica", 20)

        label_reporte = tk.Label(self.frameGenerarReporteRankingVinos, text="Aquí va el contenido para generar el reporte de ranking de vinos", bg="white", font=font_style)
        label_reporte.pack(pady=20)

        btn_volver = tk.Button(self.frameGenerarReporteRankingVinos, text="Cancelar", command=self.volver, font=font_style)
        btn_volver.pack(pady=10)
        self.gestor.opcionGenerarRankingDeVinos()

    def volver(self):
        respuesta = messagebox.askyesno("Confirmar", "Se perderan los datos del formulario \n ¿Estás seguro de volver al Menu principal de Bonvino?")
        if respuesta:
            self.frameGenerarReporteRankingVinos.pack_forget()
            self.master.frame_principal.pack(fill=tk.BOTH, expand=True)

    def opcionGenerarRankingDeVinos(self):
        self.habilitarPantalla()
            
    def solicitarFechasInicioFin(self):
        font_style = ("Helvetica", 20)

        # Campo de selección de fecha de inicio
        label_fecha_inicio = tk.Label(self.frameGenerarReporteRankingVinos, text="Fecha Inicio:", bg="white", font=font_style)
        label_fecha_inicio.pack(padx=10, pady=5, anchor="w")
        self.calendario_inicio = Calendar(self.frameGenerarReporteRankingVinos, font=font_style)
        self.calendario_inicio.pack(padx=10, pady=5)

        # Campo de selección de fecha de fin
        label_fecha_fin = tk.Label(self.frameGenerarReporteRankingVinos, text="Fecha Fin:", bg="white", font=font_style)
        label_fecha_fin.pack(padx=10, pady=5, anchor="w")
        self.calendario_fin = Calendar(self.frameGenerarReporteRankingVinos, font=font_style)
        self.calendario_fin.pack(padx=10, pady=5)

        # Botón para guardar fechas
        btn_guardar_fechas = tk.Button(self.frameGenerarReporteRankingVinos, text="Guardar Fechas", command=self.gestor.tomarSeleccionFechaInicioFin(), font=font_style)
        btn_guardar_fechas.pack(pady=10)

    def mostrarTiposReportes(self, tiposReportes: list):
        font_style = ("Helvetica", 20)

        # Combo box para tipos de reportes
        label_tipo_reporte = tk.Label(self.frameGenerarReporteRankingVinos, text="Tipo de Reporte:", bg="white", font=font_style)
        label_tipo_reporte.pack(padx=10, pady=5, anchor="w")
        self.combo_tipos_reporte = ttk.Combobox(self.frameGenerarReporteRankingVinos, values=tiposReportes, font=font_style)
        self.combo_tipos_reporte.pack(padx=10, pady=5)

        # Botón para guardar selección de tipo de reporte
        btn_guardar_tipo_reporte = tk.Button(self.frameGenerarReporteRankingVinos, text="Guardar Tipo Reporte", command=self.gestor.tomarSeleccionTipoReporte(), font=font_style)
        btn_guardar_tipo_reporte.pack(pady=10)

    def solicitarFormaVisualizacion(self, tipoVisualizacion: list):
        font_style = ("Helvetica", 20)

        # Combo box para tipo de visualización
        label_visualizacion = tk.Label(self.frameGenerarReporteRankingVinos, text="Tipo de Visualización:", bg="white", font=font_style)
        label_visualizacion.pack(padx=10, pady=5, anchor="w")
        self.combo_visualizacion = ttk.Combobox(self.frameGenerarReporteRankingVinos, values=tipoVisualizacion, font=font_style)
        self.combo_visualizacion.pack(padx=10, pady=5)

        # Botón para guardar selección de visualización
        btn_guardar_visualizacion = tk.Button(self.frameGenerarReporteRankingVinos, text="Guardar Visualización", command=self.gestor.tomarFormaVisualizacionReporte(), font=font_style)
        btn_guardar_visualizacion.pack(pady=10)

    def solicitarConfirmacionReporte(self):
        font_style = ("Helvetica", 20)

        # Preguntar confirmación
        label_confirmacion = tk.Label(self.frameGenerarReporteRankingVinos, text="¿Confirmar generación de reporte?", bg="white", font=font_style)
        label_confirmacion.pack(padx=10, pady=5, anchor="w")

        # Botones de confirmación
        btn_confirmar = tk.Button(self.frameGenerarReporteRankingVinos, text="Confirmar", command=self.tomarConfirmacionReporte, font=font_style)
        btn_confirmar.pack(side="left", padx=10, pady=5)

        btn_cancelar = tk.Button(self.frameGenerarReporteRankingVinos, text="Cancelar", command=self.volver, font=font_style)
        btn_cancelar.pack(side="right", padx=10, pady=5)

    def tomarConfirmacionReporte(self):
        print("Reporte confirmado.")
        self.gestor.mostrarConfirmacionGeneracionReporte()

    def mostrarConfirmacionGeneracionReporte(self):
        messagebox.showinfo("Confirmación", "El reporte se ha generado correctamente.")
        self.volver()
    def tomarConfirmacionReporte(self):
        print("Reporte confirmado.")
        self.gestor.mostrarConfirmacionGeneracionReporte()

    def mostrarConfirmacionGeneracionReporte(self):
        messagebox.showinfo("Confirmación", "El reporte se ha generado correctamente.")
        self.volver()

