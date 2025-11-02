# Clase Nodo
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Clase Jedi
class Jedi:
    def __init__(self, nombre, maestros, colores_sable, especie):
        self.name = nombre
        self.masters = maestros  # lista de maestros
        self.lightsaber_colors = colores_sable  # lista de colores
        self.species = especie

    def __str__(self):
        return f"{self.name} ({self.species})"

# Clase LinkedList
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def search(self, value, field):
        index = 0
        current = self.head
        while current:
            if getattr(current.value, field) == value:
                return index
            current = current.next
            index += 1
        return None

    def __getitem__(self, index):
        current = self.head
        i = 0
        while current:
            if i == index:
                return current.value
            current = current.next
            i += 1
        return None

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def show(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
            
# Crear lista de Jedi
list_jedi = LinkedList()

data = [
    ("Luke Skywalker", ["Obi-Wan Kenobi", "Yoda"], ["verde", "azul"], "Humano"),
    ("Obi-Wan Kenobi", ["Qui-Gon Jin"], ["azul"], "Humano"),
    ("Anakin Skywalker", ["Obi-Wan Kenobi"], ["azul", "rojo"], "Humano"),
    ("Ahsoka Tano", ["Anakin Skywalker"], ["verde", "azul", "blanco"], "Togruta"),
    ("Yoda", [], ["verde"], "Desconocida"),
    ("Mace Windu", ["Yoda"], ["violeta"], "Humano"),
    ("Kit Fisto", ["Yoda"], ["verde"], "Nautolano"),
    ("Qui-Gon Jin", ["Conde Dooku"], ["verde"], "Humano"),
    ("Rey", ["Leia Organa", "Luke Skywalker"], ["azul", "amarillo"], "Humano"),
    ("Plo Koon", ["Tyvokka"], ["naranja"], "Kel Dor"),
    ("Aayla Secura", ["Quinlan Vos"], ["azul"], "Twi'lek"),
    ("Barriss Offee", ["Luminara Unduli"], ["azul"], "Mirialana")
]

for nombre, maestros, colores, especie in data:
    list_jedi.append(Jedi(nombre, maestros, colores, especie))

# Subindice A) Listado ordenado por nombre y especie
print("#A listado ordenado por nombre y por especie:")
sorted_by_name = sorted(list_jedi, key=lambda j: j.name)
print("\nOrdenado por nombre:")
for j in sorted_by_name:
    print("-", j.name)

sorted_by_species = sorted(list_jedi, key=lambda j: j.species)
print("\nOrdenado por especie:")
for j in sorted_by_species:
    print("-", j.name, "(", j.species, ")")
print()

# Subindice B) Mostrar toda la información de Ahsoka Tano y Kit Fisto
print("#B información de Ahsoka Tano y Kit Fisto:")
for name in ["Ahsoka Tano", "Kit Fisto"]:
    idx = list_jedi.search(name, "name")
    if idx is not None:
        jedi = list_jedi[idx]
        print(f"\n{name}:")
        print("  Maestros:", ", ".join(jedi.masters) if jedi.masters else "Ninguno")
        print("  Colores de sable:", ", ".join(jedi.lightsaber_colors))
        print("  Especie:", jedi.species)
print()

# Subindice C) Mostrar todos los padawan de Yoda y Luke Skywalker
print("#C Padawan de Yoda y Luke Skywalker:")
for maestro in ["Yoda", "Luke Skywalker"]:
    print(f"\nAprendices de {maestro}:")
    found = False
    for jedi in list_jedi:
        if maestro in jedi.masters:
            print("-", jedi.name)
            found = True
    if not found:
        print("  Ninguno encontrado.")
print()

# Subinice D) Mostrar Jedi de especie Humano y Twi'lek
print("#D Jedi de especie humana y Twi'lek:")
for jedi in list_jedi:
    if jedi.species.lower() in ["humano", "twi'lek"]:
        print("-", jedi.name, "(", jedi.species, ")")
print()

# Subindice E) Listar Jedi que comienzan con A

print("#E Jedi que comienzan con A:")
for jedi in list_jedi:
    if jedi.name.startswith("A"):
        print("-", jedi.name)
print()

# Subindice F) Jedi que usaron sable de más de un color
print("#F Jedi con más de un color de sable:")
for jedi in list_jedi:
    if len(jedi.lightsaber_colors) > 1:
        print("-", jedi.name, "→", ", ".join(jedi.lightsaber_colors))
print()

# Subindic G) Jedi que usaron sable amarillo o violeta
print("#G Jedi con sable amarillo o violeta:")
for jedi in list_jedi:
    if "amarillo" in jedi.lightsaber_colors or "violeta" in jedi.lightsaber_colors:
        print("-", jedi.name)
print()

# Subindice H) Padawans de Qui-Gon Jin y Mace Windu
print("#H Padawans de Qui-Gon Jin y Mace Windu:")
for maestro in ["Qui-Gon Jin", "Mace Windu"]:
    print(f"\nPadawans de {maestro}:")
    found = False
    for jedi in list_jedi:
        if maestro in jedi.masters:
            print("-", jedi.name)
            found = True
    if not found:
        print("  Ninguno.")
print()