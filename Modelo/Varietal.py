class Varietal:
    def __init__(self, descripcion, porcentajeComposicion):
        self.descripcion = descripcion
        self.porcentajeComposicion = porcentajeComposicion

    def esDeTipoUva(self):
        return True