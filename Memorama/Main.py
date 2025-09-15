import keyboard as kb
from time import sleep
from Tablero import Tablero
import os
 
if os.name == "posix":
   var = "clear"       
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   var = "cls"

def detectar_tecla() -> str: 
    tecla_str : str = ""
    while(True):
        if kb.is_pressed("up"):   
            tecla_str = "up"
            break

        elif kb.is_pressed("down"):
            tecla_str = "down"
            break

        elif kb.is_pressed("right"):
            tecla_str = "right"
            break

        elif kb.is_pressed("left"):
            tecla_str = "left"
            break
        elif kb.is_pressed("enter"):
            tecla_str = "enter"
            break
    return tecla_str

def main():
    #Instanciamos la clase Tablero
    tablero = Tablero()
    tablero.crearTablero(6)
    #Limpiamos la pantalla
    os.system(var)
    tablero.imprimirCasillas()
    print(f"Posición del cursor: {tablero.get_cursor()}")
    print("\n\nUsa las flechas para moverte en el tablero")
    print("Presiona enter para desbloquear una casilla")
    print("El juego termina al encontrar todos los pares de emojis:)")
        

    while(tablero.get_puntuacion() <= 17):
        sleep(.15)

        tablero.rastrear_teclas(detectar_tecla())
        os.system(var)
        tablero.imprimirCasillas()
        print(f"Posición del cursor: {tablero.get_cursor()}")
        print("\n\nUsa las flechas para moverte en el tablero")
        print("Presiona enter para desbloquear una casilla")
        print("El juego termina al encontrar todos los pares de emojis:)")

    os.system(var)    
    print("¡GANASTE! :D")
    sleep(3)
    exit()

if __name__ == "__main__":
    main()