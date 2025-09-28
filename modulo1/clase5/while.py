# #***********************************************WHILE**************************************
# Para repetir un bloque de código mientras una condición sea verdadera.  
# El código dentro del bucle se ejecuta repetidamente hasta que la condición se vuelve falsa.

#* SINTAXIS
# inicialización de la variable de controlN*****************************!FUERA!⚠️
# ⭐while condición:
#     # Bloque de código a ejecutar mientras la condición sea True
#     # Actualización de la variable de control global, **************!ADENTRO⚠️🚩

# *⁉️Cómo funciona
# Se evalúa la condición.
# Si la condición es verdadera (True), se ejecuta el bloque de código.
# Luego se vuelve a evaluar la condición.
# Cuando la condición sea falsa, NO se entra al bucle y se continúa con el resto del programa.
# ************************************************Codigo explicacion....******************************************

contador = 5                #!INICIALIZA AFUERAAAAAAAAAAAAAA!!!!❌⚠️
while contador >= 0:
  print('Contador', contador)
  contador -= 1             #!#ACTUALIZA DENTRO DEL CICLO!!!!❌⚠️



# *⭐Uso típico del while
# Cuando no sabemos de antemano cuántas veces se repetirá el ciclo.
# Cuando la repetición depende de una condición dinámica, cambiante, o del usuario. eg, menu.
# En combinación con break, continue y pass para salir anticipadamente o alterar la iteracion.
# ************************************************Codigo explicacion....******************************************

while True:
    entrada = input('Escribe "salir" para romper el ciclo infonito: ')
    if entrada == 'salir':
        break
    
    

#*⛹🏽‍♂️⛹🏽‍♀️💡EJERCICIO #1: Genere y muestre la tabla de multiplicar de un número específico.💡⛹🏽‍♂️⛹🏽‍♀️
# El programa debe pedirle al usuario que ingrese un número entero y luego,
# utilizando un bucle, debe imprimir la tabla de multiplicar de ese número del 1 al 10.
# Luego altere el programa para imprimir la tabla de multiplicar de ese número de 2 en 2 al 10.
# ************************************************Codigo Solucion....******************************************

num = int(input('dame el num'))

i = 0  #1,2,... 9, 10                             #!INICIALIZA AFUERAAAAAAAAAAAAAA!!!!❌⚠️
while i <= 10:
    print(f'{i} X {num} = {i*num}') 
    i += 2                                      #!#ACTUALIZA DENTRO DEL CICLO!!!!❌⚠️
print(i)

# 0 X 8 = 0
# 1 X 8 = 8
# 2 X 8 = 16
# 4 X 8 = 
# ..
# 10 X