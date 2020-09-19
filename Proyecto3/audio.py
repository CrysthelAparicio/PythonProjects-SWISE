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

    def __init__(self, num, symbol):
        self.traces = set() # El método se utiliza para 
        #convertir cualquiera de los iterables en una secuencia de elementos iterables
        self.number = num
        self.symbol = symbol

        #pyaudio setup
        #El sonido se almacena en binario, 
        #al igual que todo lo relacionado con las computadoras.
        #paInt16 es básicamente una cadena binaria de 16 bits con signo. 
        #15 bits para el número y uno para el signo
        # pyaudio setup

        self.FORMAT = pyaudio.paInt16  # bytes / muestra
        self.CHANNELS = 1  # sonido mono / Un canal para el micrófono
        self.RATE = 44100  # muestra / sec (44.1 kHz)
        self.CHUNK = 1024  # cuánto audio procesado / fotograma... 
        #se establece más pequeño para una mayor velocidad de fotogramas

        # Instancia de clase PyAudio para administrar los canales de entrada y salida
        self.p = pyaudio.PyAudio()

        # Se abre el flujo (stream) para la transmisión de data en tiempo real
        self.stream = self.p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            output=True,
            frames_per_buffer=self.CHUNK,
        )
        #espectro x puntos
        self.f = np.linspace(1, int(self.RATE / 2), 64)

        #pyqtgraph setup
        pg.setConfigOptions(antialias=True)
        self.app = QtGui.QApplication(sys.argv)
        self.win = pg.GraphicsWindow(title="Audio Spectrum")
        self.win.setGeometry(10, 52, 480 * 2, 200 * 2)
        #configuración del contenido de la ventana
        self.audio_plot = self.win.addPlot(row=1, col=1)
        self.audio_plot.setYRange(0.00, 0.25)
        self.audio_plot.setXRange(2000, int(self.RATE / 2))
        self.audio_plot.showGrid(x=True, y=True)
        self.audio_plot.hideAxis("bottom")
        self.audio_plot.hideAxis("left")

        self.a = {
            "color": "r",
            "colorIndex_x": 100,
            "colorIndex_y": 100,
            "colorIndex_z": 255,
        }

        #Inicio del Gráfico
        self.graph = None

    @staticmethod
    def set_gradient_brush():
        """establecer el gradiente de color, devolver QtGui.QBrush obj"""
        grad = QtGui.QLinearGradient(0, 0, 0, 1)
        grad.setColorAt(0.1, pg.mkColor("#FF0000"))
        grad.setColorAt(0.24, pg.mkColor("#FF7F00"))
        grad.setColorAt(0.38, pg.mkColor("#FFFF00"))
        grad.setColorAt(0.52, pg.mkColor("#00FF00"))
        grad.setColorAt(0.66, pg.mkColor("#0000FF"))
        grad.setColorAt(0.80, pg.mkColor("#4B0082"))
        grad.setColorAt(0.94, pg.mkColor("#9400D3"))
        grad.setCoordinateMode(QtGui.QGradient.ObjectMode)
        return QtGui.QBrush(grad)

    #Barra Gráfica
    def set_plotdata_1(self, name, data_x, data_y):
        """establecer un gráfico con los datos iniciales y los nuevos datos... referencia
        self.traces para verificar la entrada de datos init o recurrentes"""
        if name in self.traces:
            #actualizar el contenido del gráfico de barras
            self.graph.setOpts(x=data_x, height=data_y, width=350)
        else:
            self.traces.add(name)
            #configuración inicial del gráfico de barras
            brush = self.set_gradient_brush()
            self.graph = pg.BarGraphItem(
                x=data_x, height=data_y, width=50, brush=brush, pen=(0, 0, 0)
            )
        self.audio_plot.addItem(self.graph)

    #Barra de Dispersión
    def set_plotdata_2(self, name, data_x, data_y):
        data_y = data_y[:64]
        brush_default = pg.mkBrush(
            self.a["colorIndex_x"], self.a["colorIndex_y"], self.a["colorIndex_z"], 100
        )
        if name in self.traces:
            #actualizar el contenido de la trama de dispersión
            self.graph.clear()
            self.graph.setData(data_x, data_y, brush=brush_default)
        else:
            self.traces.add(name)
            #configuración inicial del gráfico de dispersión
            self.graph = pg.ScatterPlotItem(
                x=data_x,
                y=data_y,
                pen=None,
                symbol=self.symbol,
                size=30,
                brush=(100, 100, 255, 100),
            )
        self.audio_plot.addItem(self.graph)

    #Gráfico de Curva
    def set_plotdata_3(self, name, data_x, data_y):
        data_y = data_y[:64]
        if name in self.traces:
            #actualizar el contenido del gráfico de la curva
            self.graph.clear()
            pen1 = pg.mkPen(
                self.a["colorIndex_x"],
                self.a["colorIndex_y"],
                self.a["colorIndex_z"],
                bright=100,
            )
            self.graph = pg.PlotCurveItem(x=data_x, y=data_y, pen=pen1,)
        else:
            self.traces.add(name)
            #configuración inicial de la gráfica de la curva
            self.graph = pg.PlotCurveItem(x=data_x, y=data_y, pen="r",)
        self.audio_plot.addItem(self.graph)

    #Gráfico de Líneas
    def set_plotdata_4(self, name, data_x, data_y):
        data_y = data_y[:64]
        if name in self.traces:
            #actualizar el contenido del gráfico de la curva
            self.graph.clear()
            pen1 = pg.mkPen(
                self.a["colorIndex_x"],
                self.a["colorIndex_y"],
                self.a["colorIndex_z"],
                bright=100,
                width=15,
                style=QtCore.Qt.DashLine,
            )
            self.graph.setData(data_x, data_y, pen=pen1, shadowPen="#19070B")
        else:
            pen1 = pg.mkPen(color=(250, 0, 0), width=15, style=QtCore.Qt.DashLine)
            self.traces.add(name)
            #configuración inicial de la gráfica de la curva
            self.graph = pg.PlotCurveItem(x=data_x, y=data_y, pen=pen1, shadowPen="r",)
        self.audio_plot.addItem(self.graph)

    def actualizar(self):
        """actualizar el gráfico por el número que el usuario eligió"""
        plot_data = {
            1: self.set_plotdata_1,
            2: self.set_plotdata_2,
            3: self.set_plotdata_3,
            4: self.set_plotdata_4,
        }

        plot_data.get(self.number)(
            name="spectrum", data_x=self.f, data_y=self.calculate_data()
        )

    def calculate_data(self):
        """get sound data and manipulate for plotting using fft"""
        #obtener y descomprimir los datos de la forma de onda
        wf_data = self.stream.read(self.CHUNK, exception_on_overflow=False)
        wf_data = struct.unpack(
            str(2 * self.CHUNK) + "B", wf_data
        ) 
        #generar datos del espectro para graficar usando fft (transformada rápida de Fourier)
        sp_data = fft(
            np.array(wf_data, dtype="int8") - 128
        )  # - 128 :: cualquier int menos de 127 envolverá hasta 256 abajo
        #np.abs (abajo) convierte el complejo num en fft a magnitud real
        sp_data = (
            np.abs(sp_data[0 : int(self.CHUNK)])  #cortar: cortar la primera mitad de nuestro fft
            * 2
            / (256 * self.CHUNK)
        )  #reescalar: mult 2, forma de onda div amp y no. freq en su espectro
        sp_data[sp_data <= 0.001] = 0
        return sp_data

    @staticmethod
    def start():
        """Inicio"""
        if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
            QtGui.QApplication.instance().exec_()

    def change_color(self, key):
        """cambiar el color en el gráfico de la curva después del inicio"""
        """
            blanco : 255,255,255     rojo : 255, 0, 0       anaranjado : 255, 106, 0
            amarillo : 255, 255, 0   verde : 0, 255, 0    azul cielo : 0, 255, 255
            azul : 0, 0, 255      morado: 166, 0, 255   rosado : 255, 0, 255
        """
        color_index = {
            Key.f1: (255, 255, 255),  # blanco
            Key.f2: (255, 0, 0),  # rojo
            Key.f3: (255, 106, 255),  # anaranjado
            Key.f4: (255, 255, 0),  # amarillo
            Key.f5: (0, 255, 0),  # verde
            Key.f6: (0, 255, 255),  # azul cielo
            Key.f7: (0, 0, 255),  # azul
            Key.f8: (166, 0, 255),  # morado
            Key.f9: (255, 0, 255),  # rosado
        }
        self.color_index_control()

        try:
            if key == Key.up:  # rojo higher
                AUDIO_APP.a["color_x"] = self.a["colorIndex_x"]
                self.a["colorIndex_x"] += 10
            elif key == Key.right:  # verde higher
                AUDIO_APP.a["color_y"] = self.a["colorIndex_y"]
                self.a["colorIndex_y"] += 10
            elif key == Key.left:  # azul higher
                AUDIO_APP.a["color_z"] = self.a["colorIndex_z"]
                self.a["colorIndex_z"] += 10
            else:
                (
                    self.a["colorIndex_x"],
                    self.a["colorIndex_y"],
                    self.a["colorIndex_z"],
                ) = color_index.get(key)
        except Exception as error:
            print(error)

    def color_index_control(self):
        for color_rgb in ("colorIndex_x", "colorIndex_y", "colorIndex_z"):
            if self.a[color_rgb] >= 255:
                self.a[color_rgb] = 0

    def animacion(self):
        """Llama al autoinicio y a la autoactualización para la continua
        aplicación de salida"""
        timer = QtCore.QTimer()
        timer.timeout.connect(self.actualizar)
        timer.start(20)
        self.start()


def int_to_symbol(symbol):
    symbol_to_char = {1: "d", 2: "o", 3: "x", 4: "t", 5: "s"}

    return symbol_to_char.get(symbol)


if __name__ == "__main__":
    # Validación común -------------------
    line_break = "-" * 20
    out_of_range = "Fuera de rango! Intente de nuevo: "
    # -----------------------------------------------

    print("Ingrese el tipo de gráfico que desea visualizar.")
    print(line_break)
    print("1: Gráfico de Barra")
    print("2: Gráfico de Dispersión")
    print("3: Gráfico Curvo")
    print("4: Gráfico de Línea")
    print("5: Salir")
    print(line_break)
    symbol = "o"  #símbolo por defecto para instanciar la clase FlujoAudio
    number_input = input("Tipo de Gráfico: ")
    while True:
        try:
            number = int(number_input)
            if number >= 1 and number <= 5:
                break
        except ValueError:  # por si no ponen un número xD 
            pass
        number_input = input(out_of_range)

    if number == 2:
        print("Escoge la forma / símbolo")
        print(line_break)
        print("1: Diamante")
        print("2: Circular")
        print("3: X")
        print("4: Triangular")
        print("5: Cuadrado")
        print(line_break)
        symbol = int(input("Símbolo: "))
        while symbol < 1 or symbol > 5:
            symbol = int(input(out_of_range))
        symbol = int_to_symbol(symbol)
    elif number == 5:
        exit()

    AUDIO_APP = FlujoAudio(number, symbol)
    with Listener(on_press=AUDIO_APP.change_color) as listener:
        AUDIO_APP.animacion()
    listener.join()
