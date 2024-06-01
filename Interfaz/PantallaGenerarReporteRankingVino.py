import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from tkinter import ttk

class PantallaGenerarReporteRankingVino:

    def __init__(self, master):
        self.master = master
        self.gestor = None

        self.frameGenerarReporteRankingVinos = tk.Frame(self.master, bg="white")

        

        self.frameGenerarReporteRankingVinos.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.frameGenerarReporteRankingVinos, bg="white")
        self.scrollbar = ttk.Scrollbar(self.frameGenerarReporteRankingVinos, orient="vertical", command=self.canvas.yview)
        self.formulario = tk.Frame(self.canvas, bg="white")
        
        self.formulario.grid_columnconfigure(0, weight=3)
        self.formulario.grid_columnconfigure(1, weight=2)   
        self.formulario.grid_columnconfigure(2, weight=3)
        self.formulario.grid_rowconfigure(0, weight=1)
        self.formulario.grid_rowconfigure(1, weight=1)
        self.formulario.grid_rowconfigure(2, weight=1)
        self.formulario.grid_rowconfigure(3, weight=1)
        self.formulario.grid_rowconfigure(4, weight=1)
        self.formulario.grid_rowconfigure(5, weight=1)
        self.formulario.grid_rowconfigure(6, weight=1)
        self.formulario.grid_rowconfigure(7, weight=1)
        self.formulario.grid_rowconfigure(8, weight=1)
        self.formulario.grid_rowconfigure(9, weight=1)
        self.formulario.grid_rowconfigure(10, weight=1)
        self.formulario.grid_rowconfigure(11, weight=1)
        self.formulario.grid_rowconfigure(12, weight=1)
        self.formulario.grid_rowconfigure(13, weight=1)

        self.formulario.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.formulario, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def setGestor(self, gestor):
        self.gestor = gestor

    def volver(self):
        respuesta = messagebox.askyesno("Cancelar Reporte", "Se perderán los datos del formulario \n ¿Estás seguro de volver al Menú principal de Bonvino?")
        if respuesta:
            self.frameGenerarReporteRankingVinos.pack_forget()
            self.master.frame_principal.pack(fill=tk.BOTH, expand=True)

    def opcionGenerarRankingDeVinos(self):
        self.habilitarPantalla()

    def habilitarPantalla(self):
        for widget in self.formulario.winfo_children():
            widget.destroy()
        
        font_style = ("Helvetica", 12)  # Cambiar el tamaño de la fuente

        # Botón de volver
        btn_volver = tk.Button(self.formulario, text="Volver", command=self.volver, font=font_style)
        btn_volver.grid(row=0, column=0, pady=5, sticky="w")

        self.gestor.opcionGenerarRankingDeVinos()

    def solicitarFechasInicioFin(self):
        font_style = ("Helvetica", 12) # Cambiar el tamaño de la fuente
        calendar_style = ("Arial", 5)  

        # Campo de selección de fecha de inicio
        label_fecha_inicio = tk.Label(self.formulario, text="Fecha Inicio:", bg="white", font=font_style)
        label_fecha_inicio.grid(row=1, column=1, padx=10, pady=2, sticky="ew")
        self.calendario_inicio = Calendar(self.formulario, font=calendar_style, selectmode='day')
        self.calendario_inicio.grid(row=2, column=1, padx=10, pady=2, sticky="ew")

        # Campo de selección de fecha de fin
        label_fecha_fin = tk.Label(self.formulario, text="Fecha Fin:", bg="white", font=font_style)
        label_fecha_fin.grid(row=3, column=1, padx=10, pady=2, sticky="ew")
        self.calendario_fin = Calendar(self.formulario, font=calendar_style, selectmode='day')
        self.calendario_fin.grid(row=4, column=1, padx=10, pady=2, sticky="ew")

        # Botón para guardar fechas
        btn_guardar_fechas = tk.Button(self.formulario, text="Guardar Fechas", command=self.tomarSeleccionFechaInicioFin, font=font_style)
        btn_guardar_fechas.grid(row=5, column=1, pady=5, sticky="ew")

    def mostrarTiposReportes(self, tiposReportes: list):
        font_style = ("Helvetica", 12)  # Cambiar el tamaño de la fuente

        # Combo box para tipos de reportes
        label_tipo_reporte = tk.Label(self.formulario, text="Tipo de Reporte:", bg="white", font=font_style)
        label_tipo_reporte.grid(row=6, column=1, padx=10, pady=2, sticky="ew")
        self.combo_tipos_reporte = ttk.Combobox(self.formulario, values=tiposReportes, font=font_style)
        self.combo_tipos_reporte.grid(row=7, column=1, padx=10, pady=2, sticky="ew")

        # Botón para guardar selección de tipo de reporte
        btn_guardar_tipo_reporte = tk.Button(self.formulario, text="Guardar Tipo Reporte", command=self.tomarSeleccionTipoReporte(), font=font_style)
        btn_guardar_tipo_reporte.grid(row=8, column=1, pady=5, sticky="ew")

    def solicitarFormaVisualizacion(self, tipoVisualizacion: list):
        font_style = ("Helvetica", 12)  # Cambiar el tamaño de la fuente

        # Combo box para tipo de visualización
        label_visualizacion = tk.Label(self.formulario, text="Tipo de Visualización:", bg="white", font=font_style)
        label_visualizacion.grid(row=9, column=1, padx=10, pady=2, sticky="ew")
        self.combo_visualizacion = ttk.Combobox(self.formulario, values=tipoVisualizacion, font=font_style)
        self.combo_visualizacion.grid(row=10, column=1, padx=10, pady=2, sticky="ew")

        # Botón para guardar selección de visualización
        btn_guardar_visualizacion = tk.Button(self.formulario, text="Guardar Visualización", command=self.tomarFormaVisualizacionReporte, font=font_style)
        btn_guardar_visualizacion.grid(row=11, column=1, pady=5, sticky="ew")

    def solicitarConfirmacionReporte(self):
        font_style = ("Helvetica", 12)  # Cambiar el tamaño de la fuente

        # Preguntar confirmación
        label_confirmacion = tk.Label(self.formulario, text="¿Confirmar generación de reporte?", bg="white", font=font_style)
        label_confirmacion.grid(row=2, column=2, padx=10, pady=2, sticky="ew")

        # Botones de confirmación
        btn_confirmar = tk.Button(self.formulario, text="Confirmar", command=self.tomarConfirmacionReporte, font=font_style)
        btn_confirmar.grid(row=3, column=2, padx=10, pady=2, sticky="ew")

        btn_cancelar = tk.Button(self.formulario, text="Cancelar", command=self.volver, font=font_style)
        btn_cancelar.grid(row=4, column=2, padx=10, pady=2, sticky="ew")

    def mostrarConfirmacionGeneracionReporte(self):
        messagebox.showinfo("Confirmación", "El reporte se ha generado correctamente.")
        self.volver()

    def tomarSeleccionFechaInicioFin(self):
        self.gestor.tomarSeleccionFechaInicioFin()

    def tomarSeleccionTipoReporte(self):
        self.gestor.tomarSeleccionTipoReporte()

    def tomarFormaVisualizacionReporte(self):
        self.gestor.tomarFormaVisualizacionReporte()
    
    def tomarConfirmacionReporte(self):
        self.gestor.tomarConfirmacionReporte()

