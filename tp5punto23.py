#Aclaraciones, cada nodo contiene:
# nombre de la criatura
# quién la derrotó
# descripción
# quién la ha cazado

class Node:
    def __init__(self, name, defeated_by=None, description=None, captured_by=None):
        self.name = name
        self.defeated_by = defeated_by or []  # Lista de héroes o dioses que la derrotaron
        self.description = description        # Breve descripción (subindice b)
        self.captured_by = captured_by        # Campo “capturada” (subindice g)
        self.left = None
        self.right = None
        self.height = 1 #altura incial del nodo 

class BinaryTree:
    def __init__(self):
        self.root = None
        
    # Búsqueda por nombre
    def search(self, node, name):
        if node is None or node.name == name:
            return node
        if name < node.name:
            return self.search(node.left, name)
        else:
            return self.search(node.right, name)


    #Funciones básicas
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    #Inserción balanceada
    def insert(self, root, name, defeated_by=None, description=None, captured_by=None):
        if not root:
            return Node(name, defeated_by, description, captured_by)

        if name < root.name:
            root.left = self.insert(root.left, name, defeated_by, description, captured_by)
        elif name > root.name:
            root.right = self.insert(root.right, name, defeated_by, description, captured_by)
        else:
            return root  # para no duplicar

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Casos de rotación
        if balance > 1 and name < root.left.name:
            return self.rotate_right(root)
        if balance < -1 and name > root.right.name:
            return self.rotate_left(root)
        if balance > 1 and name > root.left.name:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and name < root.right.name:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def add(self, name, defeated_by=None, description=None, captured_by=None):
        self.root = self.insert(self.root, name, defeated_by, description, captured_by)

    #Subindice a) Listado inorden de criaturas y quiénes las derrotaron
    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(f"Criatura: {node.name} | Derrotado por: {node.defeated_by} | Capturado por: {node.captured_by}")
            self.in_order(node.right)

    # Subindice b) Carga de la descripción
    def set_description(self, name, text):
        node = self.search(self.root, name)
        if node:
            node.description = text
            print(f"Descripción agregada a {name}.")
        else:
            print(f"No se encontró la criatura {name}.")

    # Subindice c) Mostrar toda la información de Talos
    def show_info(self, name):
        node = self.search(self.root, name)
        if node:
            print(f"\n--- Información de {name}")
            print(f"Derrotado por: {node.defeated_by }")
            print(f"Capturado por: {node.captured_by}")
            print(f"Descripción: {node.description or 'Sin descripción'}")
        else:
            print("No se encontró la criatura.")

    # Subindice d) Determinar los 3 héroes y/o dioses con más derrotas
    def top_defeaters(self, node, counter=None):
        if counter is None:
            counter = {}
        if node:
            for hero in node.defeated_by:
                counter[hero] = counter.get(hero, 0) + 1
            self.top_defeaters(node.left, counter)
            self.top_defeaters(node.right, counter)
        return counter
    
    # Subindice e) Listar criaturas derrotadas por Heracles
    def creatures_defeated_by(self, node, hero_name):
        if node:
            self.creatures_defeated_by(node.left, hero_name)
            if hero_name in node.defeated_by:
                print(node.name)
            self.creatures_defeated_by(node.right, hero_name)

    # Subindice f) Listar criaturas no derrotadas
    def undefeated(self, node):
        if node:
            self.undefeated(node.left)
            if not node.defeated_by:
                print(node.name)
            self.undefeated(node.right)

    # Subinidce g) Esto ya ha sido implementado en el Node (Cada nodo tiene campo “capturada”)

    # Subindice h) Marcar criaturas capturadas por Heracles
    def mark_captured_by_heracles(self):
        captured_list = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]
        for name in captured_list:
            node = self.search(self.root, name)
            if node:
                node.captured_by = "Heracles"

    # Subinindice i) Búsqueda por coincidencia
    def search_by_substring(self, node, substring):
        if node:
            if substring.lower() in node.name.lower():
                print(f"Coincidencia: {node.name}")
            self.search_by_substring(node.left, substring)
            self.search_by_substring(node.right, substring)

    #Subinidce j) Eliminación de Basilisco y Sirenas
    def delete(self, root, name):
        if not root:
            return root
        if name < root.name:
            root.left = self.delete(root.left, name)
        elif name > root.name:
            root.right = self.delete(root.right, name)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.min_value_node(root.right)
            root.name = temp.name
            root.defeated_by = temp.defeated_by
            root.captured_by = temp.captured_by
            root.right = self.delete(root.right, temp.name)
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)
        return root

    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Subindice k) Modificar Aves del Estínfalo
    def modify_stymphalian_birds(self):
        node = self.search(self.root, "Aves del Estínfalo")
        if node:
            node.defeated_by.append("Heracles (varias)")

    # Subindice l) Modificación del nombre Ladón a → Dragón Ladón
    def rename_creature(self, old_name, new_name):
        node = self.search(self.root, old_name)
        if node:
            defeated_by = node.defeated_by
            captured_by = node.captured_by
            desc = node.description
            self.root = self.delete(self.root, old_name)
            self.add(new_name, defeated_by, desc, captured_by)

    # Subindice m) Listado por nivel
    def level_order(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print(current.name)
            if current.left:
                queue.append(current.left)
                
