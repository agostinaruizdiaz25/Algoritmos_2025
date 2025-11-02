# creamos tree
class Node:
    def __init__(self, value, other_values=None):
        self.value = value
        self.other_values = other_values
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value, other_values=None):
        def __insert(root, value, other_values):
            if root is None:
                return Node(value, other_values)
            if value < root.value:
                root.left = __insert(root.left, value, other_values)
            else:
                root.right = __insert(root.right, value, other_values)
            return root
        self.root = __insert(self.root, value, other_values)

    def in_order(self):
        def __in_order(root):
            if root:
                __in_order(root.left)
                print(root.value)
                __in_order(root.right)
        __in_order(self.root)

    def post_order(self):
        def __post_order(root):
            if root:
                __post_order(root.right)
                print(root.value)
                __post_order(root.left)
        __post_order(self.root)

    def villain_in_order(self):
        def __villains(root):
            if root:
                __villains(root.left)
                if root.other_values and root.other_values.get('is_villain'):
                    print(root.value)
                __villains(root.right)
        __villains(self.root)

    def proximity_search(self, prefix):
        def __search(root):
            if root:
                __search(root.left)
                if root.value.startswith(prefix):
                    print(root.value)
                __search(root.right)
        __search(self.root)

    def delete(self, value):
        # versión simplificada, devuelve tupla (colección de elementos ordenados)
        def __delete(root, value):
            if root is None:
                return root, None
            if value < root.value:
                root.left, deleted = __delete(root.left, value)
            elif value > root.value:
                root.right, deleted = __delete(root.right, value)
            else:
                deleted = root.value
                if root.left is None:
                    return root.right, deleted
                elif root.right is None:
                    return root.left, deleted
                temp = root.right
                while temp.left:
                    temp = temp.left
                root.value = temp.value
                root.right, _ = __delete(root.right, temp.value)
            return root, deleted
        self.root, deleted = __delete(self.root, value)
        return deleted, None

    def divide_tree(self, heroes_tree, villains_tree):
        def __divide(root):
            if root:
                if root.other_values and root.other_values.get('is_villain'):
                    villains_tree.insert(root.value, root.other_values)
                else:
                    heroes_tree.insert(root.value, root.other_values)
                __divide(root.left)
                __divide(root.right)
        __divide(self.root)

    def count_heroes(self):
        def __count(root):
            if root is None:
                return 0
            count = 0
            if not root.other_values.get('is_villain'):
                count += 1
            return count + __count(root.left) + __count(root.right)
        return __count(self.root)

# Creación de los árboles principales
arbol_mcu = BinaryTree()          # árbol general con todos los personajes
arbol_heroes = BinaryTree()       # árbol solo de héroes
arbol_villanos = BinaryTree()     # árbol solo de villanos

# Subindice a. CARGA DE PERSONAJES EN EL ÁRBOL
# En cada nodo se guarda el nombre y si es villano o no (True/False)
personajes_mcu = [
    ('Iron Man', False),
    ('Thanos', True),
    ('Doctor Strange', False),
    ('Loki', True),
    ('Spider-Man', False),
    ('Ultron', True),
    ('Captain America', False),
    ('Red Skull', True),
    ('Black Widow', False),
    ('Hela', True),
    ('Vision', False),
    ('Green Goblin', True),
    ('Hulk', False),
    ('Vulture', True),
    ('Scarlet Witch', False)
]

# Se inserta todos los personajes en el árbol principal
for nombre, es_villano in personajes_mcu:
    arbol_mcu.insert(nombre, {'is_villain': es_villano})

print("Árbol del MCU cargado")
arbol_mcu.in_order()
print()

# Subindice b. Se lista los villanos en orden alfabético
#Se usa un barrido in-order, pero filtrando los nodos donde is_villain = True
print("subinidce b. Villanos ordenados alfabéticamente")
arbol_mcu.villain_in_order()
print()

#Subindice c. Mostrar los superhéroes que empiezan con C
#usar la función de búsqueda por proximidad del TDA
print("subindice c. Superhéroes que comienzan con 'C'")
arbol_mcu.proximity_search('C')
print()

#Subindice d. Se debe contar cuántos superhéroes hay en el árbol
# Llamamos a una función recursiva que cuenta los nodos con is_villain = False
print("subindice d. Cantidad de superhéroes en el árbol")
cantidad_heroes = arbol_mcu.count_heroes()
print(f"Hay {cantidad_heroes} superhéroes en el árbol.")
print()

#Subindice e. Corregimos a Doctor Strange (búsqueda por proximidad)
# Buscamos el nombre “Doctor Strange” y lo reemplazamos por “Dr. Strange”
print("subindice e. Corregir 'Doctor Strange'")
arbol_mcu.proximity_search('Do')  # se muestra coincidencias cercanas
valor, otros_valores = arbol_mcu.delete('Doctor Strange')
if valor is not None:
    nuevo_nombre = 'Dr. Strange'
    arbol_mcu.insert(nuevo_nombre, otros_valores)
    print(f"Nombre corregido: {valor} -> {nuevo_nombre}")
else:
    print("Doctor Strange no fue encontrado para corregir.")
print()

# Subindice f. Listar superhéroes en orden descendente
# Se usa el recorrido post_order() para verlos de forma descendente
print("subindice f. Superhéroes ordenados de manera descendente")
arbol_mcu.post_order()
print()

#subindice g. Generar un bosque (árbol de héroes y árbol de villanos)
print("subindice g. se crea un bosque de héroes y villanos")
# hago uso de la función divide_tree() del TDA para separar ambos árboles
arbol_mcu.divide_tree(arbol_heroes, arbol_villanos)

#subindice g.I --> se debe contar cuántos nodos tiene cada árbol
def contar_nodos(arbol):
    def __contar(root):
        if root is None:
            return 0
        return 1 + __contar(root.left) + __contar(root.right)
    return __contar(arbol.root)

nodos_heroes = contar_nodos(arbol_heroes)
nodos_villanos = contar_nodos(arbol_villanos)

print(f"(apartado I) Héroes: {nodos_heroes} nodos")
print(f"(apartado I) Villanos: {nodos_villanos} nodos")
print()

# subindice g.II --> Se hace un barrido in-order para mostrar los nombres ordenados alfabéticamente
print("(apartado II) Barrido de héroes (in-order):")
arbol_heroes.in_order()
print()

print("(aparatdo II) Barrido de villanos (in-order):")
arbol_villanos.in_order()
print()