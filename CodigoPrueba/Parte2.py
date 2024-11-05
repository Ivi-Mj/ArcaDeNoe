class Animal:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.hambre = 5
        self.sed = 5

    def alimentar(self):
        if self.hambre > 0:
            self.hambre -= 1

    def dar_agua(self):
        if self.sed > 0:
            self.sed -= 1

    def estado(self):
        return {"hambre": self.hambre, "sed": self.sed}


class Alimento:
    def __init__(self, tipo, cantidad):
        self.tipo = tipo
        self.cantidad = cantidad

    def usar(self, cantidad):
        if self.cantidad >= cantidad:
            self.cantidad -= cantidad

    @staticmethod
    def es_alimento_adecuado(tipo_animal):
        tipos_adecuados = {
            "perro": "croquetas",
            "gato": "croquetas",
            "vaca": "heno",
            "oveja": "heno"
        }
        return tipos_adecuados.get(tipo_animal) == tipo_animal