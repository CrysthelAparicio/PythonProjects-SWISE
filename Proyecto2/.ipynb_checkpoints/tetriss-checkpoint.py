"""
- Al menos un ente que se pueda sin ambigüedad llamar protagonista (LISTO)
- Definiendo un estado como la colección de variables en memoria 
necesarios para describir todos los entes del juego, 
se requiere que se tenga un número de estados no idénticos 
totales mayor que 2 en los el protagonista no puede tener 
los mismos valores en todos. Es decir, el protagonista 
debe evolucionar en los estados. (LISTO! Felipe menciono que con que mostrará perdedor ya que es tetris, suficiente y aqui nunca se gana.)
- Debe existir un objetivo claro a alcanzar, 
definido en términos de los valores de un número 
de variables que debe incluir las que definen al protagonista. 
Además, se necesita un estado de pérdida que termine 
el juego si se alcanza. (LISTO!)
- Se debe utilizar programación orientada a objetos, pues es la técnica centro de este módulo.  (LISTO)
- Al menos tres clases distintas, cada una con una responsabilidad distinta y clara. 
Además, deben contener al menos un método diferente de 
los métodos dunder, ej. __init__ (LISTO)
- Al menos una clase que herede de otra clase y adicione dos métodos 
distinto sobre los de su clase padre. OJO...(DOUGLAS, OSCAR Y ADRIANA)...OJO
- Al menos un caso de sobrecarga de operadores. (OSCAR, ADRIANA Y OSCAR) 
""" 
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
YELLOW2 = "\033[1;33m"
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

class Cuadrado:
    def __init__(self,col):
        self.col = col
    def __str__(self):
        return self.col + "x"

class EmptySquare:
    def __str__(self):
        return " "

class Forma:
    def __init__(self, ij = [(-1,-1),(0,-1),(1,-1)], col = PURPLE, x=WIDTH//2, y=HEIGHT-2):
        self.x = x 
        self.y = y
        self.ij=ij
        self.col = col
    def place(self):
        camplace = True
        for a in self.ij+[(0,0)]:
            x = self.x+a[1] #movimiento a la derecha
            y = self.y-a[0] #movimiento a la izq
            print(x, y)
            if type(cuadricula[y][x]) != EmptySquare: #Si la posición esta ocupada
                camplace = False
        if camplace:
            self.showgrid()
        return camplace

    #Mueste el escenario
    def showgrid(self):
        cuadricula[self.y][self.x] = Cuadrado(self.col)
        for a in self.ij:
            try:
                cuadricula[self.y+a[1]][self.x+a[0]] = Cuadrado(self.col)
            except IndexError:#tratando de mostrar una pieza que no está en pantalla
                pass

    #borra (no pude hacer que borrara degradadamente)        
    def removefromgrid(self):
        cuadricula[self.y][self.x] = EmptySquare()
        for a in self.ij:
            try:
                cuadricula[self.y+a[1]][self.x+a[0]] = EmptySquare()
            except IndexError: #tratando de mostrar una pieza que no está en pantalla
                pass

    def movimiento(self):
        guardaMov = True
        self.removefromgrid() #elimina si pierde el juego
        for relpos in self.ij+[(0,0)]: #ERROR: no le habia puesto parentesis
            x = self.x+relpos[0]
            y = self.y+relpos[1] - 1 #resto -1 para que sea la nueva pos
            if not type(cuadricula[y][x]) == EmptySquare: #No se va a pdoer mover
                guardaMov = False
            if y < 0:
                guardaMov = False
        if guardaMov: #se pueda mover bajando en 1
            self.y -= 1
            self.showgrid()
        else: #vamos a consolidar a la cuadricula como cuadrados
            for relpos in self.ij+[(0,0)]: #ERROR aqui tenia esto [(0.0)]:
                x = self.x+relpos[0]
                y = self.y+relpos[1] #ERROR aqui tenia en 0 y no tiene sentido debe ser 1 
                cuadricula[y][x] = Cuadrado(self.col)
        return guardaMov #ya la figura se puede mover libremente

    def rotate(self):
        self.removefromgrid()
        rota = True
        temp = []
        for a in self.ij+[(0,0)]:
            x = self.x+a[1] 
            y = self.y-a[0] #ERROR le habia puesto + 
            if x > WIDTH-1: #girar a través de la pared derecha
                rota = False
            elif x < 0: #girar a través de la pared izq
                rota = False
            elif y < 0 or y > HEIGHT - 1: #comprueba la parte inferior y superior del recuadro
                rota = False
            elif type(cuadricula[y][x]) != EmptySquare: #si la casilla objetivo ya está ocupada
                rota = False
        if rota:
            for a in self.ij:
                a = [a[1],-a[0]]
                temp.append(a) #Append() Este método nos permite agregar 
                #nuevos elementos a una lista. En este caso son las figuras o piezas.
            self.ij = temp
        self.showgrid()

    def lado(self, dx): #dx es la distancia para llegar a la base
        self.removefromgrid()
        movimiento = True
        for a in self.ij+[(0,0)]:
            x = self.x+a[0]+dx
            y = self.y+a[1] #ERROR tenia la suma de dx y no tenia sentido aquí
            print(x, y)
            if x > WIDTH-1: #moviendo solo a la derecha
                movimiento = False
            elif x < 0:
                movimiento = False
            elif y > HEIGHT-1 and y < 0:
                movimiento = False
            elif not type(cuadricula[y][x]) == EmptySquare: #si la casila objetivo ya está ocupada
                movimiento = False
        if movimiento:
            self.x += dx
        self.showgrid()

arrayPosicionesTetris = [
    ([(-1,0),(1,0),(2,0)],LIGHT_BLUE),
    ([(-1,0),(0,1),(1,0)],LIGHT_CYAN),
    ([(-1,-1),(-1,0),(1,0)],LIGHT_PURPLE),
    ([(-1,1),(-1,0),(1,0)],LIGHT_GREEN),
    ([(-1,0),(-1,-1),(0,-1)],LIGHT_RED),
    ([(1,0),(-1,-1),(0,-1)],YELLOW),
    ([(-1,0),(0,-1),(1,-1)],LIGHT_WHITE),
]

cuadricula = [[ EmptySquare() for a in range(WIDTH)] for a in range(HEIGHT)]

def display():
    clear_screen()
    print(PURPLE+"TETRIS\n"+GREEN+"SCORE: "+RED+str(score))
    print(GREEN+"="*(WIDTH+2))
    for fila in cuadricula[::-1]:
    #Sintaxis general Objeto_indexable[inicio:final:paso]
    #Como dejar vacia la primera entrada por defecto signfica inicio
    #Y dejar vacia la segunda por defecto es final
    #[::1]
    #Significa "De inicio a final con paso de -1"
    #O sea recorre toda la lista en reversa
        print("|"+"".join([str(s) for s in fila]) + GREEN + "|") 
    #El join()método toma todos los elementos en un iterable y los une en una cadena.
    print(GREEN+"="*(WIDTH+2)+END)

score = 0
random.shuffle(arrayPosicionesTetris )
shuffycounter = 0
shuffcountermax = len(arrayPosicionesTetris ) - 1 
a1,a2 = arrayPosicionesTetris[shuffycounter] #ERROR tenia un espacio que no esta definido en la sintaxis
s = Forma(a1,a2)
s.place()
display()

running = True
while running: #main
    cmd = input("Enter Command: ")
    #TO DO: --> Buscar que se pueda hacer con flechas y que las figuras caigan sin enter.
    #ESTRUCTURA DEL JUEGO
    #"Presiona Enter para ir bajando, 
    # Space y Enter para rotar, 
    # A y luego Enter para moverse a la izq, 
    # y D luego Enter para moverse a la derecha"
    if cmd == " ":
        s.rotate()
    elif cmd.lower() == "a":
        s.lado(-1)
    elif cmd.lower() == "d":
        s.lado(1)
    else: # move down
        if not s.movimiento():
            if s.y >= 18:
                running = False
            #check to see if can remove cuadricula
            counter = 0
            removes = []
            for fila in cuadricula:
                full = True
                for squ in fila:
                    if type(squ) == EmptySquare:
                        full = False
                if full:
                    removes.append(counter)
                counter += 1
            if len(removes) == 1:
                score += 1
            elif len(removes) == 2:
                score += 2
            elif len(removes) == 3:
                score += 3
            elif len(removes) >= 4: 
                score += 5
            for r in removes[::-1]:
                cuadricula.pop(r) #borrado del ultimo al primero
                cuadricula.append([EmptySquare() for a in range(WIDTH)])
            
            shuffycounter += 1
            if shuffycounter > shuffcountermax:
                shuffycounter = 0
                random.shuffle(arrayPosicionesTetris ) #ERROR aqui lo habia tomado como arreglo y es parentesis
            a1,a2 = arrayPosicionesTetris [shuffycounter]
            s = Forma(a1,a2)
            if not s.place():
                running = False
    display()

ex=""
while ex != "exit":
    ex=input("type exit to close: ")