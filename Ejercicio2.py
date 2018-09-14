#Roberto Figueroa
#|8306
#Programa solucion ejercicio 1 olimpiadas
#importamos el modulo que nos ayudara a leer y escribir en bloc de notas
from moduloIO import *
import random
from moduloExitos import *
casosT = int(input("Ingrese la cantiad de casos de prueba: "))
matriz = [[".",".",".","."],[".","T",".","."],[".",".",".","."],[".",".",".","."]]
print(matriz[1][1])
t = casosT
conta = 0
escribir = open("Salida01-X.txt","w")
while casosT != 0:
    conta = conta + 1
    ganar = False
    a = random.randint(1,16)
    while a < 16:
        fx=random.randint(0,3)
        cx=random.randint(0,3)
        fo=random.randint(0,3)
        co=random.randint(0,3)
        if matriz[fx][cx] != "T":
            matriz[fx].pop(cx)
            matriz[fx].insert(cx,"X")
        if matriz[fo][co] != "T":
            matriz[fo].pop(co)
            matriz[fo].insert(co,"O")
        a=a+1
    for i in range(4):
        print("")
        for j in range(4):
            print(end = matriz[i][j])
    for k in range(4):  
        if enHorizontal(matriz,"X",k) == 4:
           print("Caso"+str(conta)+":X gano")
           valor = "Caso"+str(conta)+":X gano"
           ganar = True
        elif enVertical(matriz,"X",k) == 4:
            print("Caso"+str(conta)+":X gano")
            valor = "Caso"+str(conta)+":X gano"
            ganar = True
        elif enHorizontal(matriz,"O",k) == 4:
            print("Caso"+str(conta)+":O gano")
            valor = "Caso"+str(conta)+":O gano" 
            ganar = True
        elif enVertical(matriz,"O",k) == 4:
            print("Caso"+str(conta)+":O gano")
            valor = "Caso"+str(conta)+":O gano"
            ganar = True
    if enDiagonalL(matriz,"X") == 4:
        print("Caso"+str(conta)+":X gano")
        valor = "Caso"+str(conta)+":X gano"
    elif enDiagonalR(matriz,"X") == 4:
        print("Caso"+str(conta)+":X gano")
        valor = "Caso"+str(conta)+":X gano"
    elif enDiagonalL(matriz,"O") == 4:
        print("Caso"+str(conta)+":O gano")
        valor = "Caso"+str(conta)+":O gano"
    elif enDiagonalR(matriz,"O") == 4:
        print("Caso"+str(conta)+":O gano")
        valor = "Caso"+str(conta)+":O gano"
    elif contarVacio == 0:
        print("Caso"+str(conta)+":Draw")
        valor = "Caso"+str(conta)+":Draw" 
    elif contarVacio != 0 and ganar != True:
        print("Caso"+str(conta)+":El juego no ha terminado")
        valor = "Caso"+str(conta)+":El juego no ha terminado"
    casosT -= 1
    escribir.write(valor)
    escribir.write("\n")
escribir.close()


