import tkinter as tk
import random
from Interfaz.PantallaGenerarReporteRankingVino import PantallaGenerarReporteRankingVino
from Controlador.GestorGenerarReporteRankingVino import GestorGenerarReporteRankingVino
from datetime import datetime, timedelta
from Modelo.Vino import Vino
from Modelo.Varietal import Varietal
from Modelo.Bodega import Bodega
from Modelo.Resena import Resena
from Modelo.Pais import Pais
from Modelo.Provincia import Provincia
from Modelo.RegionVitivinicola import RegionVitivinicola


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        self.vinos = []

        # instanciamos los paises
        self.pais1 = Pais('Argentina')
        self.pais2 = Pais('Chile')
        self.pais3 = Pais('Espana')
        self.paises = [self.pais1, self.pais2, self.pais3]

        # instanciamos las provincias
        self.region1 = RegionVitivinicola('Valle de Uco', 'Región vitivinícola de Mendoza, famosa por sus vinos Malbec de alta calidad.')
        self.region2 = RegionVitivinicola('Valle de San Juan', 'Región destacada por sus variedades de Syrah y Bonarda.')
        self.region3 = RegionVitivinicola('Neuquén', 'Región emergente en la viticultura argentina, conocida por sus vinos de altura.')
        self.region4 = RegionVitivinicola('Cafayate', 'Región del noroeste argentino, famosa por su producción de vinos de altura.')
        self.region5 = RegionVitivinicola('La Rioja', 'Región tradicional de Argentina, conocida por su producción de vinos de altura.')
        self.region6 = RegionVitivinicola('Valle de Córdoba', 'Región emergente en la viticultura argentina, conocida por sus vinos artesanales.')
        self.region7 = RegionVitivinicola('Valle de Casablanca', 'Región costera chilena, destacada por su producción de vinos blancos y Pinot Noir.')
        self.region8 = RegionVitivinicola('Valle de Colchagua', 'Región chilena conocida por sus vinos tintos, especialmente Carmenere.')
        self.region9 = RegionVitivinicola('Valle de Maipo', 'Región principal de la viticultura chilena, destacada por sus vinos tintos de alta calidad.')
        self.region10 = RegionVitivinicola('Valle de Aconcagua', 'Región chilena reconocida por sus vinos tintos de alta gama.')
        self.region11 = RegionVitivinicola('Rioja Alta', 'Región de Espana famosa por sus vinos Tempranillo.')
        self.region12 = RegionVitivinicola('Ribera del Duero', 'Región espanola reconocida por sus vinos tintos, principalmente de la variedad Tinto Fino (Tempranillo).')
        self.region13 = RegionVitivinicola('Penedés', 'Conocida por su producción de Cava y vinos blancos.')
        self.region14 = RegionVitivinicola('Priorat', 'Región vinícola catalana famosa por sus vinos tintos de alta calidad.')
        self.region15 = RegionVitivinicola('Rías Baixas', 'Región gallega conocida por su producción de vinos blancos Albarino.')

        # Asociamos las regiones vitivinícolas a las provincias
        self.provincia1 = Provincia('Mendoza', [self.region1, self.region6])
        self.provincia2 = Provincia('San Juan', [self.region2])
        self.provincia3 = Provincia('Neuquén', [self.region3])
        self.provincia4 = Provincia('Salta', [self.region4])
        self.provincia5 = Provincia('La Rioja', [self.region5])
        self.provincia6 = Provincia('Córdoba', [self.region6])
        self.provincia7 = Provincia('Valparaíso', [self.region7])
        self.provincia8 = Provincia('Chubut', [self.region8])
        self.provincia9 = Provincia('Santiago', [self.region9])
        self.provincia10 = Provincia('Aconcagua', [self.region10])
        self.provincia11 = Provincia('La Rioja', [self.region11])
        self.provincia12 = Provincia('Burgos', [self.region12])
        self.provincia13 = Provincia('Barcelona', [self.region13])
        self.provincia14 = Provincia('Tarragona', [self.region14])
        self.provincia15 = Provincia('Pontevedra', [self.region15])
        # instanciamos las bodegas
        self.bodega1 = Bodega('Bodega Catena Zapata', 'Bodega argentina pionera en la producción de vinos de alta calidad, ubicada en Mendoza.', 'Fundada en 1902, es reconocida por sus innovaciones en viticultura y enología.', ['123', '456'], 'Periodo 1', self.region1)
        self.bodega2 = Bodega('Concha y Toro', 'La bodega más grande de Chile, conocida por su vino emblemático "Casillero del Diablo".', 'Fundada en 1883, es una de las marcas de vino más reconocidas del mundo.', ['789', '012'], 'Periodo 2', self.region3)
        self.bodega3 = Bodega('Marqués de Riscal', 'Bodega histórica de Espana, famosa por su arquitectura vanguardista y sus vinos Rioja.', 'Fundada en 1858, combina tradición e innovación en la producción de vino.', ['345', '678'], 'Periodo 3', self.region4)
        self.bodega4 = Bodega('Bodegas López', 'Una de las bodegas más antiguas de Argentina, ubicada en Mendoza.', 'Desde 1898, produce vinos con métodos tradicionales y alta calidad.', ['901', '234'], 'Periodo 4', self.region2)
        self.bodega5 = Bodega('Freixenet', 'Bodega espanola líder en la producción de Cava, ubicada en la región del Penedés.', 'Con más de 150 anos de historia, es conocida por su excelencia en vinos espumosos.', ['567', '890'], 'Periodo 5', self.region5)
        self.bodegas = [self.bodega1, self.bodega2, self.bodega3, self.bodega4, self.bodega5]

        # instanciamos las resenas
        self.resena1 = Resena('Un vino elegante y equilibrado, con notas a frutos rojos y especias.', True, datetime(2024, 1, 5), 4)       
        self.resena2 = Resena('Un vino con gran estructura y taninos firmes. Ideal para maridar con carnes rojas.', True, datetime(2024, 4, 20), 5)
        self.resena3 = Resena('Un vino suave y fácil de beber, perfecto para cualquier ocasión.', True, datetime(2024, 3, 10), 4)
        self.resena4 = Resena('Excelente relación calidad-precio. Lo recomendaría sin dudarlo.', True, datetime(2024, 2, 28), 4)
        self.resena5 = Resena('Un vino con gran potencial de guarda, ideal para disfrutar en ocasiones especiales.', True, datetime(2023, 11, 15), 5)
        self.resena6 = Resena('Sabor a frutas maduras con un toque de vainilla. ¡Delicioso!', True, datetime(2023, 10, 5), 5)
        self.resena7 = Resena('Buen vino para maridar con carnes asadas. Probablemente lo vuelva a comprar.', True, datetime(2022, 9, 20), 4)
        self.resena8 = Resena('Un vino robusto con taninos bien integrados. Perfecto para los amantes del Malbec.', True, datetime(2022, 8, 12), 5)
        self.resena9 = Resena('Refrescante y burbujeante. Ideal para brindar en celebraciones.', True, datetime(2023, 5, 30), 4)
        self.resena10 = Resena('Buena relación calidad-precio. Perfecto para compartir con amigos.', True, datetime(2023, 4, 18), 4)
        self.resena11 = Resena('Un vino con gran potencial de guarda, ideal para disfrutar en ocasiones especiales.', True, datetime(2023, 3, 10), 5)
        self.resena12 = Resena('Sabor a frutas maduras con un toque de vainilla. ¡Delicioso!', True, datetime(2023, 2, 5), 5)
        self.resena13 = Resena('Buen vino para maridar con carnes asadas. Probablemente lo vuelva a comprar.', True, datetime(2023, 1, 20), 4)
        self.resena14 = Resena('Un vino robusto con taninos bien integrados. Perfecto para los amantes del Malbec.', True, datetime(2022, 12, 12), 5)
        self.resena15 = Resena('Refrescante y burbujeante. Ideal para brindar en celebraciones.', True, datetime(2022, 11, 30), 4)
        self.resena16 = Resena('Buena relación calidad-precio. Perfecto para compartir con amigos.', True, datetime(2022, 10, 18), 4)
        self.resena17 = Resena('Un vino con gran potencial de guarda, ideal para disfrutar en ocasiones especiales.', True, datetime(2022, 9, 10), 5)
        self.resena18 = Resena('Sabor a frutas maduras con un toque de vainilla. ¡Delicioso!', True, datetime(2022, 8, 5), 5)
        self.resena19 = Resena('Buen vino para maridar con carnes asadas. Probablemente lo vuelva a comprar.', True, datetime(2022, 7, 20), 4)
        self.resena20 = Resena('Un vino robusto con taninos bien integrados. Perfecto para los amantes del Malbec.', True, datetime(2022, 6, 12), 5)
        self.resena21 = Resena('Refrescante y burbujeante. Ideal para brindar en celebraciones.', True, datetime(2022, 5, 30), 4)
        self.resena22 = Resena('Buena relación calidad-precio. Perfecto para compartir con amigos.', True, datetime(2022, 4, 18), 4)
        self.resena23 = Resena('Un vino con gran potencial de guarda, ideal para disfrutar en ocasiones especiales.', True, datetime(2022, 3, 10), 5)
        self.resena24 = Resena('Sabor a frutas maduras con un toque de vainilla. ¡Delicioso!', True, datetime(2022, 2, 5), 5)
        self.resena25 = Resena('Buen vino para maridar con carnes asadas. Probablemente lo vuelva a comprar.', True, datetime(2022, 1, 20), 4)
        self.resena26 = Resena('Un vino robusto con taninos bien integrados. Perfecto para los amantes del Malbec.', True, datetime(2021, 12, 12), 5)
        self.resena27 = Resena('Refrescante y burbujeante. Ideal para brindar en celebraciones.', True, datetime(2021, 11, 30), 4)
        self.resena28 = Resena('Buena relación calidad-precio. Perfecto para compartir con amigos.', True, datetime(2021, 10, 18), 4)
        self.resena29 = Resena('Un vino con gran potencial de guarda, ideal para disfrutar en ocasiones especiales.', True, datetime(2021, 9, 10), 5)
        self.resena30 = Resena('Sabor a frutas maduras con un toque de vainilla. ¡Delicioso!', True, datetime(2021, 8, 5), 5)
        self.resena31 = Resena('Buen vino para maridar con carnes asadas. Probablemente lo vuelva a comprar.', True, datetime(2021, 7, 20), 4)
        self.resena32 = Resena('Un vino robusto con taninos bien integrados. Perfecto para los amantes del Malbec.', True, datetime(2021, 6, 12), 5)
        self.resena33 = Resena('Refrescante y burbujeante. Ideal para brindar en celebraciones.', True, datetime(2021, 5, 30), 4)
        self.resena34 = Resena('Buena relación calidad-precio. Perfecto para compartir con amigos.', True, datetime(2021, 4, 18), 4)
        self.resena35 = Resena('Un vino con gran potencial de guarda, ideal para disfrutar en ocasiones especiales.', True, datetime(2021, 3, 10), 5)
        self.resena36 = Resena('Sabor a frutas maduras con un toque de vainilla. ¡Delicioso!', True, datetime(2021, 2, 5), 5)   
        self.resena37 = Resena('Buen vino para maridar con carnes asadas. Probablemente lo vuelva a comprar.', True, datetime(2021, 1, 20), 4)
        self.resena38 = Resena('Un vino robusto con taninos bien integrados. Perfecto para los amantes del Malbec.', True, datetime(2020, 12, 12), 5)
        self.resena39 = Resena('Refrescante y burbujeante. Ideal para brindar en celebraciones.', True, datetime(2020, 11, 30), 4)
        self.resena40 = Resena('Buena relación calidad-precio. Perfecto para compartir con amigos.', True, datetime(2020, 10, 18), 4)
        self.resena41 = Resena('Un vino con gran potencial de guarda, ideal para disfrutar en ocasiones especiales.', True, datetime(2020, 9, 10), 5)
        self.resena42 = Resena('Sabor a frutas maduras con un toque de vainilla. ¡Delicioso!', True, datetime(2020, 8, 5), 5)
        self.resena43 = Resena('Buen vino para maridar con carnes asadas. Probablemente lo vuelva a comprar.', True, datetime(2020, 7, 20), 4)
        self.resena44 = Resena('Un vino robusto con taninos bien integrados. Perfecto para los amantes del Malbec.', True, datetime(2020, 6, 12), 5)
        self.resena45 = Resena('Refrescante y burbujeante. Ideal para brindar en celebraciones.', True, datetime(2020, 5, 30), 4)
        self.resena46 = Resena('Buena relación calidad-precio. Perfecto para compartir con amigos.', True, datetime(2020, 4, 18), 4)
        self.resena47 = Resena('Un vino con gran potencial de guarda, ideal para disfrutar en ocasiones especiales.', True, datetime(2020, 3, 10), 5)
        self.resena48 = Resena('Sabor a frutas maduras con un toque de vainilla. ¡Delicioso!', True, datetime(2020, 2, 5), 5)
        self.resena49 = Resena('Buen vino para maridar con carnes asadas. Probablemente lo vuelva a comprar.', True, datetime(2020, 1, 20), 4)
        self.resena50 = Resena('Un vino robusto con taninos bien integrados. Perfecto para los amantes del Malbec.', True, datetime(2019, 12, 12), 5)


        # Agrega más resenas aquí...

        self.resenas = [self.resena1, self.resena2, self.resena3, self.resena4, self.resena5, self.resena6, self.resena7, self.resena8, self.resena9, self.resena10] 
        # instanciamos los varietales
        # Instanciación de los varietales 
        self.varietal1 = Varietal('Malbec', 100)
        self.varietal2 = Varietal('Cabernet Sauvignon', 60)
        self.varietal3 = Varietal('Chardonnay', 80)
        self.varietal4 = Varietal('Merlot', 70)
        self.varietal5 = Varietal('Cava', 90)
        self.varietal6 = Varietal('Rosado', 50)
        self.varietal7 = Varietal('Blanc de Blancs', 60)
        self.varietal8 = Varietal('Tannat', 75)
        self.varietal9 = Varietal('Sauvignon Blanc', 55)
        self.varietal10 = Varietal('Verdejo', 65)
        self.varietal11 = Varietal('Brut Nature', 85)
        self.varietal12 = Varietal('Pinot Noir', 70)
        self.varietal13 = Varietal('Syrah', 75)
        self.varietal14 = Varietal('Bonarda', 55)
        self.varietal15 = Varietal('Tempranillo', 80)

        # instanciamos los vinos
        # Instanciación de los vinos (continuación)''
        self.vino1 = Vino("Catena Zapata Malbec", 2023, "imagen1.jpg", 3, 900, self.bodega1, [self.varietal1], [self.resena1, self.resena4, self.resena7])
        self.vino2 = Vino("Concha y Toro Cabernet Sauvignon", 2022, "imagen2.jpg", 4, 700, self.bodega2, [self.varietal2], [self.resena2, self.resena5, self.resena8])
        self.vino3 = Vino("Marqués de Riscal Reserva", 2023, "imagen3.jpg", 4, 800, self.bodega3, [self.varietal2], [self.resena3, self.resena6, self.resena9])
        self.vino4 = Vino("Concha y Toro Syrah", 2022, "imagen4.jpg", 4, 600, self.bodega2, [self.varietal2], [self.resena2, self.resena5, self.resena8])
        self.vino5 = Vino("Bodega López Bonarda", 2023, "imagen5.jpg", 3, 700, self.bodega4, [self.varietal1], [self.resena1, self.resena4, self.resena7])
        self.vino6 = Vino("Catena Zapata Chardonnay", 2023, "imagen6.jpg", 4, 900, self.bodega1, [self.varietal3], [self.resena10, self.resena13, self.resena16])
        self.vino7 = Vino("Casillero del Diablo Merlot", 2024, "imagen7.jpg", 3, 750, self.bodega2, [self.varietal4], [self.resena11, self.resena14, self.resena17])
        self.vino8 = Vino("Marqués de Riscal Gran Reserva", 2022, "imagen8.jpg", 4, 850, self.bodega3, [self.varietal2], [self.resena12, self.resena15, self.resena18])
        self.vino9 = Vino("Bodega López Malbec", 2023, "imagen9.jpg", 3, 650, self.bodega4, [self.varietal1], [self.resena19, self.resena22, self.resena25])
        self.vino10 = Vino("Freixenet Cava", 2021, "imagen10.jpg", 5, 500, self.bodega5, [self.varietal5], [self.resena20, self.resena23, self.resena26])
        self.vino11 = Vino("Catena Zapata Cabernet Franc", 2022, "imagen11.jpg", 4, 750, self.bodega1, [self.varietal2], [self.resena21, self.resena24, self.resena27])
        self.vino12 = Vino("Casillero del Diablo Carmenere", 2023, "imagen12.jpg", 3, 700, self.bodega2, [self.varietal4], [self.resena22, self.resena25, self.resena28])
        self.vino13 = Vino("Marqués de Riscal Rosado", 2022, "imagen13.jpg", 4, 600, self.bodega3, [self.varietal6], [self.resena23, self.resena26, self.resena29])
        self.vino14 = Vino("Bodega López Cabernet Sauvignon", 2024, "imagen14.jpg", 3, 800, self.bodega4, [self.varietal2], [self.resena24, self.resena27, self.resena30])
        self.vino15 = Vino("Freixenet Blanc de Blancs", 2023, "imagen15.jpg", 5, 700, self.bodega5, [self.varietal7], [self.resena25, self.resena28, self.resena31])
        self.vino16 = Vino("Catena Zapata Tannat", 2022, "imagen16.jpg", 4, 600, self.bodega1, [self.varietal8], [self.resena26, self.resena29, self.resena32])
        self.vino17 = Vino("Casillero del Diablo Sauvignon Blanc", 2023, "imagen17.jpg", 3, 650, self.bodega2, [self.varietal9], [self.resena27, self.resena30, self.resena33])
        self.vino18 = Vino("Marqués de Riscal Verdejo", 2023, "imagen18.jpg", 4, 750, self.bodega3, [self.varietal10], [self.resena28, self.resena31, self.resena34])
        self.vino19 = Vino("Bodega López Merlot", 2022, "imagen19.jpg", 3, 700, self.bodega4, [self.varietal4], [self.resena29, self.resena32, self.resena35])
        self.vino20 = Vino("Freixenet Brut Nature", 2024, "imagen20.jpg", 5, 800, self.bodega5, [self.varietal11], [self.resena30, self.resena33, self.resena36])

        self.vinos = [self.vino1, self.vino2, self.vino3, self.vino4, self.vino5, self.vino6, self.vino7, self.vino8, self.vino9, self.vino10, self.vino11, self.vino12, self.vino13, self.vino14, self.vino15, self.vino16, self.vino17, self.vino18, self.vino19, self.vino20]

        super().__init__()
        self.title("Bonvino")
        self.state('zoomed')

        self.frame_principal = tk.Frame(self)
        self.frame_principal.pack(fill=tk.BOTH, expand=True)

        font_style = ("Helvetica", 24)

        btn_generar_reporte = tk.Button(self.frame_principal, text="Generar Reporte Ranking Vino", command=self.mostrar_frame_reporte, font=font_style)
        btn_generar_reporte.pack(pady=20)

        self.pantalla_generar_reporte = PantallaGenerarReporteRankingVino(self)  # Aquí se pasa la referencia del gestor
        self.gestor_generar_reporte = GestorGenerarReporteRankingVino(self.pantalla_generar_reporte, self.vinos)
        self.pantalla_generar_reporte.setGestor(self.gestor_generar_reporte)
        
    def random_datetime(start, end):
        return start + timedelta(
            seconds=random.randint(0, int((end - start).total_seconds())))

    def mostrar_frame_reporte(self):
        self.frame_principal.pack_forget()
        self.pantalla_generar_reporte.opcionGenerarRankingDeVinos()

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()