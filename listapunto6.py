# Lista inicial de superhéroes
superheroes = [
    {"nombre": "Linterna Verde", "anio": 1940, "casa": "DC", "bio": "Usa un anillo de poder con su traje especial."},
    {"nombre": "Wolverine", "anio": 1974, "casa": "Marvel", "bio": "Mutante con garras de adamantium y factor curativo."},
    {"nombre": "Dr. Strange", "anio": 1963, "casa": "DC", "bio": "Hechicero supremo, maestro de las artes místicas."},
    {"nombre": "Capitana Marvel", "anio": 1968, "casa": "Marvel", "bio": "Piloto con poderes cósmicos y traje militar."},
    {"nombre": "Mujer Maravilla", "anio": 1941, "casa": "DC", "bio": "Guerrera amazona con armadura mágica."},
    {"nombre": "Flash", "anio": 1940, "casa": "DC", "bio": "El hombre más rápido del mundo."},
    {"nombre": "Star-Lord", "anio": 1976, "casa": "Marvel", "bio": "Aventurero espacial con máscara y traje especial."},
    {"nombre": "Batman", "anio": 1939, "casa": "DC", "bio": "El caballero oscuro con traje y gadgets."},
    {"nombre": "Spider-Man", "anio": 1962, "casa": "Marvel", "bio": "Joven héroe con traje arácnido."},
    {"nombre": "Superman", "anio": 1938, "casa": "DC", "bio": "El hombre de acero con armadura invulnerable."}
]

# a. eliminar Linterna Verde
superheroes = [s for s in superheroes if s["nombre"] != "Linterna Verde"]

# b. año de aparición de Wolverine
for s in superheroes:
    if s["nombre"] == "Wolverine":
        print("b) Wolverine apareció en:", s["anio"])

# c. cambiar la casa de Dr. Strange a Marvel
for s in superheroes:
    if s["nombre"] == "Dr. Strange":
        s["casa"] = "Marvel"

# d. nombres con "traje" o "armadura"
print("\nd) Superhéroes con 'traje' o 'armadura':")
for s in superheroes:
    if "traje" in s["bio"].lower() or "armadura" in s["bio"].lower():
        print("-", s["nombre"])

# e. nombre y casa de los anteriores a 1963
print("\ne) Superhéroes con aparición antes de 1963:")
for s in superheroes:
    if s["anio"] < 1963:
        print("-", s["nombre"], "(", s["casa"], ")")

# f. casa de Capitana Marvel y Mujer Maravilla
print("\nf) Casas de:")
for s in superheroes:
    if s["nombre"] in ["Capitana Marvel", "Mujer Maravilla"]:
        print("-", s["nombre"], ":", s["casa"])

# g. toda la info de Flash y Star-Lord
print("\ng) Información de Flash y Star-Lord:")
for s in superheroes:
    if s["nombre"] in ["Flash", "Star-Lord"]:
        print(s)

# h. listar los que empiezan con B, M o S
print("\nh) Superhéroes que empiezan con B, M o S:")
for s in superheroes:
    if s["nombre"][0] in ["B", "M", "S"]:
        print("-", s["nombre"])

# i. cantidad de superhéroes por casa
conteo = {}
for s in superheroes:
    conteo[s["casa"]] = conteo.get(s["casa"], 0) + 1

print("\ni) Cantidad por casa:", conteo)
