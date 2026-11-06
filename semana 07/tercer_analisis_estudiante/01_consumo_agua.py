"""Caso 1: cambio del consumo diario de agua. Complete el programa."""

consumos_litros = [120, 115, 108, 102, 96]

# TODO: Calcule el consumo total y el promedio diario.
consumo_total = sum(consumos_litros)
#print(consumo_total)
promedio_diario = consumo_total / len (consumos_litros) 
#print(promedio_diario)
# TODO: Compare el primer día con el último: litros ahorrados y porcentaje
#       de reducción respecto al primer día.
ahorro = consumos_litros[0] - consumos_litros[4]
#print(ahorro)
porcentaje_reduccion = ahorro / consumos_litros[0] * 100
#print(porcentaje_reduccion)

# TODO: Clasifique: >=15 % reducción alta; >0 % reducción moderada;
#       de lo contrario, sin reducción.
if porcentaje_reduccion >= 15 :
    estado = "Reduccion alta"
elif porcentaje_reduccion >0 :
    estado = "Reduccion moderada"
else:
    estado = "Sin reduccion"
    
# TODO: Muestre los cinco resultados.
# Control: total 541 L; promedio 108,2 L; ahorro 24 L; reducción 20 %;
#          reducción alta.
print('			    Comsumo de agua')
print('_' * 80, "\n")
print(f"Total {consumo_total} L |  Promedio {promedio_diario:.2f}L | Ahorro {ahorro}L | Reducción {porcentaje_reduccion:.0f}% | {estado}" )


# Prueba: use temporalmente cinco consumos iguales. Debe indicar 0 % y
# "Sin reducción". Restaure la lista antes de entregar.
