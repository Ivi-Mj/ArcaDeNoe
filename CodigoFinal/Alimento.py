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