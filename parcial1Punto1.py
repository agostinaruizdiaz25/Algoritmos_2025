superheroes = [
    "Falcon", "Vision", "Viuda Negra","SpiderMan", "Capitan America", "Thor", "Iron Man", "Pantera Negra", "Scaarlet witch", "Hulk", "Ojo de Halcon", "Soldado del Invierno", "Groot", "AntMan", "Doctor Strange", 
]
#Subindice A, usmaos recursividad para buscar al cap
def buscar_capitanamerica(lista, objetivo, indice=0):
    if indice >= len(lista):
        return False
    if lista[indice] == objetivo:
        return True
    return buscar_capitanamerica(lista, objetivo, indice + 1)

#Subindice B, usamos recursividad para listar a los superheroes
def lista_superheroes(lista, indice=0):
    if indice >= len(lista):
        return
    print(lista[indice])
    lista_superheroes(lista, indice + 1) 
    
#Prueba 
encontrado = buscar_capitanamerica(superheroes, "Capitan America")
print ("¿Se ha encontrado al Capitan America?", encontrado)

print("lista de personajes")
lista_superheroes(superheroes)