from Parte1 import Arca
from Parte3 import Perro, Gato, Vaca, Carne, Heno, Atun

# Crear la Arca con una capacidad máxima de 10
mi_arca = Arca(10)

# Crear animales
perro = Perro("Rex")
gato = Gato("Whiskers")
vaca = Vaca("Bessie")

# Crear alimentos
carne = Carne(10)
atun = Atun(5)
heno = Heno(8)

# Agregar animales y alimentos al arca
mi_arca.agregar_animal(perro)
mi_arca.agregar_animal(gato)
mi_arca.agregar_animal(vaca)

mi_arca.agregar_alimento(carne)
mi_arca.agregar_alimento(atun)
mi_arca.agregar_alimento(heno)

# Agregar agua al arca
mi_arca.agregar_agua(15)

# Alimentar y dar agua a los animales
mi_arca.alimentar_animal(perro)
mi_arca.dar_agua(perro)

mi_arca.alimentar_animal(gato)
mi_arca.dar_agua(gato)

mi_arca.alimentar_animal(vaca)
mi_arca.dar_agua(vaca)

# Ver el estado de los animales
print(perro.estado())
print(gato.estado())
print(vaca.estado())

# Ver el estado general del arca
print(mi_arca.estado_arca())