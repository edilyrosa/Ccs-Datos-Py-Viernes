print('linea 1')
print('linea 2')
x = True
z = 7 == 7
if x and z:
    print('✅SOY IF')
    # print('soy otra linea del bloque if')
else:
    print('🚩SOY ELSE')
    
print('linea 3')
print('linea 4')
print('soy del programa ordinario')

print('ANIDACION IF EN ELSE')
z = 0 
if z > 0:
    print('✅z es mayor')
else:
    if z < 0:
        print('⚠️z es menor que 0')
    else:
        print('🚩z es 0')
  
    
print('ANIDACION ELIF')
z = 0 
if z > 0:
    print('✅z es mayor')
elif z < 0:
    print('⚠️z es menor que 0')
else:
    print('🚩z es 0')
  

print('=='*10, 'if', '=='*10)
# como saber si un num es par y luego si es positivo?
# num = int(input('ingresa un numero: '))
num = 12
print(num % 2 == 0)  
print('⭐El num es par y positivo')
print('👀El num es 0')
print('⚠️El num es par y negativo')

if num % 2 == 0:
    if num > 0:
        print('⭐El num es par y positivo')
    elif num == 0:
        print('👀El num es 0')
    else:
        print('⚠️El num es par y negativo')
        
else:
    print('⚠️El num es impar y NO me interesa seguir')


#condicion compuesta: diga si usuario puede conducir, para poder debe:
# ser mayor_edad AND (tener_permiso OR ser_emanicipado), el tiene 17
MAYORIADAD = 18
edad = 18
mayor_edad = edad >= MAYORIADAD
tener_permiso = 'si'
ser_emanicipado = True

tener_permiso = input('tiene permiso? si/no: ')
# IsAuth = password ==  True
if edad>=MAYORIADAD and (tener_permiso == 'si' or ser_emanicipado):
    print('✅Puede conducir')
else:
    print('🚩No puede conducir') #🚩No puede conducir








if mayor_edad and (tener_permiso or ser_emanicipado):
    print('✅Puede conducir')
else:
    print('🚩No puede conducir') #🚩No puede conducir





# condional ternario
edad = 18
mensaje = 'Es mayor' if edad >= 18 else 'Es menor'
print(mensaje) # Es mayor