#Situación: Queremos saber en qué año nació una persona basándonos en su edad actual, asumiendo que ya cumplió años en el 2025.
#Entrada
anio_actual = 2026
edad_actual = int(input('Ingrese su edad actual: '))
#Proceso
anio_nacimiento = anio_actual - edad_actual
#Salida
print('Usted nacio aproximadamente en: ', anio_nacimiento)