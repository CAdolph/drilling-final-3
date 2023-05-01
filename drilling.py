famosos = [
    "Harry Houdini",
    "Newton",
    "David Blaine",
    "Hawking",
    "Messi",
    "Teller",
    "Einstein",
    "Pele",
    "Juanes"]


def hacer_grandioso(lista):
    lista_gran = []
    lista_cien = []
    lista_rest = []
    for nombre in lista:
        if nombre in ["Harry Houdini", "David Blaine", "Teller"]:
            lista_gran.append("El gran " + nombre)
        elif nombre in ["Newton", "Hawking", "Einstein"]:
            lista_cien.append(nombre)
        else:
            lista_rest.append(nombre)
    return lista_gran, lista_cien, lista_rest


def imprimir_nombres(lista):
    print("\nNombres Famosos: ")
    for nombre in lista:
        print(f"- {nombre}")
    print("\n")

    print("Magos: ")
    for x in hacer_grandioso(famosos)[0]:
        print(f"- {x}")
    print("Cientificos: ")
    for x in hacer_grandioso(famosos)[1]:
        print(f"- {x}")
    print("Resto: ")
    for x in hacer_grandioso(famosos)[2]:
        print(f"- {x}")


imprimir_nombres(famosos)
