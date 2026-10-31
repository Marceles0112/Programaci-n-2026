#Entrada
apodo = input('Ingrese un apodo: ')
color = input('Ingrese su color favorito: ')
numero = int(input('Ingrese un número: '))
simbolo = input('Ingrese un símbolo: ')

#Proceso
contraseña = apodo + color + str (numero) + simbolo

#Salida
print('Su contraseña es: ', contraseña)