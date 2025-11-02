# Lista de Jedi con sus datos
jedi = [
    {
        "nombre": "Ahsoka Tano",
        "maestros": ["Anakin Skywalker"],
        "sables": ["verde", "amarillo", "blanco"],
        "especie": "togruta"
    },
    {
        "nombre": "Kit Fisto",
        "maestros": ["Yoda"],
        "sables": ["verde"],
        "especie": "nautolano"
    },
    {
        "nombre": "Anakin Skywalker",
        "maestros": ["Obi-Wan Kenobi"],
        "sables": ["azul"],
        "especie": "humano"
    },
    {
        "nombre": "Obi-Wan Kenobi",
        "maestros": ["Qui-Gon Jinn"],
        "sables": ["azul"],
        "especie": "humano"
    },
    {
        "nombre": "Luke Skywalker",
        "maestros": ["Obi-Wan Kenobi", "Yoda"],
        "sables": ["azul", "verde"],
        "especie": "humano"
    },
    {
        "nombre": "Qui-Gon Jinn",
        "maestros": ["Conde Dooku"],
        "sables": ["verde"],
        "especie": "humano"
    },
    {
        "nombre": "Mace Windu",
        "maestros": ["Cyslin Myr"],
        "sables": ["violeta"],
        "especie": "humano"
    },
    {
        "nombre": "Aayla Secura",
        "maestros": ["Quinlan Vos"],
        "sables": ["azul"],
        "especie": "twi'lek"
    },
]

# Subindice A. listado ordenado por nombre
def listado_ordenado(jedi):
    print("\n--- Ordenado por nombre ---")
    for j in sorted(jedi, key=lambda x: x["nombre"]):
        print(j["nombre"], "-", j["especie"])
    print("\n--- Ordenado por especie ---")
    for j in sorted(jedi, key=lambda x: x["especie"]):
        print(j["nombre"], "-", j["especie"])

# Subindice B. mostrar toda la información de Ahsoka Tano y Kit Fisto
def info_personajes(jedi, nombres):
    for j in jedi:
        if j["nombre"] in nombres:
            print("\n---", j["nombre"], "---")
            for k, v in j.items():
                print(k, ":", v)

# Subindice C. mostrar todos los padawan de Yoda y Luke Skywalker
def padawans(jedi, maestros):
    print("\n--- Padawans ---")
    for j in jedi:
        for maestro in j["maestros"]:
            if maestro in maestros:
                print(j["nombre"], "fue padawan de", maestro)

# Subindice D. mostrar Jedi humanos y twi'lek
def jedi_especie(jedi, especies):
    print("\n--- Humanos y Twi'lek ---")
    for j in jedi:
        if j["especie"].lower() in especies:
            print(j["nombre"], "-", j["especie"])

# Subinidce E. listar todos los Jedi que comienzan con A
def jedi_con_A(jedi):
    print("\n--- Jedi que comienzan con A ---")
    for j in jedi:
        if j["nombre"].startswith("A"):
            print(j["nombre"])

# Subinidce F. mostrar los Jedi que usaron sable de luz de más de un color
def jedi_multicolor(jedi):
    print("\n--- Jedi con más de un color de sable ---")
    for j in jedi:
        if len(j["sables"]) > 1:
            print(j["nombre"], "-", j["sables"])

# Subindice G. indicar los Jedi que usaron sable amarillo o violeta
def jedi_colores(jedi, colores):
    print("\n--- Jedi con sable amarillo o violeta ---")
    for j in jedi:
        if any(color in j["sables"] for color in colores):
            print(j["nombre"], "-", j["sables"])

# Subindice H. padawans de Qui-Gon Jinn y Mace Windu
def padawans_de(jedi, maestros):
    print("\n--- Padawans de Qui-Gon Jinn y Mace Windu ---")
    for j in jedi:
        for maestro in j["maestros"]:
            if maestro in maestros:
                print(j["nombre"], "fue padawan de", maestro)


# Prueba general
listado_ordenado(jedi)
info_personajes(jedi, ["Ahsoka Tano", "Kit Fisto"])
padawans(jedi, ["Yoda", "Luke Skywalker"])
jedi_especie(jedi, ["humano", "twi'lek"])
jedi_con_A(jedi)
jedi_multicolor(jedi)
jedi_colores(jedi, ["amarillo", "violeta"])
padawans_de(jedi, ["Qui-Gon Jinn", "Mace Windu"])
