class Animal:
    def __init__(self, nombre, tipo):
        """Inicializa un animal con su nombre, tipo, hambre y sed."""
        self.nombre = nombre
        self.tipo = tipo
        self.hambre = 10  # Nivel inicial de hambre
        self.sed = 10     # Nivel inicial de sed

    def alimentar(self):
        """Reduce el nivel de hambre del animal."""
        if self.hambre > 0:
            self.hambre -= 1
        else:
            print(f"{self.nombre} ya no tiene hambre.")
    
    def dar_agua(self):
        """Reduce el nivel de sed del animal."""
        if self.sed > 0:
            self.sed -= 1
        else:
            print(f"{self.nombre} ya no tiene sed.")
    
    def estado(self):
        """Devuelve el estado de hambre y sed del animal."""
        return f"Hambre: {self.hambre}, Sed: {self.sed}"

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "Perro")
        self.hambre = 8
        self.sed = 8

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "Gato")
        self.hambre = 6
        self.sed = 6