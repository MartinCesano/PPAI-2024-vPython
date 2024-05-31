import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

class EjemploFrame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejemplo Frame")
        self.geometry("400x300")

        self.frame = tk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Campo de entrada de texto
        self.label_nombre = tk.Label(self.frame, text="Nombre:")
        self.label_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_nombre = tk.Entry(self.frame)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=5)

        # Campo de selección de fecha
        self.label_fecha = tk.Label(self.frame, text="Fecha:")
        self.label_fecha.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.calendario = Calendar(self.frame)
        self.calendario.grid(row=1, column=1, padx=10, pady=5)

        # Botón
        self.boton_guardar = tk.Button(self.frame, text="Guardar", command=self.guardar_datos)
        self.boton_guardar.grid(row=2, column=0, columnspan=2, pady=10)

        # Selección de opciones
        self.label_opcion = tk.Label(self.frame, text="Opción:")
        self.label_opcion.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.combo_opciones = ttk.Combobox(self.frame, values=["Opción 1", "Opción 2", "Opción 3"])
        self.combo_opciones.grid(row=3, column=1, padx=10, pady=5)
        self.combo_opciones.current(0)  # Selecciona el primer elemento por defecto

    def guardar_datos(self):
        nombre = self.entry_nombre.get()
        fecha = self.calendario.get_date()
        opcion = self.combo_opciones.get()
        print("Nombre:", nombre)
        print("Fecha:", fecha)
        print("Opción:", opcion)

if __name__ == "__main__":
    app = EjemploFrame()
    app.mainloop()
