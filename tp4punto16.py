from datetime import datetime
# Clase base para una tarea
class Tarea:
    def __init__(self, nombre, costo, tiempo, fecha_inicio, fecha_fin_estimada, fecha_fin_efectiva, persona):
        self.nombre = nombre
        self.costo = costo
        self.tiempo = tiempo
        self.fecha_inicio = fecha_inicio
        self.fecha_fin_estimada = fecha_fin_estimada
        self.fecha_fin_efectiva = fecha_fin_efectiva
        self.persona = persona

    def esta_finalizada(self):
        return self.fecha_fin_efectiva != ""

    def finalizada_en_tiempo(self):
        if not self.esta_finalizada():
            return False
        return self.fecha_fin_efectiva <= self.fecha_fin_estimada

    def __str__(self):
        return (f"Tarea: {self.nombre} | Persona: {self.persona} | "
                f"Inicio: {self.fecha_inicio} | Fin Est.: {self.fecha_fin_estimada} | "
                f"Fin Efectiva: {self.fecha_fin_efectiva or 'Pendiente'} | "
                f"Costo: ${self.costo} | Tiempo: {self.tiempo} días")

# Clase lista de tareas 
class ListaTareas(list):
    def search(self, value, field):
        """Busca una tarea por campo (nombre, persona, etc.)"""
        for i, tarea in enumerate(self):
            if getattr(tarea, field).lower() == str(value).lower():
                return i
        return None

    def delete_value(self, value, field):
        """Elimina una tarea según un campo dado"""
        pos = self.search(value, field)
        if pos is not None:
            return self.pop(pos)
        return None

    def show(self):
        """Muestra todas las tareas"""
        for tarea in self:
            print(tarea)
        print()

    #Funciones necesarias

    def tiempo_promedio(self):
        total = sum(t.tiempo for t in self)
        return total / len(self) if len(self) > 0 else 0

    def costo_total(self):
        return sum(t.costo for t in self)

    def actividades_por_persona(self, persona):
        return [t for t in self if t.persona.lower() == persona.lower()]

    def tareas_entre_fechas(self, fecha1, fecha2):
        return [t for t in self if fecha1 <= t.fecha_inicio <= fecha2]

    def tareas_finalizadas_en_tiempo(self):
        en_tiempo = [t for t in self if t.esta_finalizada() and t.finalizada_en_tiempo()]
        fuera_tiempo = [t for t in self if t.esta_finalizada() and not t.finalizada_en_tiempo()]
        return en_tiempo, fuera_tiempo

    def tareas_pendientes_por_persona(self, persona):
        return [t for t in self if t.persona.lower() == persona.lower() and not t.esta_finalizada()]


# Carga de tareas
lista_tareas = ListaTareas([
    Tarea("Análisis de Requisitos", 1200, 10, "2025-10-01", "2025-10-10", "2025-10-09", "Agostina"),
    Tarea("Diseño del Sistema", 1500, 15, "2025-10-11", "2025-10-25", "2025-10-27", "Walter"),
    Tarea("Implementación Módulo A", 1800, 20, "2025-10-20", "2025-11-10", "2025-11-08", "Agostina"),
    Tarea("Pruebas Unitarias", 1000, 8, "2025-11-11", "2025-11-19", "", "Walter")
])

print("PROYECTO DE SOFTWARE\n")
# Subindice A) Tiempo promedio
print(f"A) Tiempo promedio de tareas: {lista_tareas.tiempo_promedio():.2f} días")

#Subindice B) Costo total
print(f"B) Costo total del proyecto: ${lista_tareas.costo_total()}")

#Subindice C) Actividades realizadas por una persona
persona = "Agostina"
print(f"\nC) Actividades realizadas por {persona}:")
for t in lista_tareas.actividades_por_persona(persona):
    print(" -", t.nombre)

# Subindice D) Tareas entre dos fechas
print("\nD) Tareas entre 2025-10-01 y 2025-10-20:")
for t in lista_tareas.tareas_entre_fechas("2025-10-01", "2025-10-20"):
    print(" -", t.nombre)

# Subindice E) Finalizadas en tiempo y fuera de tiempo
en_tiempo, fuera_tiempo = lista_tareas.tareas_finalizadas_en_tiempo()
print("\nE) Tareas finalizadas en tiempo:")
for t in en_tiempo:
    print(" -", t.nombre)
print("\n   Tareas fuera de tiempo:")
for t in fuera_tiempo:
    print(" -", t.nombre)

# Subindice F) Tareas pendientes por persona
persona2 = "Walter"
pendientes = lista_tareas.tareas_pendientes_por_persona(persona2)
print(f"\nF) Tareas pendientes de {persona2}: {len(pendientes)}")
for t in pendientes:
    print(" -", t.nombre)

# Mostrar todo
print("\nTODAS LAS TAREAS")
lista_tareas.show()
