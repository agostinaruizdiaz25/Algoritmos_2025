from random import choice

class Queue:
    def __init__(self):
        self.items = []

    def arrive(self, item):
        self.items.append(item)

    def attention(self):
        if self.size() > 0:
            return self.items.pop(0)

    def on_front(self):
        if self.size() > 0:
            return self.items[0]

    def move_to_end(self):
        if self.size() > 0:
            self.items.append(self.items.pop(0))

    def size(self):
        return len(self.items)

    def show(self):
        for item in self.items:
            print(item)

# Creamos la cola con los personajes
cola_mcu = Queue()

personajes_mcu = [
    ("Tony Stark", "Iron Man", "M"),
    ("Steve Rogers", "Capitán América", "M"),
    ("Natasha Romanoff", "Black Widow", "F"),
    ("Carol Danvers", "Capitana Marvel", "F"),
    ("Scott Lang", "Ant-Man", "M"),
    ("Wanda Maximoff", "Scarlet Witch", "F"),
    ("Stephen Strange", "Doctor Strange", "M"),
    ("Sam Wilson", "Falcon", "M"),
    ("Shuri", "Black Panther (II)", "F"),
    ("Peter Parker", "Spider-Man", "M")
]

# se carga la cola
for personaje in personajes_mcu:
    cola_mcu.arrive(personaje)

# usamos variables auxiliares
personaje_capitana_marvel = None
superheroes_femeninos = []
personajes_masculinos = []
superheroe_de_scott_lang = None
datos_con_s = []
carol_danvers_encontrada = False
superheroe_de_carol = None

# Procesamos la cola 
for i in range(cola_mcu.size()):
    personaje = cola_mcu.on_front()

    nombre_real, nombre_superheroe, genero = personaje

    # subindice a. nombre del personaje de Capitana Marvel
    if nombre_superheroe.lower() == "capitana marvel":
        personaje_capitana_marvel = nombre_real

    # subindice b. superhéroes femeninos
    if genero == "F":
        superheroes_femeninos.append(nombre_superheroe)

    # subindice c. personajes masculinos
    if genero == "M":
        personajes_masculinos.append(nombre_real)

    # subindice d. superhéroe de Scott Lang
    if nombre_real.lower() == "scott lang":
        superheroe_de_scott_lang = nombre_superheroe

    # subindice e. nombres que comienzan con "S"
    if nombre_real.startswith("S") or nombre_superheroe.startswith("S"):
        datos_con_s.append(personaje)

    # subindice f. personaje Carol Danvers
    if nombre_real.lower() == "carol danvers":
        carol_danvers_encontrada = True
        superheroe_de_carol = nombre_superheroe

    # para mantener el orden de la cola
    cola_mcu.move_to_end()
#mostramos los resultados obtenidos
print("a. Personaje de Capitana Marvel:", personaje_capitana_marvel)
print("b. Superhéroes femeninos:", superheroes_femeninos)
print("c. Personajes masculinos:", personajes_masculinos)
print("d. Superhéroe de Scott Lang:", superheroe_de_scott_lang)
print("e. Datos de personajes o superhéroes que empiezan con 'S':")
for dato in datos_con_s:
    print("   ", dato)
print("f. ¿Carol Danvers está en la cola?", "Sí" if carol_danvers_encontrada else "No")
if carol_danvers_encontrada:
    print("   Su superhéroe es:", superheroe_de_carol)