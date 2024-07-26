'''ESTRUCTURA DE DATOS'''

'''
LISTAS - conjunto de datos mutable, ordenado
'''

# comprension de listas -  manera concisa de crear una lista
cuadrados = [x**2 for x in range(10)]
print(cuadrados)

lista_vacia = []
frutas = ['manzana', 'naranja', 'pera', 'banana']

print(frutas[0])  # accede e imprime el primer elemento

frutas.append('tomate')  # Agrego un elemento al final de la lista
frutas.insert(0, 'mandarina')  # Agrego un elemento en el indice indicado
print(frutas)
frutas.remove('naranja')  # Elimina la primera aparicion del elemento pasado.
frutas.pop()  # elimina el ultimo, tambien devuelve el string del elemento que fue eliminado pasando un indice
print(frutas.pop(2))
# Agrega, extiende la lista adheriendo la nueva lista al final
frutas.extend(['manzana', 'pera', 'sandia', 'melon',])
print(frutas)
# Imprime el primer indice donde aparece el elemento
print(f"index 'manzana': {frutas.index('manzana')}")
# cuenta la cantidad de veces que aparece un elemento
print(f"count 'manzana': {frutas.count('manzana')}")

# * ORDENAMIENTOS DE LISTAS
numeros = [1, 10, 25, 35, 0, 2, 15]

numeros.sort()  # ordena de menor a mayor, de A a la Z
print(numeros)
numeros.reverse()  # ordena de forma inversa
print(numeros)

'''
SETS - Conjuntos - Similar a la listas 
'''
# Sus elementos son unicos e inmutables (por ejemplo un elemento del conjunto no puede ser una lista)
# Los Conjuntos son desordenados

conjunto = {0, 1, 2, 3}
conjunto2 = {3, 4, 5}
print(len(conjunto))  # puedo saber el tamanio del conjunto
print(2 in conjunto)  # puedo verificar si el elemento esta en el conjunto
# operador union -- SOLO APARECEN LOS ELEMENTOS QUE NO SE REPITEN
print(conjunto | conjunto2)
print(conjunto.intersection(conjunto2))

# * Metodos
conjunto.add(10)
# elimina el elemento que se pasa, si no existe tira error KEYERROR
conjunto.remove(3)
# para salvar el error anterior se utilza
conjunto.discard(0)
# Elimino un elemento aleatorio
conjunto.pop()
# ELIMINO TODOS LOS ELEMENTOS
conjunto2.clear()

'''
TUPLAS
'''
# Son Inmutables,son indexadas como las listas

tupla = (1, 2, 3, 4)
dias_semana = 'lunes', 'martes', 'miercoles', 'jueves', 'viernes', (
    'sabado', 'domingo')
print(dias_semana)
print(dias_semana.count('lunes'))
print(dias_semana.index('lunes'))

print(dias_semana[0])
print(dias_semana[5][1])  # Tuplas anidadadas
conjunto_tupla = tuple(conjunto)  # convertir lista en tupla
print(conjunto_tupla)

# *Iterar una tupla
for n in tupla:
    print(n)
# *asignar el valor de una tupla a variables
w, x, y, z = tupla
print(w, x, y, z)

'''DICCIONARIOS'''
# Contenedor NO organizado y mutable que almacena pares CLAVE-VALOR
diccionario = {
    "Nombre": "Sara",
    "Edad": 27,
    "Documento": 1003882
}
diccionario2 = {
    "Direccion": "Av 39 700",
    "C.P": "7600"
}
print(diccionario)

# *Acceder a sus elementos
print(diccionario['Nombre'])
# *Modificar un elemento
diccionario['Nombre'] = 'Andres'
print(diccionario)
# *Si agregamos una CLAVE que no existe, se agrega automaticamente al diccionario
diccionario['Direccion'] = 'jose alonso 123'
print(diccionario)
# *Iterar un diccionario
# por clave
for clave in diccionario:
    print(clave)
# por valor
for clave in diccionario:
    print(diccionario[clave])
# Imprime los key y value del diccionario
for clave, valor in diccionario.items():
    print(clave, valor)

# METODOS
diccionario.items()  # devuelve una lista de claves y valores
diccionario.keys()  # devuelve una lista con todas las claves
diccionario.values()  # devuelve una lista con todos los valores
# elimina la clave que se pasa y devuelve el valor asociado, sino existe esa clave entrega el valor por defecto
print(diccionario.pop('calle', "no existe esa clave"))

#* UPDATE() se llama sobre un diccionario, actualiza los valores de las KEYS que se repiten y si alguna KEY es nueva se AGREGA.
diccionario.update(diccionario2)
print(diccionario)

