from random import choice
from datetime import datetime

# Clase Cola
class Queue:
    def __init__(self):
        self.items = []

    def arrive(self, item):
        self.items.append(item)

    def attention(self):
        if self.size() > 0:
            return self.items.pop(0)

    def on_front(self):
        if self.size() > 0:
            return self.items[0]

    def move_to_end(self):
        if self.size() > 0:
            self.items.append(self.items.pop(0))

    def size(self):
        return len(self.items)

    def show(self):
        for item in self.items:
            print(item)

# Clase Pila
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() > 0:
            return self.items.pop()

    def top(self):
        if self.size() > 0:
            return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def show(self):
        for item in reversed(self.items):
            print(item)

# creamos una función para generar notificaciones aleatorias
def generar_notificaciones(q):
    apps = ["Facebook", "Twitter", "Instagram", "LinkedIn"]
    mensajes = [
        "Mirá este curso de Python",
        "Nuevo mensaje de tu amigo",
        "Notificación general",
        "Python es tendencia",
        "Recordatorio de evento",
        "¿Querés aprender Python?",
    ]
    horas = ["11:00", "11:45", "12:30", "13:15", "15:30", "16:10"]

    for _ in range(15):
        hora = choice(horas)
        app = choice(apps)
        mensaje = choice(mensajes)
        q.arrive((hora, app, mensaje))

# subindice A. Eliminamos todas las notificaciones de Facebook
def eliminar_facebook(q):
    aux = Queue()
    while q.size() > 0:
        noti = q.attention()
        if noti[1] != "Facebook":
            aux.arrive(noti)
    while aux.size() > 0:
        q.arrive(aux.attention())

# subindice B. Mostramos las notificaciones de Twitter con "Python", sin perder datos
def mostrar_twitter_con_python(q):
    aux = Queue()
    print("\nNotificaciones de Twitter con 'Python':")
    while q.size() > 0:
        noti = q.attention()
        if noti[1] == "Twitter" and "Python" in noti[2]:
            print(noti)
        aux.arrive(noti)
    while aux.size() > 0:
        q.arrive(aux.attention())

# subindice C. Usamos la pila para almacenar notificaciones entre 11:43 y 15:57
def notificaciones_en_rango(q):
    pila = Stack()
    aux = Queue()
    inicio = datetime.strptime("11:43", "%H:%M")
    fin = datetime.strptime("15:57", "%H:%M")

    while q.size() > 0:
        noti = q.attention()
        hora_noti = datetime.strptime(noti[0], "%H:%M")
        if inicio <= hora_noti <= fin:
            pila.push(noti)
        aux.arrive(noti)

    while aux.size() > 0:
        q.arrive(aux.attention())

    print(f"\nCantidad de notificaciones entre 11:43 y 15:57: {pila.size()}")
    print("Notificaciones almacenadas en la pila:")
    pila.show()