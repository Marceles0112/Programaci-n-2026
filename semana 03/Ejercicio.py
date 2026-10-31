#Producción en clase: Juan Carlos Jimenez y María Celeste Madrigal

cuenta_bancaria = float(input('Cuanto dinero dispone en su banco: '))
antecedentes_penales = input('tiene antecedenetes penales?: ')
profesion = input ('Ingrese su profesion: ')
if (cuenta_bancaria >= 50000 and antecedentes_penales == 'no') or (profesion == 'diplomatico'):
    print ('APROBADO: VISA DORADA')
elif (cuenta_bancaria >= 20000 and antecedentes_penales == 'no'):
    print('APROBADO: VISA ESTÁNDAR')
elif (cuenta_bancaria < 20000 and profesion == 'estudiante' or profesion == 'jubilado'):
    print('PENDIENTE: Requiere entrevista')
else:
    print('DENEGADO')
    