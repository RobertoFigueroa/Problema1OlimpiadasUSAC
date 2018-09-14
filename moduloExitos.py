#modulo de exitos
def enHorizontal(matriz,caracter,linea):
    equisEnLinea = 0
    for j in range(4):
        if matriz[linea][j] == caracter or matriz[linea][j] == "T":
            equisEnLinea = equisEnLinea + 1    
    return equisEnLinea
def enVertical(matriz,caracter,columna):
    equisEnLinea = 0
    for j in range(4):
        if matriz[j][columna] == caracter or matriz[j][columna] == "T":
            equisEnLinea = equisEnLinea + 1
    return equisEnLinea
def enDiagonalL(matriz,caracter):
    equisEnLinea = 0
    for i in range(4):
        if matriz[i][i] == caracter or matriz[i][i]=="T":
            equisEnLinea = equisEnLinea + 1
    return equisEnLinea
def enDiagonalR(matriz,caracter):
    equisEnLinea = 0
    for i in range(4):
        for j in [3,2,1,0]:
            if matriz[i][j] == caracter or matriz[i][j]=="T":
                equisEnLinea = equisEnLinea + 1
    return equisEnLinea
def contarVacio(matriz):
    vecesRepetidas = matriz.count(".")
