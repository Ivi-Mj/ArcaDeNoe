# Clase Arca
class Arca:
    def __init__(self, capacidad_maxima):
        self.capacidad_maxima = capacidad_maxima
        self.animales = []
        self.alimentos = []
        self.agua = 0

    # Método para agregar animales
    def agregar_animal(self, animal):
        if len(self.animales) + len(self.alimentos) < self.capacidad_maxima:
            self.animales.append(animal)
        else:
            print("No hay espacio suficiente en el arca para más animales.")
    
    # Método para agregar alimentos
    def agregar_alimento(self, alimento):
        if len(self.animales) + len(self.alimentos) < self.capacidad_maxima:
            self.alimentos.append(alimento)
        else:
            print("No hay espacio suficiente en el arca para más alimentos.")
    
    # Método para agregar agua
    def agregar_agua(self, cantidad):
        self.agua += cantidad
    
    # Método para alimentar a un animal
    def alimentar_animal(self, animal):
        if animal in self.animales:
            alimento = self.buscar_alimento_adecuado(animal)
            if alimento:
                alimento.usar(1)
                animal.alimentar()
                print(f"{animal.nombre} el {animal.tipo} ha sido alimentado con {alimento.tipo}")
            else:
                print(f"No hay alimento adecuado para {animal.nombre}.")
        else:
            print(f"{animal.nombre} no está en el arca.")
    
    # Método para dar agua a un animal
    def dar_agua(self, animal):
        if animal in self.animales and self.agua > 0:
            animal.dar_agua()
            self.agua -= 1
            print(f"{animal.nombre} ha recibido agua.")
        else:
            print(f"No hay agua suficiente para {animal.nombre}.")
    
    # Método para verificar el estado del arca
    def estado_arca(self):
        return f"Animales: {len(self.animales)}, Cantidad de alimentos por animal disponible: {len(self.alimentos)}, Unidades de agua disponible: {self.agua}"
    
    # Método para encontrar el alimento adecuado para un animal
    def buscar_alimento_adecuado(self, animal):
        for alimento in self.alimentos:
            if alimento.es_alimento_adecuado(animal.tipo, alimento.tipo):
                return alimento
        return None