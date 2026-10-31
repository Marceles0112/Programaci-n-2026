#Leer una nota, Si la nota es mayor o igual a 90
#Excelente, si la nota es mayor a 80 = Muy bueno
#Nota mayor a 70 = Aprobado
#Nota inferior a 70 es Reprobado
nota = float(input('Ingrese una nota (0-100): '))

if(nota > 100) or (nota < 0):
    print('Error: nota no válida, debe de ser entre 0-100')
else:
    if nota >= 90:
        print('Excelente!')
    elif nota > 80:
        print('Muy bien!')
    elif nota >= 70:
        print('Aprobado')
    else: 
        print('Reprobado')
