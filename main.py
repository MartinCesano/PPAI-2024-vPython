import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from Controlador import GestorGenReporteRankingVino
from Interfaz import  PantallaGenReporteRankingVino
from Modelo import Pais, Provincia, Resena, RegionVitivinicola, Varietal, Vino, Bodega


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión Vitivinícola")
        self.geometry("500x400")
        self.resenas = []

        self.tabControl = ttk.Notebook(self)
        
        self.region_tab = ttk.Frame(self.tabControl)
        self.provincia_tab = ttk.Frame(self.tabControl)
        self.pais_tab = ttk.Frame(self.tabControl)
        self.bodega_tab = ttk.Frame(self.tabControl)
        self.varietal_tab = ttk.Frame(self.tabControl)
        self.vino_tab = ttk.Frame(self.tabControl)
        self.resena_tab = ttk.Frame(self.tabControl)
        
        self.tabControl.add(self.region_tab, text='Región')
        self.tabControl.add(self.provincia_tab, text='Provincia')
        self.tabControl.add(self.pais_tab, text='País')
        self.tabControl.add(self.bodega_tab, text='Bodega')
        self.tabControl.add(self.varietal_tab, text='Varietal')
        self.tabControl.add(self.vino_tab, text='Vino')
        self.tabControl.add(self.resena_tab, text='Resena')
        
        self.tabControl.pack(expand=1, fill="both")
        
        self.create_region_tab()
        self.create_provincia_tab()
        self.create_pais_tab()
        self.create_bodega_tab()
        self.create_varietal_tab()
        self.create_vino_tab()
        self.create_resena_tab()
        
    def create_region_tab(self):
        label = ttk.Label(self.region_tab, text="Nombre de la Región Vitivinícola:")
        label.pack(padx=10, pady=10)
        self.region_entry = ttk.Entry(self.region_tab)
        self.region_entry.pack(padx=10, pady=10)
        self.region_button = ttk.Button(self.region_tab, text="Guardar", command=self.save_region)
        self.region_button.pack(padx=10, pady=10)
        
    def save_region(self):
        nombre = self.region_entry.get()
        self.region = RegionVitivinicola(nombre)
        messagebox.showinfo("Información", f"Región '{nombre}' guardada exitosamente.")
        
    def create_provincia_tab(self):
        label = ttk.Label(self.provincia_tab, text="Nombre de la Provincia:")
        label.pack(padx=10, pady=10)
        self.provincia_entry = ttk.Entry(self.provincia_tab)
        self.provincia_entry.pack(padx=10, pady=10)
        self.provincia_button = ttk.Button(self.provincia_tab, text="Guardar", command=self.save_provincia)
        self.provincia_button.pack(padx=10, pady=10)
        
    def save_provincia(self):
        nombre = self.provincia_entry.get()
        self.provincia = Provincia(nombre, self.region)
        messagebox.showinfo("Información", f"Provincia '{nombre}' guardada exitosamente.")

    def create_pais_tab(self):
        label = ttk.Label(self.pais_tab, text="Nombre del País:")
        label.pack(padx=10, pady=10)
        self.pais_entry = ttk.Entry(self.pais_tab)
        self.pais_entry.pack(padx=10, pady=10)
        self.pais_button = ttk.Button(self.pais_tab, text="Guardar", command=self.save_pais)
        self.pais_button.pack(padx=10, pady=10)

    def save_pais(self):
        nombre = self.pais_entry.get()
        self.pais = Pais(nombre)
        messagebox.showinfo("Información", f"País '{nombre}' guardado exitosamente.")
        
    def create_bodega_tab(self):
        label = ttk.Label(self.bodega_tab, text="Nombre de la Bodega:")
        label.pack(padx=10, pady=10)
        self.bodega_entry = ttk.Entry(self.bodega_tab)
        self.bodega_entry.pack(padx=10, pady=10)
        self.bodega_button = ttk.Button(self.bodega_tab, text="Guardar", command=self.save_bodega)
        self.bodega_button.pack(padx=10, pady=10)
        
    def save_bodega(self):
        nombre = self.bodega_entry.get()
        self.bodega = Bodega(nombre, self.provincia)
        messagebox.showinfo("Información", f"Bodega '{nombre}' guardada exitosamente.")
        
    def create_varietal_tab(self):
        label = ttk.Label(self.varietal_tab, text="Nombre del Varietal:")
        label.pack(padx=10, pady=10)
        self.varietal_entry = ttk.Entry(self.varietal_tab)
        self.varietal_entry.pack(padx=10, pady=10)
        self.varietal_button = ttk.Button(self.varietal_tab, text="Guardar", command=self.save_varietal)
        self.varietal_button.pack(padx=10, pady=10)
        
    def save_varietal(self):
        nombre = self.varietal_entry.get()
        self.varietal = Varietal(nombre)
        messagebox.showinfo("Información", f"Varietal '{nombre}' guardado exitosamente.")
        
    def create_vino_tab(self):
        label = ttk.Label(self.vino_tab, text="Nombre del Vino:")
        label.pack(padx=10, pady=10)
        self.vino_entry = ttk.Entry(self.vino_tab)
        self.vino_entry.pack(padx=10, pady=10)
        self.vino_button = ttk.Button(self.vino_tab, text="Guardar", command=self.save_vino)
        self.vino_button.pack(padx=10, pady=10)
        
    def save_vino(self):
        nombre = self.vino_entry.get()
        self.vino = Vino(nombre, self.bodega, self.varietal)
        messagebox.showinfo("Información", f"Vino '{nombre}' guardado exitosamente.")
        
    def create_resena_tab(self):
        label_vino = ttk.Label(self.resena_tab, text="Nombre del Vino:")
        label_vino.pack(padx=10, pady=10)
        self.resena_vino_entry = ttk.Entry(self.resena_tab)
        self.resena_vino_entry.pack(padx=10, pady=10)

        label_calificacion = ttk.Label(self.resena_tab, text="Calificación (1-5):")
        label_calificacion.pack(padx=10, pady=10)
        self.resena_calificacion_entry = ttk.Entry(self.resena_tab)
        self.resena_calificacion_entry.pack(padx=10, pady=10)

        label_comentario = ttk.Label(self.resena_tab, text="Comentario:")
        label_comentario.pack(padx=10, pady=10)
        self.resena_comentario_entry = ttk.Entry(self.resena_tab)
        self.resena_comentario_entry.pack(padx=10, pady=10)
        
        self.resena_button = ttk.Button(self.resena_tab, text="Guardar", command=self.save_resena)
        self.resena_button.pack(padx=10, pady=10)

        self.export_button = ttk.Button(self.resena_tab, text="Exportar a Excel", command=self.export_to_excel)
        self.export_button.pack(padx=10, pady=10)
        
    def save_resena(self):
        vino_nombre = self.resena_vino_entry.get()
        calificacion = int(self.resena_calificacion_entry.get())
        comentario = self.resena_comentario_entry.get()
        vino = Vino(vino_nombre, self.bodega, self.varietal)
        resena = Resena(vino, calificacion, comentario)
        self.resenas.append(resena)
        messagebox.showinfo("Información", "Resena guardada exitosamente.")
        
    def export_to_excel(self):
        data = {
            "Vino": [resena.vino.nombre for resena in self.resenas],
            "Bodega": [resena.vino.bodega.nombre for resena in self.resenas],
            "Varietal": [resena.vino.varietal.nombre for resena in self.resenas],
            "Calificación": [resena.calificacion for resena in self.resenas],
            "Comentario": [resena.comentario for resena in self.resenas]
        }
        df = pd.DataFrame(data)
        df.to_excel("reporte_vinos.xlsx", index=False)
        messagebox.showinfo("Información", "Reporte exportado a 'reporte_vinos.xlsx'.")

if __name__ == "__main__":
    app = App()
    app.mainloop()
