import readchar
from readchar import key
import os

def borrarterminal():
    os.system('cls' if os.name=='nt' else 'clear')

def cadena_de_matrices(cadena_laberinto):
    filas_del_laberinto = cadena_laberinto.strip().split("\n")
    matriz_del_laberinto = [list(fila)for fila in filas_del_laberinto]
    return matriz_del_laberinto

def encontrarposicionfinal_inicio(matriz_del_laberinto):
    for i in range(len(matriz_del_laberinto)):
        for u in range(len(matriz_del_laberinto[i])):
            if matriz_del_laberinto[i][u] == "P": 
                posicion_inicial = (i, u)
            elif matriz_del_laberinto[i][u] == ".":
                posicion_final = (i, u)
    return posicion_inicial, posicion_final

def inicializador(mapa):
    matriz_del_laberinto = cadena_de_matrices (mapa)
    posicion_inicial, posicion_final = encontrarposicionfinal_inicio(matriz_del_laberinto)
    px, py = posicion_inicial
    
    while (px, py) != posicion_final:
        borrarterminal()
        for fila in matriz_del_laberinto: 
            print("".join(fila))
        
        tecla = readchar.readkey()
        if tecla == key.UP:
            nueva_px, nueva_py = px - 1, py
        elif tecla == key.DOWN:
            nueva_px, nueva_py = px + 1, py
        elif tecla == key.LEFT:
            nueva_px, nueva_py = px, py - 1
        elif tecla == key.RIGHT:
            nueva_px, nueva_py = px, py + 1
        else:
            continue
        
        if (
            0 <= nueva_px < len(matriz_del_laberinto)
            and 0 <= nueva_py < len(matriz_del_laberinto[0])
            and matriz_del_laberinto[nueva_px][nueva_py] != "#"
        ):
            matriz_del_laberinto[px][py] = "."
            px, py = nueva_px, nueva_py
            matriz_del_laberinto[px][py] = "P"

    borrarterminal()
    for fila in matriz_del_laberinto:
        print("".join(fila))
        
    print("Excelente, finalizaste el laberinto")
                    
    
if __name__ == "__main__": 
    borrarterminal()
    nombre = input("Ingresa tu nombre:")
    print(f"Hola, bienvenido {nombre}. Este es un juego de laberinto")
    
    mapa = """
##########
#P.......#
#.##..####
#...#.#..#
###.#.###.
#.....#..#
#.###.#..#
#...#....#
########.#
"""
    inicializador(mapa)
