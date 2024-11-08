class Animal:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.hambre = 10
        self.sed = 10
    
    def alimentar(self):
        if self.hambre > 0:
            self.hambre -= 1
        else:
            print(f"{self.nombre} ya no tiene hambre.")
    
    def dar_agua(self):
        if self.sed > 0:
            self.sed -= 1
        else:
            print(f"{self.nombre} ya no tiene sed.")
    
    def estado(self):
        return f"{self.nombre} - Hambre: {self.hambre}, Sed: {self.sed}"

# Clase Alimento
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
           (tipo_animal == "vaca" and tipo_alimento == "heno"):
            return True
        return False