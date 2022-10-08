print ("""
        Programacón de Software 
        Ficha : 2502640
        Juan Pablo Torres Niño

""")

print("""1.Listas""")

print("""     1.1. list.append(x)
        Agrega un item siempre al final de una lista.""")
print(" ")

listJp1 = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
listJp = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

listJp.append('Manzana')
print(listJp)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")

print("""     1.2. list.extend(iterable)
        Extiende la lista en agregandole los items en el espacio iterable. """)
print(" ")

list1 = ('Pan','Vino')
listJp.extend(list1)
print(listJp)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")

print("""     1.3. list.insert(i.x)
        inserta un item en una posicion dada el primer item es para saber que colocar y el segun item en la posicion.""")
print(" ")

listJp.insert(0,'JTorres')
print(listJp)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")

print("""     1.4. list.remove(x)
        Quita el item donde su valor sea x.""")
print(" ")

listJp.remove('JTorres')
print(listJp)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")

print("""     1.5. list.pop([i])
        Quita el item en la posicion asignada, si este valor es un espacio vacio borrara el ultimo item de la lista.""")
print(" ")

listJp.pop(0)
print (listJp)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")

print("""     1.6. list.clear()
        Quita todos los elemtos de las listas.""")
print(" ")

listJp1.clear()
print (listJp1)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")

print("""     1.7. list.index(x[,start[,end]])
        Retorna el indice basado en cero del eemto cuyo valor sea x.""")
print(" ")

print(listJp.index('banana', 4))
print(listJp.index('banana'))

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")

print("""     1.8. list.count(x)
        Retorna las veces que le indique x.""")
print(" ")

Bn = listJp.count('Banana')
print(Bn)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")

print("""     1.9.  list.sort()
        Ordena los elementos de forma alfabeticamente.""")
print(" ")

listJp.sort()
print (listJp)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")

print("""     1.10. list.reverse()
        invierte los elemto de la lista.""")
print(" ")

listJp.reverse()
print (listJp)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")

print("""     1.11. list. copy()
        Retorna una copia de la lista de forma superficial.""")
print(" ")

list2 = listJp.copy()
print (list2)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("""2. Usando listas como pilas """)
print(" ")

list3 = [3, 4, 5]
list3.append(6)
list3.append(7)
print(list3)
list3.pop()
print(list3)
list3.pop()
print(list3)
list3.pop()
print(list3)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")

print("""3. usuando listas como cola
    Usar una lista como cola primero tienes que llamar la biblioteca "collections.deque" lo cual este fue diseñado para agregar y quitar de forma rapida.""")
print(" ")

from collections import deque
listJt = deque(["Eric", "John", "Michael"])
print(listJt)
listJt.append("Terry")
listJt.append("Graham")
print(listJt)
listJt.popleft() 
listJt.popleft() 
print(listJt)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")

print("""4. Compresion de listas
    las compresiones de listas ofrecen una manera de crear listas. de forma que su resultado sean operaciones implicadas en cada elemento.""")
print(" ")

cuadrado1 = []
for x in range(10):
    cuadrado1.append(x**2)
print(cuadrado1)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("     4.1 sobre escribe una varible que sigue existiendo en forma de bucle y no tendra ningun efecto en la lista anterior")
print(" ")

cuadrado1 = list(map(lambda x: x**2, range(10)))
print(cuadrado1)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")

print("     4.2.  O un equivalente")
print(" ")

cuadrado1 = [x**2 for x in range(10)]
print(cuadrado1)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")

print("     4.3.  Esta lista de compresion combina los elementos de dos listas si no son iguales")
print(" ")

tri = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(tri)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")

print("     4.4.  Si la expresion es una tupla, siempre debe estar entre parentesis.")
print(" ")

vec = [-4, -2, 0, 2, 4]
vec2 = [x*2 for x in vec]
print(vec2)

vec3 = [x for x in vec if x >= 0]
print(vec3)

vec4 = [abs(x) for x in vec]
print(vec4)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("""5. Compresiones anidadas""")
print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("   5.1. La expresion es una compresion de listas puede ser cualquier expresion arbitraria")
print(" ")

matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
]

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("   5.2.  Esta expresion transpondra las filas y columnas")
print(" ")

mtx1 = [[row[i] for row in matrix] for i in range(4)]
print(mtx1)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")

print("  5.3. La funcion zip() haria un buen trabajo para este caso de uso")
print(" ")

mtx2 = list(zip(*matrix))
print(mtx2)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")

print("""6. La instruccion "del"
        La instruccion del tambien puede usarse para quitar secciones de una lista o vaciar la lista completa """)
print(" ")

jp = [1, 2, 3, 15, 16, 5233]
del jp[0]
print (jp)

del jp[2:4]
print (jp)

del jp[:]
print (jp)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")

print("""  6.1.  Tambien se puede utilizar para eliminar varibles: del jp """)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("""7. tuplas y secuencias
        Como Python es un lenguaje en evolución, otros datos de tipo secuencia pueden agregarse. Existe otro dato de tipo secuencia estándar: la tupla.""")
print(" ")

tjp = 12345, 67891, 'hello!'
tjp [0]
print (tjp[0])

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("     7.1. Tupla anidada")
print(" ")

u = tjp, (1, 2, 3, 4, 5)
print (u)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("""#las tuplas son inmodificables

      7.2.  La tupla para observar cuantas variables hay en el""")
print(" ")

empty = ()
  
nombre = 'juan', 'pablo', 'torres',

print (len(empty))
print (len(nombre))

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("     7.3. para desempaquetado es una combinacion de empaquetado de tuplas de forma secuencial")
print(" ")

t = tjp, u 
print (t)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("""8. Conjuntos
        Una coleccion no ordenada y sn elementos repetidos.""")
print(" ")

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

conjunto = 'orange' in basket 
print(conjunto)
conjunto1 = 'crabgrass' in basket
print(conjunto1)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("""     8.1. demuestra una operacion unica entre 2 letras""")
print(" ")
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)
print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("""     8.2.Una forma similar a las compresiones de listas""")
print(" ")

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("""9. Diccionario
        Los diccionarios se encuentran a veces en otros lenguajes como «memorias asociativas» o «arreglos asociativos». A diferencia de las secuencias, que se indexan mediante un rango numérico, los diccionarios se indexan con claves, que pueden ser cualquier tipo inmutable; las cadenas y números siempre pueden ser claves. Las tuplas pueden usarse como claves si solamente contienen cadenas, números o tuplas; si una tupla contiene cualquier objeto mutable directa o indirectamente, no puede usarse como clave. No podés usar listas como claves, ya que las listas pueden modificarse usando asignación por índice, asignación por sección, o métodos como append() y extend().""")
print(" ")

jppt = {'sandra': 1234, 'salinas': 5678}
jppt['luigui'] = 9874
print(jppt)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("""     9.1. El constructor "dict()" crea un directamente desde secuencias de pares""")
jjp = dict ([('salinas', 5678), ('luigui', 9874), ('sandra', 1234)])
print(jjp)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("""     9.2.Ademas, las compresiones de diccionarios se pueden usar para crear diccionario desde expresiones arbitrarias de clave y valor""")
print(" ")

njp = {x: x**2 for x in (2, 4, 6)}
print (njp)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("""10. Tecnicas de iteración 
        Se pueden tener al mismo tiempo la clave y su valor correspondiente usando los siguientes metodos :""")
print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("""     10.1. .items""")
print(" ")

knights = {'El': 'agua', 'moja': ':D'}
for k, v in knights.items():
  print(k, v)
print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("""     10.2. enumerate()""")
print(" ")

for i, v in enumerate(['tic', 'tac', 'toe']):
  print(i, v)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("""     10.3. zip()""")
print(" ")

preguntas = ['name', 'quest', 'favorite color']
respuestas = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(preguntas, respuestas):
  print('What is your {0}?  It is {1}.'.format(q, a))

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("""     10.4. reversed()""")
print(" ")

for i in reversed(range(1, 10, 2)):
  print(i)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("""     10.5. sorted()""")
print(" ")

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

for i in sorted(basket):
  print(i)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("""     10.6. set()""")
print(" ")

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

for f in sorted(set(basket)):
  print(f)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("""# se pueden intercambiar una lista y es mas simple y seguro crear una lista""")
print(" ")

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
  if not math.isnan(value):
    filtered_data.append(value)
    
print(filtered_data)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("""11. mas acerca de condiciones 
        Las condiciones usadas en las instrucciones while e if pueden contener cualquier operador, no sólo comparaciones.

        The comparison operators in and not in are membership tests that determine whether a value is in (or not in) a container. The operators is and is not compare whether two objects are really the same object. All comparison operators have the same priority, which is lower than that of all numerical operators.

        Las comparaciones pueden encadenarse. Por ejemplo, a < b == c verifica si a es menor que b y además si b es igual a c.

        Las comparaciones pueden combinarse mediante los operadores booleanos and y or, y el resultado de una comparación (o de cualquier otra expresión booleana) puede negarse con not. Estos tienen prioridades menores que los operadores de comparación; entre ellos not tiene la mayor prioridad y or la menor, o sea que A and not B or C equivale a (A and (not B)) or C. Como siempre, los paréntesis pueden usarse para expresar la composición deseada.""")
print(" ")

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)

print(" ")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("""12. Comparando secuencias y otros tipos.
        Las secuencias pueden compararse con otros objetos del mismo tipo de secuencia. La comparación usa orden lexicográfico: primero se comparan los dos primeros ítems, si son diferentes esto ya determina el resultado de la comparación; si son iguales, se comparan los siguientes dos ítems, y así sucesivamente hasta llegar al final de alguna de las secuencias. Si dos ítems a comparar son ambos secuencias del mismo tipo, la comparación lexicográfica es recursiva. Si todos los ítems de dos secuencias resultan iguales, se considera que las secuencias son iguales. Si una secuencia es la parte inicial de la otra, la secuencia más corta es la más pequeña. El orden lexicográfico de los strings utiliza el punto de código Unicode para ordenar caracteres individuales. Algunos ejemplos de comparación entre secuencias del mismo tipo:""")