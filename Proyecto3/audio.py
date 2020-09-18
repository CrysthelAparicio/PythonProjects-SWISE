"""Ecualizador de audio de fuente con sonido de entrada"""
#Libreria Principal
import pyaudio

#Librerias conocidas
import struct
import sys
import numpy as np

#Librerias extras
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
from scipy.fftpack import fft
from pynput.keyboard import Listener, Key

#Clases

class FlujoAudio:
    """Transmitir audio de la fuente de entrada (micro) y mostrará de forma continua un
    gráfico (barra) basado en el espectro de audio de los datos de la forma de onda"""

    def __init__(self, num, simbolo):
        self.rastros = set() # El método se utiliza para 
        #convertir cualquiera de los iterables en una secuencia de elementos iterables
        self.numero = num
        self.simbolo = simbolo

        #pyaudio setup
        #El sonido se almacena en binario, 
        #al igual que todo lo relacionado con las computadoras.
        #paInt16 es básicamente una cadena binaria de 16 bits con signo. 
        #15 bits para el número y uno para el signo

        self.FORMAT = pyaudio.paInt16  # bytes / muestra
        self.CHANNELS = 1  # sonido mono / Un canal para el micrófono
        self.RATE = 44100  # muestra / sec (44.1 kHz)
        self.CHUNK = 1024  # cuánto audio procesado / fotograma... 
        #se establece más pequeño para una mayor velocidad de fotogramas

        # Instancia de clase PyAudio para administrar los canales de entrada y salida
        self.p = pyaudio.PyAudio()

        # Se abre el flujo (stream) para la transmisión de data en tiempo real
        stream = p.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            output=False,
            frames_per_buffer=CHUNK
        )
        #espectro x puntos

if __name__ == "__main__":
    # Validación común -------------------
    saltoLinea = "-" * 20
    fueraRango = "Fuera de rango! Intente de nuevo: "
    # -----------------------------------------------

    print("Ingrese el tipo de gráfico que desea visualizar.")
    print(saltoLinea)
    print("1: Gráfico de Barra")
    print("2: Gráfico de Dispersión")
    print("3: Gráfico Curvo")
    print("4: Gráfico de Línea")
    print("5: Salir")
    print(saltoLinea)
    simbolo = "o"  # default symbol to instantiate AudioStream class
    number_input = input("Tipo de Gráfico: ")
    while True:
        try:
            numero = int(number_input)
            if numero >= 1 and numero <= 5:
                break
        except ValueError:  # por si no ponen un número xD 
            pass
        number_input = input(fueraRango)

    if numero == 2:
        print("Escoge la forma / símbolo")
        print(saltoLinea)
        print("1: Diamante")
        print("2: Circular")
        print("3: X")
        print("4: Triangular")
        print("5: Cuadrado")
        print(saltoLinea)
        simbolo = int(input("Símbolo: "))
        while simbolo < 1 or simbolo > 5:
            simbolo = int(input(fueraRango))
        simbolo = int_to_symbol(simbolo)
    elif numero == 5:
        exit()

