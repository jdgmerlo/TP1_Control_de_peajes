#Trabajo Práctico N° 1 - Control de Peajes

IMP_ARGENTINA = 300
IMP_BRASIL = 400
IMP_BOLIVIA = 200
IMP_PARAGUAY = 300
IMP_URUGUAY = 300

patente = input('Ingrese patente del vehículo: ')

if(len(patente) == 7):
    if(patente[0:1].isalpha() and patente[2:4].isnumeric() and patente[5:6].isalpha()):
        nacionalidad = 'Argentina'
    elif(patente[0:2].isalpha() and patente[3].isnumeric() and patente[4].isalpha() and patente[5:6].isnumeric()):
        nacionalidad = 'Brasil'
    elif(patente[0:1].isalpha() and patente[2:6].isnumeric()):
        nacionalidad = 'Bolivia'
    elif(patente[0:3].isalpha() and patente[4:6].isnumeric()):
        nacionalidad = 'Paraguay'
    elif(patente[0:2].isalpha() and patente[3:6].isnumeric()):
        nacionalidad = 'Uruguay'
    else:
        nacionalidad = 'Otro'
else:
    nacionalidad = 'Otro'

print('-' * 20)
print('Motocicleta ---> 0')
print('Automóvil ---> 1')
print('Camión ---> 2')

tipo_vehiculo = int(input('Ingrese tipo de vehículo: '))

print('-' * 20)
print('Manual    ---> 1')
print('Telepeaje ---> 2')

forma_pago = int(input('Ingrese forma de pago: '))

print('-' * 20)
print('Argentina ---> 0')
print('Brasil    ---> 1')
print('Bolivia   ---> 2')
print('Paraguay  ---> 3')
print('Uruguay   ---> 4')

pais = int(input('Ingrese país de cabina atravesada: '))

print('-' * 20)

distancia = float(input('Ingrese distancia(Km): '))

#Impresión del ticket.

print('*' * 20)
print('***TICKET***')
print('*' * 20)
print('País de procedencia del vehículo: ', nacionalidad)

if(pais == 0):
    if(tipo_vehiculo == 0):
        importe_basico = (50 * IMP_ARGENTINA) / 100
    elif(tipo_vehiculo == 1):
        importe_basico = IMP_ARGENTINA
    elif(tipo_vehiculo == 2):
        importe_basico = IMP_ARGENTINA + ((60 * IMP_ARGENTINA) / 100)
elif(pais == 1):
    if (tipo_vehiculo == 0):
        importe_basico = (50 * IMP_BRASIL) / 100
    elif (tipo_vehiculo == 1):
        importe_basico = IMP_BRASIL
    elif (tipo_vehiculo == 2):
        importe_basico = IMP_BRASIL + ((60 * IMP_BRASIL) / 100)
elif(pais == 2):
    if (tipo_vehiculo == 0):
        importe_basico = (50 * IMP_BOLIVIA) / 100
    elif (tipo_vehiculo == 1):
        importe_basico = IMP_BOLIVIA
    elif (tipo_vehiculo == 2):
        importe_basico = IMP_BOLIVIA + ((60 * IMP_BOLIVIA) / 100)
elif (pais == 3):
    if (tipo_vehiculo == 0):
        importe_basico = (50 * IMP_PARAGUAY) / 100
    elif (tipo_vehiculo == 1):
        importe_basico = IMP_PARAGUAY
    elif (tipo_vehiculo == 2):
        importe_basico = IMP_PARAGUAY + ((60 * IMP_PARAGUAY) / 100)
elif (pais == 4):
    if (tipo_vehiculo == 0):
        importe_basico = (50 * IMP_URUGUAY) / 100
    elif (tipo_vehiculo == 1):
        importe_basico = IMP_URUGUAY
    elif (tipo_vehiculo == 2):
        importe_basico = IMP_URUGUAY + ((60 * IMP_URUGUAY) / 100)

print('Importe básico a pagar: $', importe_basico)

if(forma_pago == 2):
    importe_final = importe_basico - ((10 * importe_basico) / 100)
elif(forma_pago == 1):
    importe_final = importe_basico

print('Importe final a pagar: $', importe_final)

valor_kilometro = importe_final / distancia

print('Valor promedio pagado por kilómetro: $', valor_kilometro)