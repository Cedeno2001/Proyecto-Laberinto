import readchar
from readchar import key
nombre = input("Ingresa tu nombre:")
print(f"Hola, bienvenido {nombre}. Este es un juego de laberinto")

def main():
    print("entraste en un bucle, para salir tiene que presionar la tecla UP")
    while True:
        teclas = readchar.readkey()
        print(f"tecla seleccionada:{teclas}")
        if teclas == key.UP:
            break
    print("Felicidades, lograste salir del bucle!!") 
    
    
if __name__ == "__main__": 
    main()      
