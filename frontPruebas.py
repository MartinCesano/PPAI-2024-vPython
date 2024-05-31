import tkinter as tk
from Interfaz.PantallaGenerarReporteRankingVino import PantallaGenerarReporteRankingVino


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bonvino")
        self.state('zoomed')

        self.frame_principal = tk.Frame(self)
        self.frame_principal.pack(fill=tk.BOTH, expand=True)

        font_style = ("Helvetica", 24)

        btn_generar_reporte = tk.Button(self.frame_principal, text="Generar Reporte Ranking Vino", command=self.mostrar_frame_reporte, font=font_style)
        btn_generar_reporte.pack(pady=20)

        self.pantalla_reporte = PantallaGenerarReporteRankingVino(self)
        self.pantalla_reporte.opcionGenerarRankingDeVinos()
        self.pantalla_reporte.frameGenerarReporteRankingVinos.pack_forget()

    def mostrar_frame_reporte(self):
        self.frame_principal.pack_forget()
        self.pantalla_reporte.frameGenerarReporteRankingVinos.pack()

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()