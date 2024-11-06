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

class Alimento:
    def __init__(self, tipo, cantidad):
        """Inicializa el alimento con tipo y cantidad."""
        self.tipo = tipo
        self.cantidad = cantidad
    
    def usar(self, cantidad):
        """Reduce la cantidad de alimento disponible."""
        if self.cantidad >= cantidad:
            self.cantidad -= cantidad
        else:
            print(f"No hay suficiente {self.tipo}.")
    
    @classmethod
    def es_alimento_adecuado(cls, tipo_animal):
        """Método que debe ser implementado en las clases derivadas de Alimento."""
        raise NotImplementedError("Este método debe ser implementado en la clase derivada.")

class Croquetas(Alimento):
    def __init__(self, cantidad):
        super().__init__("Croquetas", cantidad)
    
    @classmethod
    def es_alimento_adecuado(cls, tipo_animal):
        """Las croquetas son adecuadas tanto para perros como para gatos."""
        return tipo_animal in ["Perro", "Gato"]

class Heno(Alimento):
    def __init__(self, cantidad):
        super().__init__("Heno", cantidad)
    
    @classmethod
    def es_alimento_adecuado(cls, tipo_animal):
        """El heno es adecuado solo para gatos."""
        return tipo_animal == "Gato"