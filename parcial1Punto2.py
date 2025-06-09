from typing import Any
from super_heroes_data import superheroes

#Clases necesarias 
class Queue:
    def __init__(self):
        self.__elements = []

    def arrive(self, value: Any) -> None:
        self.__elements.append(value)

    def attention(self):
        return self.__elements.pop(0) if self.__elements else None

    def size(self):
        return len(self.__elements)

    def on_front(self):
        return self.__elements[0] if self.__elements else None

    def move_to_end(self):
        if self.__elements:
            value = self.attention()
            self.arrive(value)
            return value

    def show(self):
        for i in range(len(self.__elements)):
            print(self.move_to_end())


class List:
    def __init__(self):
        self.data = []
        self.criterios = {}

    def add_criterion(self, name, func):
        self.criterios[name] = func

    def append(self, item):
        self.data.append(item)

    def search(self, value, criterio=''):
        if criterio and criterio in self.criterios:
            key = self.criterios[criterio]
            for i, item in enumerate(self.data):
                if key(item) == value:
                    return i
        else:
            for i, item in enumerate(self.data):
                if item == value:
                    return i
        return None

    def delete_value(self, value, criterio=''):
        index = self.search(value, criterio)
        if index is not None:
            return self.data.pop(index)
        return None

    def sort_by_criterion(self, criterio):
        if criterio in self.criterios:
            self.data.sort(key=self.criterios[criterio])

    def __getitem__(self, index):
        return self.data[index]

    def __iter__(self):
        return iter(self.data)

    def show(self):
        for item in self.data:
            print(item)

class Superhero:
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    def __str__(self):
        return f"{self.name}, {self.real_name} - {'Villano' if self.is_villain else 'Héroe'}"
    
#Criterios
def order_by_name(item):
    return item.name

def order_by_real_name(item):
    return item.real_name

def order_by_year(item):
    return item.first_appearance

#Carga de lista
list_superhero = List()
list_superhero.add_criterion('name', order_by_name)
list_superhero.add_criterion('real_name', order_by_real_name)
list_superhero.add_criterion('year', order_by_year)

for data in superheroes:
    hero = Superhero(
        name=data["name"],
        alias=data["alias"],
        real_name=data["real_name"],
        short_bio=data["short_bio"],
        first_appearance=data["first_appearance"],
        is_villain=data["is_villain"]
    )
    list_superhero.append(hero)

#Subindice A-
list_superhero.sort_by_criterion('name')
print("A. Personajes ordenados por nombre:")
list_superhero.show()

#Subindice B-
print("B. Posición de The Thing y Rocket Raccoon:")
for name in ["The Thing", "Rocket Raccoon"]:
    index = list_superhero.search(name, 'name')
    if index is not None:
        print(f"{name} está en la posición {index}")
    else:
        print(f"{name} no se encontró")

#Subindice C-
print("C. Villanos:")
for hero in list_superhero:
    if hero.is_villain:
        print(hero)

#Subindice D-
villanos_queue = Queue()
for hero in list_superhero:
    if hero.is_villain:
        villanos_queue.arrive(hero)

print("D. Villanos con primera aparición antes de 1980:")
for _ in range(villanos_queue.size()):
    villano = villanos_queue.move_to_end()
    if villano.first_appearance < 1980:
        print(villano)

#Subindice E-
print("E. Superhéroes que comienzan con Bl, G, My o W:")
for hero in list_superhero:
    if not hero.is_villain and hero.name.startswith(("Bl", "G", "My", "W")):
        print(hero)
        
#Subindice G-
print("G. Superhéroes ordenados por año de aparición:")
superheroes_only = List()
superheroes_only.add_criterion('year', order_by_year)
for hero in list_superhero:
    if not hero.is_villain:
        superheroes_only.append(hero)
superheroes_only.sort_by_criterion('year')
superheroes_only.show()

#Subinidice H-    
print("H. Modificar nombre real de Ant Man:")
index = list_superhero.search('Ant Man', 'name')
if index is not None:
        list_superhero[index].real_name = "Scott Lang"
        print("Modificado:", list_superhero[index])
else:
        print("Ant Man no se encontró.")

#Subindice I-
print("I. Personajes con 'time-traveling' o 'suit' en la biografía:")
for hero in list_superhero:
    bio = hero.short_bio.lower()
    if "time-traveling" in bio or "suit" in bio:
        print(hero)
        
#Subinidice J-
print("J. Eliminación de Electro y Baron Zemo:")
for name in ["Electro", "Baron Zemo"]:
    index = list_superhero.search(name, 'name')
    if index is not None:
        eliminado = list_superhero[index]
        list_superhero.delete_value(name, 'name')
        print("Eliminado:", eliminado)
    else:
        print(f"{name} no se encontró")        