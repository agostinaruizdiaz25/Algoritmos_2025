import heapq

#   Clase Grafo (no dirigido)

class Graph:
    def __init__(self):
        self.nodes = {}      # { nombre : tipo }
        self.edges = {}      # { nodo : { vecino : peso } }

    # a) agregar nodo con su tipo
    def add_node(self, name, tipo):
        self.nodes[name] = tipo
        self.edges[name] = {}

    # agregar arista en grafo NO dirigido
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

    # b) DFS
    def dfs(self, start):
        visited = set()
        orden = []

        def recorrer(n):
            visited.add(n)
            orden.append(n)
            for vecino in self.edges[n]:
                if vecino not in visited:
                    recorrer(vecino)

        recorrer(start)
        return orden

    # b) BFS
    def bfs(self, start):
        from collections import deque
        visited = set([start])
        cola = deque([start])
        orden = []

        while cola:
            nodo = cola.popleft()
            orden.append(nodo)
            for vecino in self.edges[nodo]:
                if vecino not in visited:
                    visited.add(vecino)
                    cola.append(vecino)
        return orden

    # c, e, f) Dijkstra camino más corto
    def dijkstra(self, start, target):
        dist = {n: float("inf") for n in self.nodes}
        dist[start] = 0
        prev = {}
        pq = [(0, start)]

        while pq:
            d, u = heapq.heappop(pq)
            if u == target:
                break
            for v, peso in self.edges[u].items():
                if d + peso < dist[v]:
                    dist[v] = d + peso
                    prev[v] = u
                    heapq.heappush(pq, (dist[v], v))

        # reconstruir el camino
        camino = []
        nodo = target
        while nodo in prev or nodo == start:
            camino.append(nodo)
            if nodo == start:
                break
            nodo = prev[nodo]
        camino.reverse()

        return camino, dist[target]

    # d) KRUSKAL – Árbol de Expansión Mínima
    def kruskal(self):
        parent = {}
        rank = {}

        def find(n):
            if parent[n] != n:
                parent[n] = find(parent[n])
            return parent[n]

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                if rank[ra] < rank[rb]:
                    parent[ra] = rb
                elif rank[ra] > rank[rb]:
                    parent[rb] = ra
                else:
                    parent[rb] = ra
                    rank[ra] += 1

        for n in self.nodes:
            parent[n] = n
            rank[n] = 0

        # convertir aristas a lista
        edges_list = []
        for u in self.edges:
            for v, w in self.edges[u].items():
                if (v, u, w) not in edges_list:
                    edges_list.append((u, v, w))

        edges_list.sort(key=lambda x: x[2])  # ordenar por peso

        mst = []
        total = 0

        for u, v, w in edges_list:
            if find(u) != find(v):
                union(u, v)
                mst.append((u, v, w))
                total += w

        return mst, total


#   CARGA DEL GRAFO SEGÚN LA FIGURA

g = Graph()

# Nodos con su tipo
datos = {
    "Manjaro":"pc", "Parrot":"pc", "Fedora":"pc", "Mint":"pc", "Ubuntu":"pc",
    "Debian":"notebook", "Red Hat":"notebook", "Arch":"notebook",
    "Impresora":"impresora",
    "Guaraní":"servidor", "MongoDB":"servidor",
    "Switch 1":"switch", "Switch 2":"switch",
    "Router 1":"router", "Router 2":"router", "Router 3":"router"
}

for nombre, tipo in datos.items():
    g.add_node(nombre, tipo)

# Aristas según el diagrama

edges = [
    ("Red Hat", "Router 2", 25),
    ("Debian", "Switch 1", 17),
    ("Ubuntu", "Switch 1", 18),
    ("Switch 1", "Router 1", 29),
    ("Mint", "Router 1", 20),
    ("Impresora", "Mint", 22),
    ("Router 1", "Router 2", 37),
    ("Router 2", "Router 3", 50),
    ("Red Hat", "Guaraní", 9),
    ("Guaraní", "Router 3", 30),

    # parte derecha
    ("Router 3", "Manjaro", 61),
    ("Router 3", "Switch 2", 40),
    ("Switch 2", "Parrot", 12),
    ("Switch 2", "Arch", 56),
    ("Switch 2", "MongoDB", 5),
    ("Router 1", "Fedora", 3)
]

for u,v,w in edges:
    g.add_edge(u, v, w)


#   RESPUESTAS A LOS PUNTOS

print(" b) DFS y BFS desde las notebooks")

for nb in ["Red Hat","Debian","Arch"]:
    print(f"\n--- {nb} ---")
    print("DFS:", g.dfs(nb))
    print("BFS:", g.bfs(nb))

print(" c) Camino más corto desde PCs a la impresora")

for pc in ["Manjaro","Red Hat","Fedora"]:
    camino, dist = g.dijkstra(pc, "Impresora")
    print(f"\nDesde {pc}: {camino}  (distancia: {dist})")

print(" d) Árbol de expansión mínima (usando kruskal)")

mst, total = g.kruskal()
print("Aristas del MST:")
for u,v,w in mst:
    print(f"{u} -- {v}  ({w} m)")
print("Distancia total:", total)

print(" e) PC más cercana a Guaraní")

pcs = [n for n,t in datos.items() if t=="pc"]
mejor = None
dist_min = float("inf")
camino_mejor = []

for pc in pcs:
    camino, dist = g.dijkstra(pc, "Guaraní")
    if dist < dist_min:
        dist_min = dist
        mejor = pc
        camino_mejor = camino

print("La PC más cercana es:", mejor)
print("Camino:", camino_mejor, " Distancia:", dist_min)

print(" f) Computadora del Switch 1 más cercana a MongoDB")

conectadas_sw1 = ["Debian","Ubuntu","Router 1"]
mejor = None
dist_min = float("inf")
camino_mejor = []

for comp in conectadas_sw1:
    camino, dist = g.dijkstra(comp, "MongoDB")
    if dist < dist_min:
        dist_min = dist
        mejor = comp
        camino_mejor = camino

print("La mejor es:", mejor)
print("Camino:", camino_mejor, "Distancia:", dist_min)

print(" g) Mover impresora al Router 2 y repetir DFS/BFS")

# quitar conexión vieja y agregar la nueva
g.edges["Impresora"] = {}
g.add_edge("Impresora", "Router 2", 15)

print("\nDFS y BFS nuevamente desde Red Hat:")
print("DFS:", g.dfs("Red Hat"))
print("BFS:", g.bfs("Red Hat"))