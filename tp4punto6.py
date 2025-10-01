# Lista de superhéroes
superheroes = [
    {"nombre": "Linterna Verde", "año": 1940, "casa": "DC", "bio": "Usa un anillo de poder con su traje especial."},
    {"nombre": "Wolverine", "año": 1974, "casa": "Marvel", "bio": "Mutante con garras de adamantium y factor curativo."},
    {"nombre": "Dr. Strange", "año": 1963, "casa": "DC", "bio": "Hechicero supremo, maestro de las artes místicas."},
    {"nombre": "Capitana Marvel", "año": 1968, "casa": "Marvel", "bio": "Piloto con poderes cósmicos y traje militar."},
    {"nombre": "Mujer Maravilla", "año": 1941, "casa": "DC", "bio": "Guerrera amazona con armadura mágica."},
    {"nombre": "Flash", "año": 1940, "casa": "DC", "bio": "El hombre más rápido del mundo."},
    {"nombre": "Star-Lord", "año": 1976, "casa": "Marvel", "bio": "Aventurero espacial con máscara y traje especial."},
    {"nombre": "Batman", "año": 1939, "casa": "DC", "bio": "El caballero oscuro con traje y gadgets."},
    {"nombre": "Spider-Man", "año": 1962, "casa": "Marvel", "bio": "Joven héroe con traje arácnido."},
    {"nombre": "Superman", "año": 1938, "casa": "DC", "bio": "El hombre de acero con armadura invulnerable."}
]

#Subindice A. eliminar  a Linterna Verde
superheroes = [s for s in superheroes if s["nombre"] != "Linterna Verde"]

#Subindice B. el año de aparición de Wolverine
for s in superheroes:
    if s["nombre"] == "Wolverine":
        print("b) Wolverine apareció en:", s["anio"])

#Subindice C. cambiarle la casa de Dr. Strange
for s in superheroes:
    if s["nombre"] == "Dr. Strange":
        s["casa"] = "Marvel"

#Subindice D. Listar nombres que contengan la palabra "traje" o "armadura"
print("\nd) Superhéroes con 'traje' o 'armadura':")
for s in superheroes:
    if "traje" in s["bio"].lower() or "armadura" in s["bio"].lower():
        print("-", s["nombre"])

#Subindice E. nombre y casa de los anteriores a 1963
print("\ne) Superhéroes con aparición antes de 1963:")
for s in superheroes:
    if s["anio"] < 1963:
        print("-", s["nombre"], "(", s["casa"], ")")

#Subindice F. casa de Capitana Marvel y Mujer Maravilla
print("\nf) Casas de:")
for s in superheroes:
    if s["nombre"] in ["Capitana Marvel", "Mujer Maravilla"]:
        print("-", s["nombre"], ":", s["casa"])

#Subindice G. toda la info de Flash y Star-Lord
print("\ng) Información de Flash y Star-Lord:")
for s in superheroes:
    if s["nombre"] in ["Flash", "Star-Lord"]:
        print(s)

#Subindice H. listar los que empiezan con B, M o S
print("\nh) Superhéroes que empiezan con B, M o S:")
for s in superheroes:
    if s["nombre"][0] in ["B", "M", "S"]:
        print("-", s["nombre"])

# i. cantidad de superhéroes por casa
conteo = {}
for s in superheroes:
    conteo[s["casa"]] = conteo.get(s["casa"], 0) + 1

print("\ni) Cantidad por casa:", conteo)
