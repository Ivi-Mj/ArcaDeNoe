from Parte2 import Animal, Alimento
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