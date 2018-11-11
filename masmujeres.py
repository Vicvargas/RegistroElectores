#Aquí inicia el flujo del programa


def masMujeres():
    """
*********************************************************************

                            Instituto Tecnológico de Costa Rica
Ingeniería en Computadores
Curso: Introducción a la programación
Profesor: Milton Villegas Lemus
Programa: Encuentra el cantón (o país) con más mujeres registradas de la provincia (o "Extranjero") ingresada por el user
Python 3.6.2
Autora: Victoria Ruíz Vargas - 2017097147
Versión: 1.0.0
Fecha de última modificación: 11/11/2018
Entradas: Una provincia o "Extranjero"
Salidas: Cantón o país con más mujeres registradas
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
        return masMujeres()
    return sortMujeres(newarch, arch)

# Aquí crea la lista de los países o cantones de manera desordenada

def sortMujeres(newarch, arch):
    with open(newarch) as file:
        lines_after_16 = file.readlines()[16:]
        return sortMujeres_aux(lines_after_16, [], 1, arch)

# Aquí le hace .split() a la lista (quita espacios)
    
def sortMujeres_aux(lista, nuevaLista, indice, arch):
    if indice == len(lista):
        return crearLista(nuevaLista, [], 0, 0, arch)
    if indice+2>len(lista):
        return crearLista(nuevaLista, [], 0, 0, arch)
    else:
        return sortMujeres_aux(lista, nuevaLista + [lista[indice].split()],indice+2, arch)

# Aquí crea la lista con la cantidad de mujeres en cada cantón o país
    
def crearLista(lista, nuevaLista, i, j, arch):
    if i == len(lista):
        return crearLista_aux(nuevaLista, [], 0, arch)
    else:
        if lista[i][0][0].isalpha():
            j = 3
        if lista[i][1][0].isalpha():
            j = 4
        if lista[i][2][0].isalpha():
            j = 5
        dato = [lista[i][0],lista[i][j]]
        return crearLista(lista, nuevaLista + [dato], i+1, 0, arch)

# Los transforma en enteros para ordenarlos
    
def crearLista_aux(lista, nuevaLista, indice, arch):
    if indice == len(lista):
        return insertionsort(nuevaLista, lista, arch)
    else:
        return crearLista_aux(lista, nuevaLista + [int(lista[indice][1])], indice+1, arch)
        
# Ordena la lista con el método insertion sort

def insertionsort(lista, viejaLista, arch):
    return insertionsort_aux(lista,1,len(lista), viejaLista, arch)

def insertionsort_aux(lista,i,n, viejaLista, arch):
    if i == n:
        return verifica(str(lista[-1]), viejaLista, 0, arch)
    Aux = lista[i]
    j = incluye_orden(lista,i,Aux)
    lista[j] =  Aux
    return insertionsort_aux(lista,i+1,n, viejaLista, arch)

def incluye_orden(lista,j,Aux):
    if j <= 0 or lista[j-1] <= Aux:
        return j
    lista[j] = lista[j-1]
    return incluye_orden(lista,j-1,Aux)

# Verifica a qué cantón o país corresponde el dato y lo imprime en pantalla

def verifica(may, viejaLista, indice, arch):
    if may in viejaLista[indice][1]:
        if viejaLista[indice][0] == "ESTADOS":
            return "República de Costa Rica, 07-09-2018, " + arch + ", " + viejaLista[indice][0] + " UNIDOS, "+ may
        else:
            return "República de Costa Rica, 07-09-2018, " + arch + ", " + viejaLista[indice][0] + ", "+ may
    else:
        return verifica(may, viejaLista, indice+1, arch)
