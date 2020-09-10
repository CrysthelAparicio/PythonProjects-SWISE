#Imports

import random
import os
import time

#colores definidos
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"

WIDTH = 10
HEIGHT = 20

def clear_screen():
    os.system("cls")

class Square:
    def __init__(self,col):
        self.col = col
    def __str__(self):
        return self.col + "#"

class EmptySquare:
    def __str__(self):
        return " "

class Forma:
    def _init__(self, ij = [(-1,-1),(0,-1),(1,-1)], col = PURPLE, x=WIDTH//2, y=HEIGHT-2):
        self.x = x
        self.y = y
        self.ij = ij
        self.col = col
    def place(self):
        camplace = True
        for a in self.ij+[(0,0)]:
            x = self.x+a[1] #movimiento a la derecha
            y = self.y-a[0] #movimiento a la izq
        print(x,y)
        if type(grid[y][x]) != EmptySquare: #Si la posición esta ocupado
            camplace = False
        if camplace:
            self.showgrid()
        return camplace

    # Muestre el escenario
    def showgrid(self):
        grid[self.y][self.x] = Square(self.col)
        for a in self.ij:
            try: 
                grid[self.y+a[1]][self.x+a[0]] = Square(self.col)
            except IndexError: #tratando de mostrar una pieza que no está en pantalla
                pass
    
    # borra degradadamente
    def removeFromgrid(self):
        grid[self.y][self.x] = Square(self.col)
        for a in self.ij:
            try: 
                grid[self.y+a[1]][self.x+a[0]] = EmptySquare()
            except IndexError: #tratando de mostrar una pieza que no está en pantalla
                pass

    def move(self):
        safe = True
        self.removeFromgrid #eliminar si pierde el juego
        for rpos in self.ij+[0,0]:
            x = self.x+rpos[0]
            y = self.y+rpos[1] - 1 #resto -1 para que sea la nueva pos
            if not type(grid[y][x]) == EmptySquare: #No se va a poder mover
                safe = False
            if y < 0:
                safe = False
            if safe: #se pueda mover bajando en 1
                self.y -= 1 #igualar los espacios
                self.showgrid()
            else: #vamos a consolidar a la cuadricula como cuadrados
                for rpos in self.ij+[(0.0)]:
                    x = self.x+rpos[0]
                    y = self.y+rpos[1]
                    grid[y][x] = Square(self.col)
            return safe #ya la figura se puede mover libremente

    #def rotate: 