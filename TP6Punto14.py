# ============================================================
# a) Definir los vértices del grafo (ambientes de la casa)
# ============================================================

class Grafo:
    def __init__(self):
        self.vertices = {}
        self.aristas = []   # lista de tuplas (peso, v1, v2)

    def agregar_vertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = []

    # ============================================================
    # b) Agregar aristas con su distancia (peso)
    #    Se carga un grafo NO dirigido
    # ============================================================
    def agregar_arista(self, v1, v2, peso):
        self.vertices[v1].append((v2, peso))
        self.vertices[v2].append((v1, peso))
        self.aristas.append((peso, v1, v2))

    # Método para mostrar el grafo (opcional)
    def mostrar(self):
        for v in self.vertices:
            print(v, ":", self.vertices[v])

    # ============================================================
    # c) KRUSKAL → Árbol de Expansión Mínima
    # ============================================================

    # Estructuras para Union-Find (Disjoint Set)
    def find(self, padres, x):
        if padres[x] != x:
            padres[x] = self.find(padres, padres[x])
        return padres[x]

    def union(self, padres, rangos, x, y):
        raiz_x = self.find(padres, x)
        raiz_y = self.find(padres, y)

        if raiz_x != raiz_y:
            if rangos[raiz_x] < rangos[raiz_y]:
                padres[raiz_x] = raiz_y
            elif rangos[raiz_x] > rangos[raiz_y]:
                padres[raiz_y] = raiz_x
            else:
                padres[raiz_y] = raiz_x
                rangos[raiz_x] += 1

    def kruskal(self):
        # Inicializar estructuras de conjuntos
        padres = {}
        rangos = {}

        for v in self.vertices:
            padres[v] = v
            rangos[v] = 0

        # Ordenar aristas por peso
        aristas_ordenadas = sorted(self.aristas)

        mst = []  # árbol de expansión mínima
        total = 0

        for peso, v1, v2 in aristas_ordenadas:
            if self.find(padres, v1) != self.find(padres, v2):
                self.union(padres, rangos, v1, v2)
                mst.append((v1, v2, peso))
                total += peso

        return mst, total

    # ============================================================
    # d) DIJKSTRA → Camino mínimo entre dos ambientes
    # ============================================================
    def dijkstra(self, inicio):
        import heapq

        dist = {v: float('inf') for v in self.vertices}
        dist[inicio] = 0

        pq = [(0, inicio)]
        anterior = {v: None for v in self.vertices}

        while pq:
            d_actual, actual = heapq.heappop(pq)

            if d_actual > dist[actual]:
                continue

            for vecino, peso in self.vertices[actual]:
                nueva_dist = d_actual + peso
                if nueva_dist < dist[vecino]:
                    dist[vecino] = nueva_dist
                    anterior[vecino] = actual
                    heapq.heappush(pq, (nueva_dist, vecino))

        return dist, anterior

    def reconstruir_camino(self, anterior, inicio, fin):
        camino = []
        actual = fin
        while actual is not None:
            camino.append(actual)
            actual = anterior[actual]
        camino.reverse()
        return camino


# ============================================================
# a) Crear el grafo y sus vértices (ambientes de la casa)
# ============================================================
g = Grafo()
ambientes = [
    "cocina", "comedor", "cochera", "quincho", "baño1", "baño2",
    "habitacion1", "habitacion2", "sala_de_estar", "terraza", "patio"
]

for amb in ambientes:
    g.agregar_vertice(amb)

# ============================================================
# b) Cargar aristas con distancia (al menos 3 por ambiente)
#    (Ejemplo con distancias ficticias)
# ============================================================
g.agregar_arista("cocina", "comedor", 4)
g.agregar_arista("cocina", "patio", 7)
g.agregar_arista("cocina", "baño1", 3)

g.agregar_arista("comedor", "sala_de_estar", 6)
g.agregar_arista("comedor", "terraza", 10)
g.agregar_arista("comedor", "habitacion1", 9)

g.agregar_arista("cochera", "patio", 8)
g.agregar_arista("cochera", "quincho", 5)
g.agregar_arista("cochera", "baño2", 11)

g.agregar_arista("quincho", "patio", 4)
g.agregar_arista("quincho", "terraza", 12)
g.agregar_arista("quincho", "sala_de_estar", 9)

g.agregar_arista("habitacion1", "habitacion2", 2)
g.agregar_arista("habitacion1", "baño1", 6)
g.agregar_arista("habitacion2", "baño2", 3)

g.agregar_arista("sala_de_estar", "terraza", 7)
g.agregar_arista("sala_de_estar", "patio", 13)
g.agregar_arista("patio", "terraza", 8)

# ============================================================
# c) Aplicar KRUSKAL → obtener el MST y metros totales
# ============================================================
mst, total_metros = g.kruskal()

print("\n=== Árbol de Expansión Mínima (Kruskal) ===")
for v1, v2, peso in mst:
    print(f"{v1} -- {v2}  ({peso} m)")

print(f"\nMetros totales de cables necesarios: {total_metros} m")

# ============================================================
# d) Camino MÁS CORTO entre habitación1 y sala_de_estar
# ============================================================
dist, anterior = g.dijkstra("habitacion1")
camino = g.reconstruir_camino(anterior, "habitacion1", "sala_de_estar")

print("\n=== Camino más corto habitacion1 → sala_de_estar ===")
print(" → ".join(camino))
print(f"Distancia total: {dist['sala_de_estar']} m")