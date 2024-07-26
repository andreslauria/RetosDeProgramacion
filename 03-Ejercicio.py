'''
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
'''


def ElegirOpcion():
    print("1) Buscar \n2) Agregar nuevo contacto\n3) Actualizar contacto\n4) Eliminar contacto\n5) O cualquier tecla para salir")
    opcion = input("Elige que operacion quieres realizar: ")
    return opcion


def buscar():
    nombre = input("Escriba el nombre del contacto: ").lower()
    return print(f"El telefono de {nombre} es:  {contactos.get(nombre, 'NO ESTA AGENDADO')}")


def agregar():
    nombre = input("Escriba el nombre del contacto a agregar: ").lower()
    telefono = input(f"Escriba el telefono de {nombre}: ")
    if telefono.isnumeric() and len(telefono) <= 11:
        contactos[nombre] = telefono
    else:
        print("Telefono mal ingresado")
        agregar()


def actualizar():
    nombre = input("Escriba el nombre del contacto a actualizar: ").lower()
    if nombre in contactos.keys():
        telefono = input(f"Escriba el nuevo telefono de {nombre}: ")
        if telefono.isnumeric() and len(telefono) <= 11:
            contactos[nombre] = telefono
        else:
            print("Telefono mal ingresado")
            actualizar()
    else:
        print("Ese nombre no esta agendado")
        ElegirOpcion()


def eliminar():
    nombre = input("Escriba el nombre del contacto a eliminar: ").lower()
    print(contactos.pop(nombre, "CONTACTO NO ENCONTRADO"))


contactos = {}

print("AGENDA DE CONTACTOS")

opcion = ElegirOpcion()

if opcion.isnumeric():
    while (opcion.isnumeric() and int(opcion) < 5):
        if opcion == "1":
            buscar()
            print("-------------------------------------------------------------")
        elif opcion == "2":
            agregar()
        elif opcion == "3":
            actualizar()
        elif opcion == "4":
            eliminar()

        opcion = ElegirOpcion()
else:
    print("Opcion mal ingresada, Adios!")
