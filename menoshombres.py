# Aquí inicia el flujo del programa


def menosHombres():
    """
*********************************************************************
		Instituto Tecnológico de Costa Rica
Ingeniería en Computadores
Curso: Introduccion a la Programación
Profesor: Milton Villegas Lemus
Programa: Encuentra el cantón o país con menos hombres registrados diferente de cero
Lenguaje: Python 3.6.2
Autores: Stephanie Canales Cerdas - 2018235725
         Victoria Ruíz Vargas - 2017097147
Versión: 2.0.0
Fecha Última Modificación: 11/11/2018
Entradas: Una provincia o "Extranjero"
Salidas: Cantón o país con menos hombres registrados diferente de cero
Restricciones: Debe ingresar el nombre de la provincia escrito correctamente o "Extranjero"
II Parte, II Parcial
 
*********************************************************************** """
    
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
        return menosHombres()
    return sortHombres(newarch, arch)

# Aquí crea la lista de los países o cantones de manera desordenada

def sortHombres(newarch, arch):
    with open(newarch) as file:
        lines_after_16 = file.readlines()[16:]
        return sortHombres_aux(lines_after_16, [], 1, arch)

# Aquí le hace .split() a la lista(quita espacios)

def sortHombres_aux(lista, nuevaLista, indice, arch):
    if indice == len(lista):
        return crearLista(nuevaLista, [], 0, 0, arch)
    if indice+2>len(lista):
        return crearLista(nuevaLista,[],0,0,arch)
    else:
        return sortHombres_aux(lista, nuevaLista + [lista[indice].split()],indice+2, arch)

# Aquí crea la lista con la cantidad de hombres en cada cantón o país

def crearLista(lista, nuevaLista, i, j, arch):
    if i == len(lista):
        return crearLista_aux(nuevaLista, [], 0, arch)
    else:
        if lista[i][0][0].isalpha():
            j = 2
        if lista[i][1][0].isalpha():
            j = 3
        if lista[i][2][0].isalpha():
            j = 4
        dato = [lista[i][0],lista[i][j]]
        return crearLista(lista, nuevaLista + [dato], i+1, 0, arch)

# Los transforma en enteros para ordenarlos

def crearLista_aux(lista, nuevaLista, indice, arch):
    if indice == len(lista):
        return insertionsort(nuevaLista, lista, arch)
    else:
        return crearLista_aux(lista, nuevaLista + [int(lista[indice][1])], indice+1, arch)
        
# Ordena la lista usando el método insertion sort

def insertionsort(lista, viejaLista, arch):
    return insertionsort_aux(lista,1,len(lista), viejaLista, arch)

def insertionsort_aux(lista,i,n, viejaLista, arch):
    if i == n:
        return verifica(str(lista[0]), viejaLista, 0, arch)
    Aux = lista[i]
    j = incluye_orden(lista,i,Aux)
    lista[j] =  Aux
    return insertionsort_aux(lista,i+1,n, viejaLista, arch)

def incluye_orden(lista,j,Aux):
    if j <= 0 or lista[j-1] <= Aux:
        return j
    lista[j] = lista[j-1]
    return incluye_orden(lista,j-1,Aux)

# Verifica a que cantón o país corresponde el dato y lo imprime en pantalla

def verifica(men, viejaLista, indice, arch):
    if arch == "Extranjero":
            return especial(men, viejaLista, indice, arch, "")
    elif men == viejaLista[indice][1]:
        if arch == "Alajuela":
            return "República de Costa Rica, 07-09-2018, " + arch + ", " + viejaLista[indice][0] + " MATE0, "+ men
        if arch =="Heredia":
            return "República de Costa Rica, 07-09-2018, " + arch + ", " + viejaLista[indice][0] + " ISIDRO, "+ men
        else:
            return "República de Costa Rica, 07-09-2018, " + arch + ", " + viejaLista[indice][0] + ", "+ men
    else:
        return verifica(men, viejaLista, indice+1, arch)

# El caso especial de Extranjero diferente de cero

def especial(men,viejaLista,indice,arch, result):
    if indice == len(viejaLista):
        return "República de Costa Rica, 07-09-2018, " + arch + ", " + result + '1'
    if viejaLista[indice][1] == '1':
        if viejaLista[indice][0] == "TRINIDAD":
            return especial(men, viejaLista, indice+1, arch, result + viejaLista[indice][0] + " Y TOBAGO, ")
        else:
            return especial(men, viejaLista, indice+1, arch, result + viejaLista[indice][0] + ", ")
    else:
        return especial(men, viejaLista, indice+1, arch, result)



