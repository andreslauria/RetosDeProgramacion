# Declarando Funciones

# Sin Parametros ni Retorno
def Saludar():
    print("Hola!")

# Sin Parametros con Retorno


def Despedir():
    varLocal = "VariableLocar"
    return (f"Adios y {varLocal}")

# Con Parametros Sin Retorno


def AreaCuadrado(lado):
    print(f"Area del cuadrado es: {lado * lado}")

# Con Parametros y retorno


def Sumar(n1, n2):
    return n1 + n2

# Utilizando las funciones


Saludar()

lado = 2
AreaCuadrado(lado)

suma = Sumar(1, 12)
print(f"La suma es: {suma}")

despedida = Despedir()
print(despedida)


# variables global
str1 = "fizz"
str2 = "buzz"


def intercambio(str1, str2):
    # Variable Local
    cont = 0
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print(f"{str1} {str2}")
        elif num % 3 == 0:
            print(str1)
        elif num % 5 == 0:
            print(str2)
        else:
            cont += 1
    return cont


print(intercambio(str1, str2))
