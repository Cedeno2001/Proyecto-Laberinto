import readchar
from readchar import key
import os
nombre = input("Ingresa tu nombre:")
print(f"Hola, bienvenido {nombre}. Este es un juego de laberinto")

def borrarterminal():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    numero = 0
    while numero <= 50:
        borrarterminal()
        print(f"haz presionado {numero}:")
        
        tecla = readchar.readkey()
        
        if tecla == "n":
            numero += 1
            if numero == 50:
                borrarterminal()
                print("llegaste a 50. Lo lograste!!") 
                break   
    
    
if __name__ == "__main__": 
    main()

   
      
