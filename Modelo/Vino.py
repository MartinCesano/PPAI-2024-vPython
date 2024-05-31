class Vino:
    def __init__(self, nombre, añada, imagen_etiqueta, nota_de_cata, precio, bodega, varietal):
        self.nombre = nombre
        self.añada = añada
        self.imagen_etiqueta = imagen_etiqueta
        self.nota_de_cata = nota_de_cata
        self.precio = precio
        self.bodega = bodega
        self.varietal = varietal

    def obtenerResena(self):
        pass

    def calcularRanking(self):
        pass

    def obtenerBodega(self):
        return self.bodega

    def obtenerVarietal(self):
        return self.varietal

    def getPrecio(self):
        return self.precio

    def getNombreVino(self):
        return self.nombre