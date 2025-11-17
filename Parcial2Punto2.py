# Parcial2Punto2
import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    # se agrega vertice
    def add_vertex(self, name, episodes=None):
        if episodes is None:
            episodes = []
        self.vertices[name] = {"edges": {}, "episodes": episodes}

    # se agrega arista no dirigida con peso 
    def add_edge(self, v1, v2, weight):
        self.vertices[v1]["edges"][v2] = weight
        self.vertices[v2]["edges"][v1] = weight

    # prim arbol de expansion minima desde unn icinico 
    def mst_prim(self, start):
        visited = set([start])
        edges = []
        mst = []

        for v, w in self.vertices[start]["edges"].items():
            heapq.heappush(edges, (w, start, v))

        while edges:
            weight, v1, v2 = heapq.heappop(edges)
            if v2 not in visited:
                visited.add(v2)
                mst.append((v1, v2, weight))

                for next_v, next_w in self.vertices[v2]["edges"].items():
                    if next_v not in visited:
                        heapq.heappush(edges, (next_w, v2, next_v))

        return mst

    # dijkstra para el camino mas corto 
    def shortest_path(self, start, end):
        pq = [(0, start, [])]
        visited = set()

        while pq:
            dist, current, path = heapq.heappop(pq)

            if current in visited:
                continue
            visited.add(current)

            path = path + [current]

            if current == end:
                return dist, path

            for neighbor, weight in self.vertices[current]["edges"].items():
                if neighbor not in visited:
                    heapq.heappush(pq, (dist + weight, neighbor, path))

        return None

    # maximo peso de cualquier arista
    def max_shared_episodes(self):
        max_w = 0
        pairs = []

        for v in self.vertices:
            for w, weight in self.vertices[v]["edges"].items():
                if weight > max_w:
                    max_w = weight
                    pairs = [(v, w)]
                elif weight == max_w:
                    pairs.append((v, w))

        # para eliminar duplicados (A-B y B-A)
        unique_pairs = set(tuple(sorted(p)) for p in pairs)

        return max_w, list(unique_pairs)

# carga de personajes de SW
g = Graph()

# Episodios donde apareció cada personaje (simulacion)
appearances = {
    "Luke Skywalker":  [4, 5, 6, 7, 8, 9],
    "Darth Vader":     [3, 4, 5, 6],
    "Yoda":            [1, 2, 3, 5, 6, 8],
    "Boba Fett":       [2, 5, 6],
    "C-3PO":           [1,2,3,4,5,6,7,8,9],
    "Leia":            [4, 5, 6, 7, 8, 9],
    "Rey":             [7, 8, 9],
    "Kylo Ren":        [7, 8, 9],
    "Chewbacca":       [3, 4, 5, 6, 7, 8, 9],
    "Han Solo":        [4, 5, 6, 7],
    "R2-D2":           [1,2,3,4,5,6,7,8,9],
    "BB-8":            [7, 8, 9],
}

# para crear vértices
for p, eps in appearances.items():
    g.add_vertex(p, eps)

# se agrega arista donde peso=episodios en los que aparecen juntos
def shared_episodes(p1, p2):
    return len(set(appearances[p1]) & set(appearances[p2]))

people = list(appearances.keys())

for i in range(len(people)):
    for j in range(i+1, len(people)):
        w = shared_episodes(people[i], people[j])
        if w > 0:
            g.add_edge(people[i], people[j], w)


# resoluciones
# Subindice A) Árbol de expansión mínima desde C-3PO, Yoda y Leia
print("\n arbol de expansion minima")

for person in ["C-3PO", "Yoda", "Leia"]:
    print(f"\nMST desde {person}:")
    mst = g.mst_prim(person)
    for v1, v2, w in mst:
        print(f"{v1} -- {v2} (peso: {w})")

#subindice B) Máximo número de episodios compartidos entre dos personajes
print("\n maxio de episodios compartidos")

max_w, pairs = g.max_shared_episodes()

print(f"Máximo número de episodios compartidos: {max_w}")
print("Pares de personajes:")
for p1, p2 in pairs:
    print(f"  - {p1} y {p2}")

#subinidce C) Caminos más cortos
print("\n camino mas cortos")

dist, path = g.shortest_path("C-3PO", "R2-D2")
print(f"Camino más corto entre C-3PO y R2-D2: {path}, distancia = {dist}")

dist, path = g.shortest_path("Yoda", "Darth Vader")
print(f"Camino más corto entre Yoda y Darth Vader: {path}, distancia = {dist}")

#Subindice D) Personajes que aparecieron en los 9 episodios
print("\n personajes que aparecieron en todos los episodios")
for p, eps in appearances.items():
    if len(eps) == 9:
        print(p)
