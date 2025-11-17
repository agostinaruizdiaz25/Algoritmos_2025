class Node:
    def __init__(self, key, pokemon_data):
        self.key = key                   # clave de ordenamiento (nombre, número o tipo)
        self.pokemon_data = pokemon_data # diccionario con todos los datos del Pokémon
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # inserción en árbol binario ordenado por self.key 
    def insert(self, key, pokemon_data):
        def __insert(root, key, pokemon_data):
            if root is None:
                return Node(key, pokemon_data)
            if key < root.key:
                root.left = __insert(root.left, key, pokemon_data)
            else:
                root.right = __insert(root.right, key, pokemon_data)
            return root

        self.root = __insert(self.root, key, pokemon_data)

    #recorrido in orden
    def in_order(self):
        def __in_order(root):
            if root:
                __in_order(root.left)
                print(root.key)
                __in_order(root.right)
        __in_order(self.root)

    #listado in orden pero con muestra de datos
    def in_order_full_data(self):
        def __in_order(root):
            if root:
                __in_order(root.left)
                print(root.pokemon_data)
                __in_order(root.right)
        __in_order(self.root)

    #busqueda por proximidad para los nombre 
    def proximity_search(self, text):
        def __search(root):
            if root:
                __search(root.left)
                if text.lower() in root.key.lower():
                    print(root.pokemon_data)
                __search(root.right)
        __search(self.root)

    # busqueda por clave para los numeros 
    def search(self, key):
        def __search(root, key):
            if root is None:
                return None
            if key == root.key:
                return root.pokemon_data
            if key < root.key:
                return __search(root.left, key)
            else:
                return __search(root.right, key)
        return __search(self.root, key)

    #listado por niveles para los nombres solamente
    def level_order(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

# lista de pokemones 
pokemons = [
    ("Bulbasaur", 1,
     ["planta", "veneno"],
     ["fuego", "hielo", "psíquico", "volador"],
     False, False),

    ("Charizard", 6,
     ["fuego", "volador"],
     ["roca", "eléctrico", "agua"],
     True, True),

    ("Pikachu", 25,
     ["eléctrico"],
     ["tierra"],
     False, False),

    ("Gengar", 94,
     ["fantasma", "veneno"],
     ["psíquico", "siniestro", "fantasma"],
     True, False),

    ("Steelix", 208,
     ["acero", "tierra"],
     ["fuego", "agua", "lucha", "tierra"],
     True, False),

    ("Houndoom", 229,
     ["fuego", "siniestro"],
     ["agua", "lucha", "tierra", "roca"],
     True, False),

    ("Lucario", 448,
     ["lucha", "acero"],
     ["fuego", "tierra", "lucha"],
     True, False),

    ("Jolteon", 135,
     ["eléctrico"],
     ["tierra"],
     False, False),

    ("Lycanroc", 745,
     ["roca"],
     ["acero", "agua", "planta", "lucha", "tierra"],
     False, False),

    ("Tyrantrum", 697,
     ["roca", "dragón"],
     ["acero", "hielo", "lucha", "hada", "dragón"],
     False, False),
]

#arboles solicitados por el ejercicio

arbol_nombre = BinaryTree()   # índice = nombre
arbol_numero = BinaryTree()   # índice = número
arbol_tipo = BinaryTree()     # índice = tipo (un Pokémon puede ir a varios)

# carga de datos en los tres arboles

for nombre, numero, tipos, debilidad, mega, giga in pokemons:

    data = {
        "nombre": nombre,
        "numero": numero,
        "tipos": tipos,
        "debilidad": debilidad,
        "mega": mega,
        "gigamax": giga
    }

    # árbol por nombre
    arbol_nombre.insert(nombre, data)

    # árbol por número
    arbol_numero.insert(numero, data)

    # árbol por tipo (cada tipo sería una clave independiente)
    for t in tipos:
        arbol_tipo.insert(t, data)

print("Árboles cargados correctamente\n")

# SUBINDICE a) Mostrar datos por número o por proximidad de nombre
print("SUBINDICE a) Búsqueda por número:")
pokemon = arbol_numero.search(94)   # ejemplo Gengar
print(pokemon)
print()

print("SUBINDICE a) Búsqueda por proximidad de nombre 'bul':")
arbol_nombre.proximity_search("bul")
print()

# SUBINDICE b) Mostrar todos los Pokémon de un tipo dado
tipos_consultar = ["fantasma", "fuego", "acero", "eléctrico"]

print("SUBINDICE b) Pokémon por tipos:")
for t in tipos_consultar:
    print(f"\nPokémon tipo {t}:")
    arbol_tipo.proximity_search(t)   # uso proximidad pero la clave es exacta

# SUBINDICE c) Listados ordenados
print("\nSUBINDICE c.I) Listado ascendente por número:")
arbol_numero.in_order()
print()

print("SUBINDICE c.II) Listado ascendente por nombre:")
arbol_nombre.in_order()
print()

print("SUBINDICE c.III) Listado por niveles (nombre):")
arbol_nombre.level_order()
print()

# SUBINDICE d) Pokémon débiles frente a Jolteon, Lycanroc y Tyrantrum

debilidades_relevantes = ["eléctrico", "roca", "dragón"]

print("SUBINDICE d) Pokémon débiles frente a Jolteon, Lycanroc y Tyrantrum:")

for nombre, numero, tipos, debilidad, mega, giga in pokemons:
    if any(d in debilidad for d in debilidades_relevantes):
        print(nombre)

print()

# SUBINDICE e) Tipos y cuántos hay de cada uno
print("SUBINDICE e) Cantidad de Pokémon por tipo:")

contador_tipos = {}

for nombre, numero, tipos, debilidad, mega, giga in pokemons:
    for t in tipos:
        contador_tipos[t] = contador_tipos.get(t, 0) + 1

for t, cant in contador_tipos.items():
    print(f"{t}: {cant}")

print()

# SUBINDICE f) Pokémon con megaevolución
print("SUBINDICE f) Pokémon con megaevolución:")
mega_count = sum(1 for p in pokemons if p[4] == True)
print(f"Total: {mega_count}")
print()

# SUBINDICE g) Pokémon con forma Gigamax
print("SUBINDICE g) Pokémon con forma Gigamax:")
giga_count = sum(1 for p in pokemons if p[5] == True)
print(f"Total: {giga_count}")
print()
