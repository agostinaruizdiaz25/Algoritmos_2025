# Definimos la pila con algunos ejemplos de trajes
pila_trajes = [
    {'modelo': 'Mark XLIV', 'pelicula': 'Avengers: Age of Ultron', 'estado': 'Dañado'},
    {'modelo': 'Mark XLV', 'pelicula': 'Avengers: Age of Ultron', 'estado': 'Impecable'},
    {'modelo': 'Mark XLVII', 'pelicula': 'Spider-Man: Homecoming', 'estado': 'Dañado'},
    {'modelo': 'Mark L', 'pelicula': 'Avengers: Infinity War', 'estado': 'Destruido'},
    {'modelo': 'Mark LXXXV', 'pelicula': 'Avengers: Endgame', 'estado': 'Impecable'},
    {'modelo': 'Mark XLVI', 'pelicula': 'Capitan America: Civil War', 'estado': 'Impecable'},
]
#a
peliculas_hulkbuster = [traje['pelicula'] for traje in pila_trajes if traje['modelo'] == 'Mark XLIV']
if peliculas_hulkbuster:
    print("El modelo Mark XLIV fue utilizado en:")
    for peli in peliculas_hulkbuster:
        print(f"- {peli}")
else:
    print("El modelo Mark XLIV no fue utilizado en ninguna película.")
##b
print("Modelos de trajes dañados:")
for traje in pila_trajes:
    if traje['estado'] == 'Dañado':
        print(f"- {traje['modelo']} (Película: {traje['pelicula']})")
#c
nueva_pila = []
print("Eliminando trajes destruidos:")
for traje in pila_trajes:
    if traje['estado'] == 'Destruido':
        print(f"- {traje['modelo']} (Película: {traje['pelicula']}) eliminado")
    else:
        nueva_pila.append(traje)

pila_trajes = nueva_pila  # Actualizamos la pila original sin los destruidos
#d
#e
nuevo_modelo = {'modelo': 'Mark LXXXV', 'pelicula': 'Avengers: Endgame', 'estado': 'Impecable'}

# Revisamos si ya existe ese modelo en esa película
repetido = any(traje['modelo'] == nuevo_modelo['modelo'] and traje['pelicula'] == nuevo_modelo['pelicula']
               for traje in pila_trajes)

if not repetido:
    pila_trajes.append(nuevo_modelo)
    print("Modelo Mark LXXXV agregado correctamente.")
else:
    print("El modelo Mark LXXXV ya está cargado para esa película.")

#f
peliculas_objetivo = ["Spider-Man: Homecoming", "Capitan America: Civil War"]
print("Trajes usados en las películas seleccionadas:")
for traje in pila_trajes:
    if traje['pelicula'] in peliculas_objetivo:
        print(f"- {traje['modelo']} en {traje['pelicula']}")