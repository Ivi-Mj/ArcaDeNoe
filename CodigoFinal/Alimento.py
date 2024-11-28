class Alimento:
    def __init__(self, tipo, cantidad):
        self.tipo = tipo
        self.cantidad = cantidad
    
    def usar(self, cantidad):
        if self.cantidad >= cantidad:
            self.cantidad -= cantidad
        else:
            print("No hay suficiente cantidad de alimento.")
    
    @staticmethod
    def es_alimento_adecuado(tipo_animal, tipo_alimento):
        # Define una relación simple entre tipos de animales y alimentos
        if (tipo_animal == "perro" and tipo_alimento == "carne") or \
           (tipo_animal == "gato" and tipo_alimento == "atun") or \
           (tipo_animal == "toro" and tipo_alimento == "heno"):
            return True
        return False
# Clases derivadas de Alimento
class Carne(Alimento):
    def __init__(self, cantidad):
        super().__init__("carne", cantidad)

class Atun(Alimento):
    def __init__(self, cantidad):
        super().__init__("atun", cantidad)

class Heno(Alimento):
    def __init__(self, cantidad):
        super().__init__("heno", cantidad)