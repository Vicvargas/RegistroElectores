# Aquí inicia el flujo del programa


def promedio():
    """
*********************************************************************

                            Instituto Tecnológico de Costa Rica
Ingeniería en Computadores
Curso: Introducción a la programación
Profesor: Milton Villegas Lemus
Programa: Calcula el promedio de habitantes del archivo ingresado por el user
Python 3.6.2
Autora: Victoria Ruíz Vargas - 2017097147
Versión: 1.0.0
Fecha de última modificación: 11/11/2018
Entradas: Una provincia o "Extranjero"
Salidas:  Promedio de habitantes para la provincia o el extranjero
Restricciones: Debe ingresar el nombre de la provincia escrito correctamente o "Extranjero"

II Parte, II Parcial

********************************************************************* """
    arch = input("Ingrese la provincia para ver el registro correspondiente \n o 'Extranjero' si desea ver los votos en el extranjero: ")
    return definiendoLugar(arch)

# Aquí recibe el input del user

def definiendoLugar(arch):
    newarch = ""
    if(arch == "Guanacaste"):
        newarch = r"C:\Users\PC\Desktop\Archivosordenados\GUAArchivo7.txt"
    elif(arch == "San José"):
        newarch = r"C:\Users\PC\Desktop\Archivosordenados\SJOArchivo1.txt"
    elif(arch == "Cartago"):
        newarch = r"C:\Users\PC\Desktop\Archivosordenados\CARArchivo3.txt"
    elif(arch == "Heredia"):
        newarch = r"C:\Users\PC\Desktop\Archivosordenados\HERArchivo4.txt"
    elif(arch == "Limón"):
        newarch = r"C:\Users\PC\Desktop\Archivosordenados\LIMArchivo6.txt"
    elif(arch == "Puntarenas"):
        newarch = r"C:\Users\PC\Desktop\Archivosordenados\PUNArchivo5.txt"
    elif(arch == "Alajuela"):
        newarch = r"C:\Users\PC\Desktop\Archivosordenados\ALAArchivo2.txt"
    elif(arch == "Extranjero"):
        newarch = r"C:\Users\PC\Desktop\Archivosordenados\EXTArchivo8.txt"
    else:
        print("\n \nEntrada inválida, inténtelo de nuevo. \n \n")
        return promedio()
    return sortPromedio(newarch, arch)

# Aquí crea la lista de los países o cantones de manera desordenada

def sortPromedio(newarch, arch):
    with open(newarch) as file:
        lines_after_16 = file.readlines()[16:]
        return sortPromedio_aux(lines_after_16, [], 1, arch)

# Aquí le hace .split() a la lista (quita espacios)

def sortPromedio_aux(lista, nuevaLista, indice, arch):
    if indice == len(lista):
        return crearLista(nuevaLista, [], 0, 0, arch)
    if indice+2>len(lista):
        return crearLista(nuevaLista, [], 0, 0, arch)
    else:
        return sortPromedio_aux(lista, nuevaLista + [lista[indice].split()],indice+2, arch)

# Aquí crea la lista con la cantidad de mujeres en cada cantón o país

def crearLista(lista, nuevaLista, i, j, arch):
    if i == len(lista):
        return crearLista_aux(nuevaLista, [], 0, arch)
    else:
        if lista[i][0][0].isalpha():
            j = 1
        if lista[i][1][0].isalpha():
            j = 2
        if lista[i][2][0].isalpha():
            j = 3
        dato = [lista[i][0],lista[i][j]]
        return crearLista(lista, nuevaLista + [dato], i+1, 0, arch)
    
def crearLista_aux(lista, nuevaLista, indice, arch):
    if indice == len(lista):
        return suma(nuevaLista, 0,0,arch)
    else:
        return crearLista_aux(lista, nuevaLista + [int(lista[indice][1])], indice+1, arch)    

def promediar(promedio,lugar):
    if lugar == "Extranjero":
        return "El promedio de habitantes en el extranjero es " + str(int(promedio))
    else:
        return "El promedio de habitantes para "+ lugar + " es " + str(int(promedio))

# Calcula el promedio de los habitantes

def suma(lista,i,result,lugar): 
    if i == len(lista):
        return promediar(result/len(lista),lugar)
    else:
        return suma(lista,i+1,result +lista[i],lugar) 
