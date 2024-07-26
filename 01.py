from random import randint

num1 = randint(1, 10)
num2 = randint(1, 10)

print(f"Suma: {num1} + {num2} = {num1 + num2}")
print(f"Resta: {num1} - {num2} = {num1 - num2}")
print(f"Multiplicacion: {num1} * {num2} = {num1 * num2}")
print(f"Division: {num1} / {num2} = {num1 / num2}")
print(f"Division Entera: {num1} // {num2} = {num1 // num2}")
print(f"Modulo (Resto): {num1} % {num2} = {num1 % num2}")
print(f"Potencia: {num1} ** {num2} = {num1 ** num2}")
print(f"Suma: {num1} + {num2} = {num1 + num2}")

# operadores logicos y de comparacion

# and
print("40 > 10 and hola == Hola.lower() --> True and True --> True")
# Imprime True, ya que las dos condiciones son verdaderas
print(40 > 10 and "hola" == "Hola".lower())

# or
print("30 - 20 == 10 or 30 - 20 == 100 --> True or False --> True")
# Imprime True, si una de las condiciones son verdaderas
print(30 - 20 == 10 or 30 - 20 == 100)

# not
print("not 10 == 10 --> not (True) --> False")
# Imprime False, ya que la condicion es True y el operador NOT invierte
print(not 10 == 10)


# > (Mayor que)
print(f"{num1} > {num2} : {num1 > num2}")
# < (Menor que)
print(f"{num1} < {num2} : {num1 < num2}")
# == (Igual que)
print(f"{num1} = {num2} : {num1 == num2}")
# >= (Mayor o Igual que)
print(f"{num1} >= {num2} : {num1 >= num2}")
# <= (Menor o Igual que)
print(f"{num1} <= {num2} : {num1 <= num2}")
# != (No Igual que)
print(f"{num1} != {num2} : {num1 != num2}")


# Operadores de identidad
a = 3
b = 3
c = 4
print(f'3 is 3 -> {a is b}')
print(f'4 is not 3 -> {c is not b}')

# Operadores de pertenencia
a = [1, 2, 3, 4, 5]
print(f'1 in a -> {1 in a}')
print(f'7 not in a -> {7 not in a}')

# Estructuras de control condicionales iterativas, excepciones
name = 'Abel'
apellido = 'Perez'

# Condicionales
if name is not apellido:
    print('Sentencia IF')
if name is apellido:
    pass
elif 'a' in apellido:
    print('Sentencia elif')
else:
    print('Sentencia else')

# Iteraciones
for l in name:
    print(l)

n = 0
while n <= 4:
    print(n)
    n += 1

# Excepciones
a = 1
b = 2
try:
    print(len(a))
except Exception as err:
    print(err)

# Extra: Programa que imprima por consola todos los numeros comprendidos entre 10 y 55 incluidos
#        pares y que no son ni el 16 ni multiplos de 3
for n in range(10, 56):
    if not n % 3 == 0 and n != 16 and n % 2 == 0:
        print(n)
