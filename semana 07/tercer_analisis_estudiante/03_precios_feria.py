"""Caso 3: comparación de precios de un producto en cinco ferias."""

producto = "Tomate"
precios = [900, 850, 1000, 950, 1200]
total = sum(precios)
#print(total)

# TODO: Calcule promedio, mínimo, máximo y rango (máximo - mínimo).
promedio = total / len(precios) 
#print(promedio)
minimo = min (precios)
#print(minimo)
maximo = max (precios)
#print(maximo)
rango = (maximo - minimo)
#print(rango)

# TODO: Recorra precios con while y un índice para contar los que SUPERAN
#       el promedio. Aumente el índice en cada vuelta para terminar el ciclo.
indice = 0
promedio_superior = 0

while indice < len(precios):
    if precios[indice] > promedio:
        promedio_superior += 1
    indice += 1

#print(promedio_superior)

# TODO: Clasifique el rango: >=300 variación alta; >=150 moderada; si no, baja.
if rango >= 300:
    estado = "Variacion alta"
elif rango >= 150:
    estado = "Moderada"
else:
    estado = "Baja"

# TODO: Muestre producto y todos los resultados.
# Con los datos base: promedio ₡980, mínimo ₡850, máximo ₡1200,
# rango ₡350, 2 precios sobre el promedio, variación alta.

print('							   Precios Feria')
print('_' * 130, "\n")
print(f"Promedio: ₡{promedio:.2f} | Precio mínimo: ₡{minimo} | Precio máximo: ₡{maximo} | Rango: ₡{rango} | Precios sobre el promedio: {promedio_superior} | {estado}" )

# Prueba de código: use temporalmente cinco precios iguales y compruebe que
# el rango sea cero y ninguno supere el promedio. Restaure la lista.
