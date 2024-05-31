import unittest
from datetime import datetime
from unittest.mock import Mock
from Modelo.Vino import Vino
from Modelo.Resena import Resena
from Modelo.Bodega import Bodega
from Modelo.RegionVitivinicola import RegionVitivinicola
from Controlador.GestorGenerarReporteRankingVino import GestorGenerarReporteRankingVino

class TestGestorGenerarReporteRankingVino(unittest.TestCase):

    def setUp(self):
        # Crear instancias de RegionVitivinicola y Bodega
        self.region_vitivinicola = RegionVitivinicola("villa maria", "villa maria")
        self.bodega = Bodega("Bodega XYZ", "Descripción de la bodega", "Historia de la bodega", ["30.0000° S", "69.0000° W"], "2024", self.region_vitivinicola)

        # Crear instancias de Vino
        self.vino1 = Vino("Vino A", 2020, "imagen.jpg", 4.5, 25.0, self.bodega, ["Varietal 1"])
        self.vino2 = Vino("Vino B", 2019, "imagen.jpg", 4.2, 30.0, self.bodega, ["Varietal 2"])

        # Crear instancias de Resena
        self.resena1 = Resena("Reseña 1", datetime(2022, 1, 1), "Sommelier", 4.5)
        self.resena2 = Resena("Reseña 2", datetime(2022, 3, 1), "Amigo", 4.0)
        self.resena3 = Resena("Reseña 3", datetime(2022, 2, 1), "Sommelier", 4.8)

        # Asignar reseñas a los vinos
        self.vino1.setResenas([self.resena1, self.resena2])
        self.vino2.setResenas([self.resena3])

        # Crear mock para pantalla
        self.mock_pantalla = Mock()

    def test_buscarVinosConResenasPorTipoYFecha(self):
        # Configurar fechas
        fecha_inicio = datetime(2022, 1, 1)
        fecha_fin = datetime(2022, 3, 1)

        # Crear instancia de GestorGenerarReporteRankingVino con mock pantalla
        gestor = GestorGenerarReporteRankingVino(self.mock_pantalla)

        # Ejecutar el método buscarVinosConResenasPorTipoYFecha
        vinos_filtrados = gestor.buscarVinosConResenasPorTipoYFecha(fecha_inicio, fecha_fin, [self.vino1, self.vino2])

        # Verificar que se devuelvan los vinos con reseñas de Sommelier en el rango de fechas
        self.assertEqual(len(vinos_filtrados), 2)
        self.assertIn(self.vino1, vinos_filtrados)
        self.assertIn(self.vino2, vinos_filtrados)

        # Verificar que se devuelvan solo los vinos con reseñas de Sommelier en el rango de fechas
        for vino in vinos_filtrados:
            self.assertTrue(any(resena.tipo == "Sommelier" for resena in vino.getResenas()))

if __name__ == '__main__':
    unittest.main()
