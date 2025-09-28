mi_lista = [1, 2, 3, 4, 5]
mi_lista = ('hola', 2, False, 4, 12.12)

for ele in mi_lista:
    print(ele)
    
for letras in 'hola mundo':
    print(letras)
    
for e in range(2, 10, 2): # 0, 1, 2, 3, 4, 5
    print(e)
    
for e in [1, 2, 3, 4, 5]:
    print(e**2)


# *break, continue y pass: se usan en los bucles para alterar el flujo normal del ciclo.
print('=='*10, 'break, continue y pass', '=='*10)
for e in range(1, 10):
    if e == 3:
        #break  # rompe el ciclo
        #continue  # salta a la siguiente iteracion
        pass  # no hace nada, es un placeholder
    print(e)
print('HOLA SOY PROGRAMA FUERA DE LOOPS')

# #***************** MATRICES Y SU RECORRIDO: FOR ANIDADO
# Una matriz en Python se representa comúnmente como una lista de listas 
# (una lista donde cada elemento es otra lista que representa una fila). 
# Para recorrer todos sus elementos con un for, 
# lo ideal es usar bucles anidados (un for dentro de otro).

lista = [1, 2, 3]

matriz = [
    [0, 2, 3],  # fila 0
    [4, 0, 6],  # fila 1
    [7, 8, 0]   # fila 2
]

print(matriz[0])  # [1, 2, 3]
print(matriz[1][2])  #6


print(matriz[0][0])  #1
print(matriz[1][1])  #5
print(matriz[2][2])  #9


for fila in matriz:  # Recorre cada fila de la matriz
    for elemento in fila:  # Recorre cada elemento dentro de la fila
        print(elemento)
    
matriz = [
    [1, 2, 3],  # fila 0
    [4, 5, 6, True, 12.12],  # fila 1
    [7]   # fila 2
]

sabores = ['ch', 'fr', 'man']

edily = {
    'nombre': 'edily',
    'edad': 7,
    'sabores_favoritos': sabores,
    'matriz': matriz
}