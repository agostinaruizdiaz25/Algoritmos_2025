# Clase Nodo
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Clase Superhero (modelo de cada héroe)
class Superhero:
    def __init__(self, nombre, año, casa, bio):
        self.name = nombre
        self.first_appearance = año
        self.comic_house = casa
        self.short_bio = bio

    def __str__(self):
        return f"{self.name} ({self.comic_house}, {self.first_appearance})"

# Clase LinkedList para manejar la lista de superhéroes

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

    def delete_value(self, value, field):
        prev = None
        current = self.head
        while current:
            if getattr(current.value, field) == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return f"{value} eliminado correctamente."
            prev = current
            current = current.next
        return f"{value} no se encontró."

    def search(self, value, field):
        index = 0
        current = self.head
        while current:
            if getattr(current.value, field) == value:
                return index
            index += 1
            current = current.next
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

    def show(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

# Crear lista de superhéroes
data = [
    ("Linterna Verde", 1940, "DC", "Usa un anillo de poder con su traje especial."),
    ("Wolverine", 1974, "Marvel", "Mutante con garras de adamantium y factor curativo."),
    ("Dr. Strange", 1963, "Marvel", "Hechicero supremo, maestro de las artes místicas."),
    ("Capitana Marvel", 1968, "Marvel", "Piloto con poderes cósmicos y traje militar."),
    ("Mujer Maravilla", 1941, "DC", "Guerrera amazona con armadura mágica."),
    ("Flash", 1940, "DC", "El hombre más rápido del mundo."),
    ("Star-Lord", 1976, "Marvel", "Aventurero espacial con máscara y traje especial."),
    ("Batman", 1939, "DC", "El caballero oscuro con traje y gadgets."),
    ("Spider-Man", 1962, "Marvel", "Joven héroe con traje arácnido."),
    ("Superman", 1938, "DC", "El hombre de acero con armadura invulnerable.")
]

list_superhero = LinkedList()
for nombre, año, casa, bio in data:
    list_superhero.append(Superhero(nombre, año, casa, bio))

# Subindice A) Eliminar Linterna Verde

print("#A eliminar a Linterna Verde")
print(list_superhero.delete_value('Linterna Verde', 'name'))
print()

# Subindice B) Mostrar año aparición de Wolverine
print("#B año de aparición de Wolverine")
index = list_superhero.search('Wolverine', 'name')
if index is not None:
    print(list_superhero[index].first_appearance)
else:
    print("El superhéroe no está en la lista.")
print()

# Subindice C) Cambiar la casa de Dr. Strange a Marvel

print("#C cambiar casa de Dr. Strange a Marvel")
index = list_superhero.search('Dr. Strange', 'name')
if index is not None:
    hero = list_superhero[index]
    hero.comic_house = 'DC'
    print("Nueva casa:", hero.comic_house)
else:
    print("Dr. Strange no está en la lista.")
print()

# Subindice D) Mostrar héroes que mencionan “traje” o “armadura”

print("#D héroes con 'traje' o 'armadura' en la biografía:")
for hero in list_superhero:
    if 'traje' in hero.short_bio.lower() or 'armadura' in hero.short_bio.lower():
        print("-", hero.name)
print()

# Subindice E) Héroes con fecha anterior a 1963

print("#E héroes anteriores a 1963:")
for hero in list_superhero:
    if hero.first_appearance < 1963:
        print(f"- {hero.name} ({hero.comic_house})")
print()

# Subindice F) Casa de Capitana Marvel y Mujer Maravilla

print("#F casa de Capitana Marvel y Mujer Maravilla:")
for name in ["Capitana Marvel", "Mujer Maravilla"]:
    idx = list_superhero.search(name, "name")
    if idx is not None:
        print(f"{name}: {list_superhero[idx].comic_house}")
print()

# Subindice G) Información completa de Flash y Star-Lord

print("#G información de Flash y Star-Lord:")
for name in ["Flash", "Star-Lord"]:
    idx = list_superhero.search(name, "name")
    if idx is not None:
        hero = list_superhero[idx]
        print(f"\n{name}:")
        print(f"  Año: {hero.first_appearance}")
        print(f"  Casa: {hero.comic_house}")
        print(f"  Bio: {hero.short_bio}")
print()

# Subindice H) Héroes que comienzan con B, M o S

print("#H héroes que comienzan con B, M o S:")
for hero in list_superhero:
    if hero.name.startswith(("B", "M", "S")):
        print("-", hero.name)
print()

# Subindice I) Cantidad de superhéroes por casa

print("#I cantidad de superhéroes por casa:")
conteo = {"Marvel": 0, "DC": 0}
for hero in list_superhero:
    if hero.comic_house in conteo:
        conteo[hero.comic_house] += 1
for casa, cantidad in conteo.items():
    print(f"{casa}: {cantidad}")