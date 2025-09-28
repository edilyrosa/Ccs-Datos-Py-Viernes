

# **********************************************TDD dict
# Se crea con llaves {}. 
# Colección de datos que almacena información en pares de clave:valor. 
# Con Asignación puedes crear un nuevo par (c:v) 
# o actualiza, utilizando la clave (como indice) para acceder al valor. 
# Con la asignacion, Si la clave ya existe haces actualizacion, sino creacion del elemento.
# Cada elemento es un par (c:v), y deben estar separados por “,”
# ? ⁉️QUE TDD PUEDEN SER CLAVE Y VALUE?
# clave: debe ser TDD inmutable (como un str, int, o tuple).
# valor: puede ser de cualquier TDD.


#***CREACION****
persona = {
    'nombre':'Edily',
    'peso':55.12,
    'edad':33,
    'femenida':True,
    # claves TDD Num
    102:'Maria',
    # claves TDD Bool
    True:'Si', 
    False: 'No',
    'hobbies':['cantar', 'comprar', 'programar'],
    'contactos':{
        'email':'edi@',
        'telefono':4246664
    },
    # claves tDD Tuple
    ('latitud', 'longitud'):[40.44444, -77.87666],
    (1, 2, 3):[10, 20, 30]
}

#***ACCESO A VALUES****
#print(persona[2])            # !KeyError: 2
print(persona['peso'])        # *55.12
print(persona[102])           # *Maria
print(persona['hobbies'])     # *['cantar', 'comprar', 'programar']
print(persona['hobbies'][2])     # *programar
print(persona['contactos']['telefono'])     # *4246664
print(persona[('latitud', 'longitud')])     # *[40.44444, -77.87666]
print(persona[('latitud', 'longitud')][1])     # *-77.87666
print(persona[(1, 2, 3)][2])     # *30



#*METODOS
# Tamaño: con len(dict), retorna el número de elementos.
print('len de personas', len(persona)) # *len de personas 11

# Mutabilidad: Son mutables, puedes agregar, eliminar y modificar elementos. Las claves son irrepetibles.
persona['nombre'] = 'Rositaaa'
print(persona['nombre']) #*Rositaaa
#Actualizar o crear depende de si la clave YA existe.
persona['soltera'] = True
print('len de personas', len(persona)) # *len de personas 12
print(persona)

# Acceder al Valor: 
    # dict[clave]: Lanza error si la clave no existe
    # valor = mi_diccionario.get(clave): Retorna None o un valor por defecto si la clave no existe.
print(persona.get('soltera')) # ✅True
#print(persona['noExiste']) #!KeyError: 'noExiste'
print(persona.get('noExiste')) # ✅True - None



# Eliminar un Elemento:
    # dict.pop(clave): Elimina el elemento y retorna el valor
    # dict.popitem(): Elimina el ultimo elemento.
    # del dict[clave] Elimina el elemento sin retornar nada.
    
persona.pop('soltera') 
print('len de personas', len(persona)) # *len de personas 11
persona.popitem()
print(persona)

# Vaciar Diccionario: Elimina todos los elementos.
    # dict.clear()
#persona.clear()
print(persona)

# Verificar Clave: Comprueba si una clave existe. Retorna bool.
    # clave in dict
    

print('peso' in persona) #True


 #*METODOS
# ************************************************Codigo explicacion....******************************************
#*RECORRERLOS O ITERRALOS: default con for-> claves, enumerate(), dict.values(), dict.items()
# Ordenados: mantienen el orden de inserción de los elementos.
# for clave in dict -> defalult, itera sobre las claves
# dict.values() -> itera sobre los valores
# dict.items() -> itera sobre los pares clave-valores al mismo tiempo

for key in persona:
    print(key)
    
for v in persona.values():
    print(v)
    
for c,v in persona.items():
    print(c, '-', v)





# ************************************************Codigo explicacion....******************************************
#TODO: ⛹🏽‍♂️⛹🏽‍♀️💡EJERCICIO # 1: CREA UN DICT CON 5 ELEMENTOS, LAS CLAVES SERAN {1,2,3,4,5} 
# Y LOS VALORES SERAN EL CUADRADO DE LAS CLAVES
# CREA EL DICT VACIO, LUEGO MEDIANTE UN FOR ITERA UN RANGE(1,6) PARA CREAR LOS PARES (c:v)

# # *SOLUCION EJERCICIO #1
# ************************************************Codigo Solucion EJERCICIO....******************************************
# #📖👀⁉️ A diferencia de las listas, a un dict vacío sí puedes asignar directamente valores usando una clave nueva, 
# # incluso si el dict está inicialmente vacío.
# lista_vacia = []
# lista_vacia[0] = 'hola'  #! Esto produce IndexError: list assignment index out of range

# # Esto ocurre porque la lista inicialmente no tiene elementos y no se puede asignar directamente a un índice inexistente.
# # Para agregar elementos a una lista vacía debes usar métodos como:
# # append() para añadir al final


# #TODO: ⛹🏽‍♂️⛹🏽‍♀️💡EJERCICIO PROPUESTO PARA CASA: mapeando un dict para encontra TDD num y aplicar descuento.💡⛹🏽‍♂️⛹🏽‍♀️
# persona_ejercicio = {
#     'nombre': 'Ana',
#     'femenina': True,
#     102: 100,
#     'hobbies': ['leer', 'viajar', 'codear'],
#     'contacto': {
#         'email': 'ana@ejemplo.com',
#         'telefono': '555-1234'
#     },
#     ('latitud', 'longitud'): [40.7128, -74.006],
#     (1, 2, 3): [10, 20, 30]
# }
# # Instrucciones:
# # Recorre el diccionario dict _ejercicio con un ciclo for.
# # Para cada elemento, verifica si el valor asociado es un número (ya sea entero o decimal).
# # Usa la función: isinstance(valor, (int, float)) para hacer esta comprobación.
# # ⭐isinstance(valor, (int, float)) -> verifica si valor es un de tipo int o float. Retorna bool.
# # Si el valor es numérico, calcula y aplica un descuento del 20% a ese valor.
# # Por cada valor numérico modificado, imprime un mensaje en el siguiente formato:
# # La clave es "clave", se le aplica un descuento del 20% a su valor original VALOR_ORIGINAL,
# # resultando en VALOR_CON_DESCUENTO.




# #*COPIAR UN DICT
# #  ? Copia Superficial: .copy() || dict()
# # Crea un nuevo dict, pero si el original contiene objetos mutables
# # (list o dict), ambos diccionarios apuntarán a los mismos objetos. 
# # Cualquier cambio en esos objetos anidados afectará a ambas copias.
# # Uso: Si solo contiene TDD inmutables (str, int, tuple).

# # ?Copia Profunda: import copy; copy.deepcopy()
# # Crea un diccionario totalmente independiente, replicando todos los objetos anidados. 
# # Uso: El contiene objetos mutables anidados que necesitas que sean independientes de la copia original.
# edily = {
#     'genero':'F',
#     "edad":30,                                                    # ✅TDD valor es int: INmutable, los cambios NO afectan al otro
#     ("materias", 'calificaciones'): [['math', 'bio'], [20, 19]],  # ⚠️TDD valor es List: Mutable, los cambios SI afectan al otro
#     "telefonos":{                                                 # ⚠️TDD valor es dict: Mutable, los cambios SI afectan al otro
#         "casa":42499,
#         "ofi":42400,
#     }
# }
# # &...
# # ************************************************Codigo explicacion....******************************************


# #*⛹🏽‍♂️⛹🏽‍♀️💡EJERCICIO PARA LA CASA : Manupulacion de copia profunda de dict💡⛹🏽‍♂️⛹🏽‍♀️
# # Crea una copia profunda del diccionario producto (usando copy.deepcopy).
# # 1. En la copia:
# # 2. Agrega el elemento 'moneda' con el valor ('$', '€'), imprimelo.
# # 3. Agrega el elemento 'precio_moneda' ( tipo string ), que resultará de concatenar el primer elemento de la clave moneda ('$') al valor de 'precio', imprimelo.

# # 4. Si el valor del "peso" (que está dentro de la clave ("dimensiones", "peso")) es menor o igual a "1.5kg" 
# # (extraer la parte numerica de ese str y remplaza 'el texto 'kg' por '', y conviertelo a float),
# # aplica un 20% de descuento sobre el "precio" (modifica el valor del precio).

# # 5. Extrae solo los valores numéricos de las "dimensiones" y guárdalos en una list (identifica el separador y str.split('separador')-> list).
# # tendras que limpiar el ultimo elemento con str.replace('cm', ''), luego conviertelos a float.

# # 6. Finalmente, imprime en consola el mensaje:
# # print(f'Escríbele a "{nombre_proveedor}" al correo "{email_proveedor}" para pedir descuento del producto "{nombre_producto}".')

# print('=='*30, 'EJERCICIO #4', '=='*30)
# import copy
# producto = {
#     "nombre": "Laptop XYZ",
#     "precio": 1200.50,
#     "en_stock": True,
#     101: "Electrónica",
#     "características": ["16GB RAM", "512GB SSD", "Intel i7"],
#     "proveedor": {
#         "nombre": "Proveedor ABC",
#         "contacto": "contacto@abc.com"
#     },
#     ("dimensiones", "peso"): ["30cm x 20cm x 2cm", "1.5kg"],
#     (2023, 9, 15): "Fecha de lanzamiento"
# }



