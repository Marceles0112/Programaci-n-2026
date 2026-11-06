"""Caso 4: analice los registros de soporte sin crear funciones propias."""

from incidencias import incidencias

# Cada incidencia es un diccionario: id, provincia, categoria,
# minutos_atencion y resuelto (True o False).

# TODO: Prepare un acumulador de minutos, un diccionario para contar
# "Acceso", "Equipo" y "Red", un contador de casos pendientes,
# un set de provincias con pendientes, una lista de tuplas de casos
# urgentes y una tupla para el caso con más minutos de atención.

total_minutos = 0
conteo_categorias = {"Acceso": 0, "Equipo": 0, "Red": 0}
casos_pendientes = 0
provincias_pendientes = set()
casos_urgentes = []
max_minutos_caso = ("", 0) # (id_caso, minutos)

# TODO: Recorra incidencias una sola vez. Actualice los acumuladores y el
# conteo de la categoría de cada registro.
for inc in incidencias:
    total_minutos += inc["minutos_atencion"]
    cat = inc["categoria"]
    if cat in conteo_categorias:
        conteo_categorias[cat] += 1

# TODO: Si un caso no está resuelto, cuéntelo y agregue su provincia al set.
# Si, además, tiene 60 minutos o más, agregue (id, minutos) a la lista
# de casos urgentes y actualice la tupla del caso más largo de atención.
    if not inc["resuelto"]:
        casos_pendientes += 1
        provincias_pendientes.add(inc["provincia"]) 
        if inc["minutos_atencion"] >= 60:
            casos_urgentes.append((inc["id"], inc["minutos_atencion"])) 
        if inc["minutos_atencion"] > max_minutos_caso[1]:
            max_minutos_caso = (inc["id"], inc["minutos_atencion"])

# TODO: Muestre total y promedio de minutos, conteo por categoría, cantidad
# de pendientes, provincias con pendientes, urgentes y el caso más largo.
promedio_minutos = total_minutos / len(incidencias) if incidencias else 0

print('			    Soporte Universitario')
print('_' * 80, "\n")
print(f"Total de minutos: {total_minutos} ")
print(f"Promedio: {promedio_minutos:.2f}%")
print(f"Conteo por categoría: {conteo_categorias}")
print(f"Casos pendientes: {casos_pendientes}")
print(f"Provincias con pendientes: {provincias_pendientes}")
print(f"Casos urgentes (>= 60 min): {casos_urgentes}")
print(f"Caso con más minutos de atención: ID {max_minutos_caso[0]} con {max_minutos_caso[1]} minutos")

# Prueba: cambie temporalmente INC-07 a resuelto=True. Debe salir de la
# lista de urgentes, del conteo de pendientes y del set de provincias
# pendientes, pero seguir como caso más largo. Restaure incidencias.py.
