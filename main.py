from juego import JuegoArchivo

if __name__ == "__main__":
    path_a_mapas = "mapas/"
    nombre = input("Ingresa tu nombre:")
    print(f"Hola, bienvenido {nombre}. Este es un juego de laberinto")
    
    juego = JuegoArchivo(path_a_mapas)
    juego.terminal()
    juego.inicializador()