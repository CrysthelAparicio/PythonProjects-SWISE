import curses
import time

from board import BlockBoard
import blocks

WAIT_TIME = 1
H = 16
W = 10

#Funcion para imprimir el board o escenario de juego
def print_board(board: list):
	for row in range(len(board)):
		row_str = "|"
		row_str += " ".join(board[row])
		row_str += "|"
		stdscr.addstr(row, 0, row_str)
	stdscr.refresh() 
	#stdscr es para inciar y finalizar una aplicación de curses :3

def print_log(row, log):
	stdscr.clrtoeol()
	stdscr.addstr(row + H + 2, 0, str(log))
	stdscr.refresh()
	#addstr()muestra una cadena en la ubicación
	#actual del cursor en la stdscrventana

	#Borrar desde el cursor hasta el final de la ventana: 
	# se eliminan todas las líneas debajo del cursor y luego se realiza el equivalente de clrtoeol().

def shiftBlock(key, board: BlockBoard):
	#Manejo del flechas teclado 
	if key == curses.KEY_LEFT:
		board.shiftBlockLeft()
	elif key == curses.KEY_RIGHT:
		board.shiftBlockRight()
	elif key == curses.KEY_DOWN:
		board.shiftBlockBottom()
	elif key == curses.KEY_UP:
		board.transposeBlock()

	tempBoard2 = board.getCurrentBoard()
	print_board(tempBoard2)


if __name__ == "__main__":
	stdscr = curses.initscr()
	curses.noecho()
	#Para poder leer las teclas y solo mostrarlas en
	#determinadas circunstancias. 
	#Esto requiere llamar a la noecho()función.
	curses.cbreak()
	#Por lo general, las aplicaciones también necesitarán reaccionar 
	#a las teclas al instante, sin necesidad de presionar 
	#la tecla Intro; esto se llama modo cbreak, a diferencia 
	#del modo de entrada con búfer habitual.
	stdscr.keypad(True)
	# stdscr.nodelay(True)
	stdscr.timeout(WAIT_TIME * 1000)

	mainBoard = BlockBoard(W, H) #width & height
	print_board(mainBoard.board)
	print_log(0, "Score: {0}".format(mainBoard.removedLineCount))

	try:
		while True:
			newBlockSuccessful = mainBoard.setBlock(blocks.randomBlock())

			if not newBlockSuccessful:  #final del juego
				break

			while True:
				print_board(mainBoard.getCurrentBoard())

				endWait = time.time() + WAIT_TIME
				while time.time() < endWait:
					pressedKey = stdscr.getch()
					shiftBlock(pressedKey, mainBoard)

				#bloque de cambio de fondo
				shiftBottomSuccessful = mainBoard.shiftBlockBottom()
				if not shiftBottomSuccessful:
					break

			#hay colisión, actualizar el tablero
			mainBoard.saveBlock()
			print_log(0, "Score: {0}".format(mainBoard.removedLineCount))

	except KeyboardInterrupt:
		print("quit")
	finally:
		curses.echo()
		curses.nocbreak()
		stdscr.keypad(False)
		curses.endwin()
		print("Game Over")
		print("Score: {0}".format(mainBoard.removedLineCount))