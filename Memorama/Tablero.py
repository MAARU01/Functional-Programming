import typing
import randomizacion
from time import sleep
from Casilla import Casilla
import os
 
if os.name == "posix":
   var = "clear"       
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   var = "cls"

class Tablero:
    puntuacion:             int
    casilla_seleccionada1:   dict
    casilla_seleccionada2:   dict
    cursor:                  dict
    casillas:               list[list[typing.Any]]

    #Constructor
    def __init__(self): 
        self.puntuacion = 0
        self.casilla_seleccionada1 = {'x':-1,'y':-1}
        self.casilla_seleccionada2 = {'x':-1,'y':-1}
        self.casillas=[list(range(6)) for _ in range(6)]
        self.cursor = {'x':0,'y':0}


    def get_puntuacion(self) -> int:
        return self.puntuacion
    
    def get_casillas(self)-> list:
        return self.casillas
        
    def get_cursor(self)-> dict:
        return self.cursor

    # Metodos


    def crearTablero(self, tamanio_tablero: int)->None:
        conta = 0
        emojis = randomizacion.randomizarEmojis()
        for i in range(tamanio_tablero):
            for j in range(tamanio_tablero):
                casilla = Casilla()
                casilla.set_simbolo(emojis[conta])
                self.casillas[i][j] = casilla
                conta += 1

    def imprimirCasillas(self)->None:
        print(f"Puntuación actual: {self.puntuacion}")
        for i in range(len(self.casillas)):
            for j in range(len(self.casillas[0])):
                if self.casillas[i][j].get_es_visible() == True:
                    print (self.casillas[i][j].get_simbolo(),end="")
                elif (i == self.cursor['y'] and j == self.cursor['x']):
                    print('⏹️',end="")
                else:
                    
                    print('🛑',end="")
            print("")

    def cambiar_estado_casilla(self,coordenadas: dict)->None:
        self.casillas[coordenadas['x']][coordenadas['y']].cambiar_visibilidad()

    def comparacion_casillas (self, coordenadas_actuales : dict, coordenadas_anteriores: dict)-> None :
        if self.casillas[coordenadas_actuales['x']][coordenadas_actuales['y']].get_simbolo() == self.casillas[coordenadas_anteriores['x']][coordenadas_anteriores['y']].get_simbolo():
            self.puntuacion+=1
        else: 
            self.casillas[coordenadas_actuales['x']][coordenadas_actuales['y']].cambiar_visibilidad()
            self.casillas[coordenadas_anteriores['x']][coordenadas_anteriores['y']].cambiar_visibilidad()
        self.casilla_seleccionada1 = {'x':-1,'y':-1}
        self.casilla_seleccionada2 = {'x':-1,'y':-1}


    def rastrear_teclas(self,tecla:str)->None:
        coordenada_x = self.cursor['x']
        coordenada_y = self.cursor['y']
        if (tecla == "down" and self.cursor['y'] < 5):
            self.cursor['y'] += 1
        elif (tecla == "up" and self.cursor['y']>0):
            self.cursor['y'] -= 1
        elif (tecla == "right" and self.cursor['x'] < 5):
            self.cursor['x'] += 1
        elif (tecla == "left" and self.cursor['x'] > 0):
            self.cursor['x'] -= 1
        elif tecla == "enter" and self.casillas[coordenada_y][coordenada_x].get_es_visible() == False:
            #las coordenadas están invertidas
            self.casillas[coordenada_y][coordenada_x].cambiar_visibilidad()
            if self.casilla_seleccionada1['x'] == -1 and self.casilla_seleccionada1['y'] == -1:
                self.casilla_seleccionada1 = {'x': coordenada_y,'y':coordenada_x}
            else: 
                self.casilla_seleccionada2 = {'x': coordenada_y,'y':coordenada_x}
                os.system(var)
                self.imprimirCasillas()
                sleep(.5)
                self.comparacion_casillas(self.casilla_seleccionada1,self.casilla_seleccionada2)