class Arca:
    animales = []
    alimentos = []
    agua = 0
    capacidad_maxima = 0

    def __init__(cls, capacidad_maxima):
        cls.capacidad_maxima = capacidad_maxima
        cls.animales = []
        cls.alimentos = []
        cls.agua = 0

    @classmethod
    def agregar_animal(cls, animal):
        if len(cls.animales) < cls.capacidad_maxima:
            cls.animales.append(animal)
            print(f"Animal {animal.nombre} agregado a la arca.")
        else:
            print("No hay espacio suficiente para más animales.")

    @classmethod
    def agregar_alimento(cls, alimento):
        cls.alimentos.append(alimento)
        print(f"Alimento {alimento.tipo} agregado a la arca.")

    @classmethod
    def agregar_agua(cls, cantidad):
        cls.agua += cantidad
        print(f"Se han añadido {cantidad} unidades de agua a la arca.")

    @classmethod
    def alimentar_animal(cls, animal):
        alimento_adecuado = None
        for alimento in cls.alimentos:
            if alimento.es_alimento_adecuado(animal.tipo):
                alimento_adecuado = alimento
                break

        if alimento_adecuado:
            alimento_adecuado.usar(1)  # Alimentamos al animal con 1 unidad de alimento.
            animal.alimentar()
            print(f"{animal.nombre} ha sido alimentado.")
        else:
            print(f"No se ha encontrado alimento adecuado para {animal.nombre}.")

    @classmethod
    def dar_agua(cls, animal):
        if cls.agua > 0:
            animal.dar_agua()
            cls.agua -= 1
            print(f"{animal.nombre} ha recibido agua.")
        else:
            print("No hay suficiente agua para dar a los animales.")

    @classmethod
    def estado_arca(cls):
        print(f"Estado actual del Arca:")
        print(f"Animales: {len(cls.animales)}")
        print(f"Alimentos: {len(cls.alimentos)}")
        print(f"Agua: {cls.agua}")
