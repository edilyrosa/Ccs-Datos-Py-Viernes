#  ******************************FUNCIONES CON def *********************************************
# Bloque de código de sentencias que realiza una tarea específica en el programa, 
# siendo reusable. Usamos funciones para modular y evitar la repetición. 
# La keyword "def" es usada para definir una función.
# 
# ⭐Argumentos: datos que pueda necesitar una función para realizar su tarea, y
# serán pasados dentro de sus parentesis de ejecucion, separados por ","
# pasa tantos, como parámetros se haya declarado en su definición, 
# a menos que sean variables globales.  
# 
# ⭐La función podría o no retornar un valor o resultado, con la instrucción return.
# return termina una función y opcionalmente devuelve un valor.

# *SINTAXIS:
#  def nombre_funcion(parámetros_opcionales):
#     # Bloque de código indentado que define lo que hace la función
#     instrucciones
#     return valor_retorno_opcional
# Ejemplos:
# ************************************************Codigo explicacion....******************************************
def saludar_standar():
    print('Hola Usuario')

saludar_standar()

var_global = 'Usuari@'
def saludar_var_global():
    print(f'Hola {var_global}')
    
saludar_var_global()

def saludar_con_parametro(nombre):
    print(f'Hola {nombre}')
    
saludar_con_parametro('Edily') 
saludar_con_parametro(12) 

def suma(a, b):
    return a + b

resultado= suma(5, 5) + 100
print(resultado)



#  ******************************ÁMBITO DE VARIABLES GLOBALES EN FUNCIONES*********************************************
# ⭐Por default, en ámbito local, solo podemos leer una variables globales, 
# ❌NO modificarla.
# Dentro de un ámbito local (función), puedes modificar una variable global, 
# usar la keyword global antes de intentar modificarla. Como 1era declaracion en la func
# ⚠️Cuidado, la modificación afectara el valor de la variable, local y globalmente.
# Esto NO es una buena practica⚠️

x = 100
def cambiando_x():
    global x
    x+= 400 #!UnboundLocalError: local variable 'x' referenced before assignment
    #x = 400 #posible y correcto pq estas creando una var local
    print('ahora x es ', x) #400


print('x =', x) #100
cambiando_x()
print('x =', x) #400

# 📖💡⭐La imposibilidad de modificar variables globales en ámbitos de d funciones, 
# NO ocurre en los bucles, porque estos NO crea un nuevo ámbito. 
# Estárias trabajando directamente en el ámbito global donde la variable fue definida
# ************************************************Codigo explicacion....******************************************

def saludar(nombre, apellido):
    print(f'hola, {nombre} tu apellido es {apellido}?')
    
#*ARGUMENTOS POSICIONALES Y POR PALABRA CLAVE EN FUNCIONES
# Cuando ""llamas""" a una función, puedes pasar los """argumentos""" de dos maneras:
# *1️⃣Argumentos posicionales: Se pasan en el mismo orden en que los PARÁMETRO están definidos.
saludar('Edily', 'Mora')
saludar('Mora', 'Edily') # ⚠️EL ORDEN ES IMPORTANTE

# *2️⃣Argumentos por palabra clave: Puedes especificar los argumentos usando los nombres de los PARÁMETRO, 
# te permite cambiar el orden.
saludar(apellido='Mora', nombre='Edily') 

# *3️⃣Valores por defecto: Puedes asignar un valor por defecto a un PARÁMETRO al definir la función. 
# Esto hace que ese parámetro sea opcional. Si el usuario no lo proporciona, se usará el valor por defecto. 
# ⚠️❌Los parámetros con valores por defecto siempre deben ir después de los parámetros sin valores por defecto, 
# de lo contrario generaras un Error ❌
def saludar_nombre_default(apellido, nombre='Usuaria'):
    print(f'hola, {nombre} tu apellido es {apellido}?')

saludar_nombre_default('Mora')
saludar_nombre_default('Mora', 'Rosa')
# ************************************************Codigo explicacion....******************************************
#*⛹🏽‍♂️⛹🏽‍♀️⛹🏽‍♂️⛹🏽‍♀️💡EJERCICIO #1:Funciones
# Crear un programa que verifique si una persona es mayor de edad. 
# Para ello, debes crear una función que reciba 
# la edad como parámetro y devuelva True si la persona 
# es mayor de edad o False si no lo es.

edad = int(input('Diga su edad'))
def eres_mayor(edad):
    return edad >= 18

print(eres_mayor(edad))
    


# #*⛹🏽‍♂️⛹🏽‍♀️⛹🏽‍♂️⛹🏽‍♀️💡EJERCICIO DESAFIO #2:Funciones
# Crea una función que calcule el precio final de un producto después de aplicar un descuento. 
# La función debe recibir de usuario con input(), el precio original, el porcentaje de descuento, 
# y si aplica el descuento (si/no), y devolver el precio final, lo que dependerá de si aplica o no 
# el descuento.
