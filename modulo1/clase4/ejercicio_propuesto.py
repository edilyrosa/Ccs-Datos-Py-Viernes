# Ejercicio # 3: Recorriendo Matriz + Condicionales
# Imprima SOLO los elementos de la diagonal principal de la siguiente matriz.
# La diagonal principal de una matriz cuadrada, son los elementos donde el 
# índice de fila es igual al índice de columna, es decir, donde i == j.
matriz = [
    [0, 1, 1, 5],  # fila 0
    [1, 0, 1],  # fila 1
    [1, 1, 0],  # fila 2
    'Edily', 
    {'uno':1, 'dos':2, 'tres':3, 'tress':3}
]
[1, 2, 3]
# for i in range(6): {0-5}

for i in range(len(matriz)): #0, 1, 2
    for j in range(len(matriz[i])): # 0, 1, 2
        if i == j:
            print(f'Diagonal matriz[{i}][{j}] = {matriz[i][j]}')
    


















































# La diagonal principal de una matriz cuadrada, son los elementos donde el índice de fila es 
# igual al índice de columna, es decir, donde i == j.
# matriz = [
#     [0, 1, 1], # fila 0
#     [1, 0, 1], # fila 1
#     [1, 1, 0]  # fila 2
# ]

# for i in range(len(matriz)): # recorre 0, 1, 2 - indices de filas
#     for j in range(len(matriz[i])): # recorre 0, 1, 2 - indices de columnas en fila i
#         if i == j:
#             print(f"Diagonal[{i}][{j}] = {matriz[i][j]}")
