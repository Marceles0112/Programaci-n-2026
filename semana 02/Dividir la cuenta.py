#Situación: Saliste a comer pizza con amigos. Llegó la cuenta total y quieren dividirla en partes iguales.
#Entrada
total = float(input('Ingrese el monto de la cuenta: '))
cantidad_personas = int(input('Ingrese la cantidad de personas: '))

#Proceso
pago_persona = total / cantidad_personas

#Salida
print('Monto a pagar por persona: ', pago_persona)