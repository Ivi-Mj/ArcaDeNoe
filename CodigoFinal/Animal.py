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
# Clases derivadas de Animal
class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "perro")

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "gato")

class Vaca(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "vaca")
