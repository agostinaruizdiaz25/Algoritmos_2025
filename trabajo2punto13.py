#definir la pila con ejemplos de los trajes de Iron Man
pila_trajes = [
    {'modelo': 'Mark XLIV','pelicula': 'Avengers: Age of Ultron', 'estado':'dañado'},
    {'modelo': 'Mark L','pelicula': 'Avengers: Infinity War', 'estado':'Destruido'},
    {'modelo': 'Mark LXXXV','pelicula': 'Avengers: Endgame', 'estado':'impecable'},
    {'modelo': 'Mark XLVII','pelicula': 'SpiderMan:Homecoming', 'estado':'dañado'},
    {'modelo': 'Mark XLVI','pelicula': 'Capitan America:Civil War', 'estado':'impecable'},
    {'modelo': 'Mark XLV','pelicula': 'Avengers: Age of Ultron', 'estado':'impecable'},
]
#subindice A, ¿se uso el Hulkbuster?
peliculas_hulkbuster = [traje['pelicula'] for traje in pila_trajes if traje['modelo'] == 'Mark XLIV']
if peliculas_hulkbuster:
    print("el modelo Mark XLV fue utilizado en:")
    for peli in peliculas_hulkbuster:
        print(f" - {peli}")
else:
        print ("el modelo no ha sido utilizado en ninguna pelicula del MCU")
#subindice B muestra de modelos dañados
print("los modelos dañados son:")
for traje in pila_trajes:
    if traje['estado'] == 'dañado':
        print(f"-{traje['modelo']} (pelicula:{traje['pelicula']})")
        
#subindice C, eliminacion de los modelos destruidos, para eso creamos una nueva pila
destruidos_pila = []
print("eliminar trajes destruidos:")
for traje in pila_trajes:
     if traje['estado'] == 'destruido':
         print(f"-{traje['modelo']}(pelicula:{traje['pelicula']}) eliminado")
else:
      destruidos_pila.append(traje)
      
pila_trajes = destruidos_pila #esto se hace para actualizar la pila original
#subindice D, modelos por pelicula y por repeticion, punto ya contemplado e integrado en los demas, ya que cada pila es independiente aun cuando el modelo o pelicula se repita.
#subindice E. Agregar el modleo Mark LXXXV
modelo_nuevo = {'modelo': 'Mark LXXV', 'pelicula':'avengers:endgame','estado':'impecable'}
#implementamos un repetir para comprobar si el modelo existe en la pelicula
repetido = any (traje['modelo'] == modelo_nuevo['modelo'] and traje ['pelicula'] == modelo_nuevo['pelicula']
               for traje in pila_trajes)
if not repetido:
    pila_trajes.append(modelo_nuevo)
    print('modleo Mark LXXXV se ha agregado')
else:
    print ('el modelo ya ha sido cargado')
#subindice F, trajes que se han usado en SM:H y CA:CW
peliculas_buscadas = ['spiderman:homecoming', 'capitan america:civil war']
print ("trajes usados en las peliculas buscadas:")
for traje in pila_trajes:
    if traje['pelicula'] in peliculas_buscadas:
        print(f" - {traje['modelo']} en {traje['pelicula']}")