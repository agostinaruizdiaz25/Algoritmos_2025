def usar_la_fuerza(mochila, objetos_extraidos=0):
    # si la mochila está vacía
    if not mochila:
        return False, objetos_extraidos

    # sacar el primer objeto
    objeto = mochila[0]
    objetos_extraidos += 1

    # encontrar el sable de luz
    if objeto == "sable de luz":
        return True, objetos_extraidos

    #recursividad: seguir buscando en el resto de la mochila
    return usar_la_fuerza(mochila[1:], objetos_extraidos)

# Ejemplificación
mochila = ["comida", "agua","sable de luz", "manta", "botiquín"]

encontrado, objetos_sacados = usar_la_fuerza(mochila)

if encontrado:
    print(f"¡Encontraste el sable de luz después de sacar {objetos_sacados} objetos!")
else:
    print("No había un sable de luz en la mochila")
