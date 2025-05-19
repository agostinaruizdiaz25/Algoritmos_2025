#definimos la pila con ejemplos de personajes del MCU
pila_personajesmarvel = [
    {'nombre': 'Iron Man', 'peliculas': 10},
    {'nombre': 'Thor', 'peliculas': 9},
    {'nombre': 'Rocket Raccoon', 'peliculas': 5},
    {'nombre': 'Viuda Negra', 'peliculas': 7},
    {'nombre': 'Groot', 'peliculas': 4},
    {'nombre': 'Doctor Strange', 'peliculas': 4},
    {'nombre': 'Captain America', 'peliculas': 9},
    {'nombre': 'Gamora', 'peliculas': 5},
    {'nombre': 'Drax', 'peliculas': 5},
    {'nombre': 'Hulk', 'peliculas': 8},
]
#subindice A, definimos la posición de Roocket y Groot
def busqueda_posicion(pila, nombres):
    posiciones = {}
    for i, personaje in enumerate(reversed(pila), start=1):  # simulacion de pila (último = cima)
        if personaje['nombre'] in nombres:
            posiciones[personaje['nombre']] = i
    return posiciones

posiciones = busqueda_posicion(pila_personajesmarvel, ['Rocket Raccoon', 'Groot'])
for nombre, pos in posiciones.items():
    print(f"{nombre} está en la posición {pos} desde la cima de la pila.")
    
#subindice B, visualización de personajes que aparecen en más de 5 peliculas
print("Personajes que participaron en más de 5 películas:")
for personaje in pila_personajesmarvel:
    if personaje['peliculas'] > 5:
        print(f"- {personaje['nombre']} ({personaje['peliculas']} películas)")
        
#subindice C, determinar la cantidad de peliculas de la Viuda negra
def busqueda_participacion(pila, nombre_objetivo):
    for personaje in pila:
        if personaje['nombre'].lower() == nombre_objetivo.lower():
            return personaje['peliculas']
    return 0  # Si no se encuentra
pelis_vn = busqueda_participacion(pila_personajesmarvel, "Viuda Negra")
print(f"Viuda Negra participó en {pelis_vn} película(s).")

#subindice D, determinar nombre de personajes que empiecen con: C-D-G
print("Personajes cuyos nombres empiezan con C, D o G:")
for personaje in pila_personajesmarvel:
    if personaje['nombre'][0].upper() in ['C', 'D', 'G']:
        print(f"- {personaje['nombre']}")