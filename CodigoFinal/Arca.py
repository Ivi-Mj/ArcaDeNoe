class Arca:
    # Atributos estáticos
    animales = []
    alimentos = []
    agua = 0
    capacidad_maxima = 0

    def __init__(cls, capacidad_maxima):
        """Inicializa el arca con capacidad máxima, listas vacías y agua a cero."""
        cls.capacidad_maxima = capacidad_maxima
        cls.animales = []
        cls.alimentos = []
        cls.agua = 0

    @classmethod
    def agregar_animal(cls, animal):
        """Agrega un animal al arca si no se supera la capacidad máxima."""
        if len(cls.animales) < cls.capacidad_maxima:
            cls.animales.append(animal)
            print(f"Animal {animal.nombre} agregado al arca.")
        else:
            raise ValueError("No hay espacio suficiente en el arca para más animales.")
    
    @classmethod
    def agregar_alimento(cls, alimento):
        """Agrega un alimento al arca."""
        cls.alimentos.append(alimento)
        print(f"Alimento {alimento.tipo} agregado al arca.")
    
    @classmethod
    def agregar_agua(cls, cantidad):
        """Agrega agua al arca."""
        cls.agua += cantidad
        print(f"{cantidad} litros de agua agregados al arca.")
    
    @classmethod
    def alimentar_animal(cls, animal):
        """Alimenta a un animal con un alimento adecuado."""
        if animal in cls.animales:
            for alimento in cls.alimentos:
                if alimento.es_alimento_adecuado(animal.tipo):
                    alimento.usar(1)
                    animal.alimentar()
                    print(f"{animal.nombre} ha sido alimentado con {alimento.tipo}.")
                    return
            print(f"No se encontró alimento adecuado para {animal.nombre}.")
        else:
            print(f"El animal {animal.nombre} no está en el arca.")
    
    @classmethod
    def dar_agua(cls, animal):
        """Da agua a un animal específico."""
        if animal in cls.animales:
            animal.dar_agua()
            print(f"{animal.nombre} ha recibido agua.")
        else:
            print(f"El animal {animal.nombre} no está en el arca.")
    
    @classmethod
    def estado_arca(cls):
        """Devuelve el estado actual del arca."""
        return {
            "Animales": len(cls.animales),
            "Alimentos": len(cls.alimentos),
            "Agua disponible": cls.agua
        }
    
    @classmethod
    def mostrar_estado_animales(cls):
        """Muestra el estado de todos los animales en el arca."""
        if cls.animales:
            print("Estado de los animales en el arca:")
            for animal in cls.animales:
                print(f"{animal.nombre} ({animal.tipo}) - {animal.estado()}")
        else:
            print("No hay animales en el arca.")