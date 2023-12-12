import readchar
import os
import random
from functools import reduce
class Juego:
    def __init__(self, path_a_mapas):
        self.path_a_mapas = path_a_mapas
        self.mapa = self.cargar_mapas_random()
        self.matriz_del_laberinto = self.cadena_de_matrices(self.mapa)
        self.posicion_inicio, self.posicion_fin = self.encontrar_posiciones_inicio_y_fin(self.matriz_del_laberinto)
        self.px, self.py = self.posicion_inicio
  
    def cargar_mapas_random(self):
        archivos_de_los_mapas = os.listdir(self.path_a_mapas)
        file = random.choice(archivos_de_los_mapas)
        paquete_completo = os.path.join(self.path_a_mapas, file)
        with open(paquete_completo, "r") as archivos_de_los_mapas:
            return archivos_de_los_mapas.read().strip()

    def cadena_de_matrices(self, cadena_de_los_laberintos):
        return list(map(list, cadena_de_los_laberintos.strip().split("\n")))


    def encontrar_posiciones_inicio_y_fin(self, matriz_del_laberinto):
        for i in range(len(matriz_del_laberinto)):
            for u in range(len(matriz_del_laberinto[i])):
                if matriz_del_laberinto[i][u] == "P":
                    posicion_inicio = (i, u)
                elif matriz_del_laberinto[i][u] == ".":
                    posicion_final = (i, u)
        return posicion_inicio, posicion_final
    
    def inicializador(self):
        while (self.px, self.py) != self.posicion_fin:
            self.terminal()
            for fila in self.matriz_del_laberinto:
                print("".join(fila))
            tecla = readchar.readkey()
            if tecla == readchar.key.UP:
                nueva_px, nueva_py = self.px - 1, self.py
            elif tecla == readchar.key.DOWN:
                nueva_px, nueva_py = self.px + 1, self.py
            elif tecla == readchar.key.LEFT:
                nueva_px, nueva_py = self.px, self.py - 1
            elif tecla == readchar.key.RIGHT:
                nueva_px, nueva_py = self.px, self.py + 1
            else:
                continue
            if (
                0 <= nueva_px < len(self.matriz_del_laberinto)
                and 0 <= nueva_py < len(self.matriz_del_laberinto[0])
                and self.matriz_del_laberinto[nueva_px][nueva_py] != "#"
            ):
                self.matriz_del_laberinto[self.px][self.py] = "."
                self.px, self.py = nueva_px, nueva_py
                self.matriz_del_laberinto[self.px][self.py] = "P"
        self.terminal()
        for fila in self.matriz_del_laberinto:
            print("".join(fila))
        print("Excelente, finalizaste el laberinto!")
    def terminal(self):
        os.system("cls" if os.name == "nt" else "clear")

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        super().__init__(path_a_mapas)
    
    def file_map_read(self, file):
        with open(file, "r") as archivos_de_los_mapas:
           lines = archivos_de_los_mapas.readlines()
        coordinates = lines[0].strip().split()
        row_map = reduce(lambda x, y: x + y, lines[1:])
        return coordinates, row_map.strip()
            