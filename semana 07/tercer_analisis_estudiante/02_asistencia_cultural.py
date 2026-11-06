"""Caso 2: asistencia por bloques. Complete el análisis con un ciclo for."""

asistencias = [120, 180, 210, 250, 230]
capacidad = 300

# TODO: Recorra asistencias con for para acumular el total y contar los bloques
#       que SUPERAN el 70 % de la capacidad (210 no cuenta).
total_asistencia = 0
capacidad_mayor_setenta = 0
limite_capacidad = capacidad * 0.70

for asistencia in asistencias:
    total_asistencia += asistencia
    if asistencia > limite_capacidad:
        capacidad_mayor_setenta += 1

# TODO: Calcule el promedio y su porcentaje de ocupación.
promedio = total_asistencia / len(asistencias) 
ocupacion = promedio / capacidad * 100
#print(promedio)
#print(ocupacion)

# TODO: Clasifique el promedio: >=80 % alta; >=50 % media; si no, baja.
if ocupacion >= 80:
    estado = "Alta"
elif ocupacion >= 50:
    estado = "Media"
else:
    estado = "Baja"

# TODO: Muestre total, promedio, porcentaje, cantidad de bloques y estado.
# Con los datos base: total 990, promedio 198, 66 %, 2 bloques, ocupación media.
print('			Asistencia Cultural')
print('_' * 70, "\n")
print(f"Total de asistencias: {total_asistencia}")
print(f"Promedio por bloque: {promedio}")
print(f"Porcentaje de ocupación: {ocupacion:.2f}%")
print(f"Bloques que superan el 70%: {capacidad_mayor_setenta}")
print(f"Estado de ocupación : {estado}")

# Prueba de código: use temporalmente cinco bloques con 240 asistentes cada uno
# para comprobar el límite del 80 %. Después restaure la lista.
