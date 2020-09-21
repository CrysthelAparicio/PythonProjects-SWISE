<p align="center">
  <a href="https://github.com/CrysthelAparicio/PythonProjects-SWISE">
    <img src="https://s3.amazonaws.com/com.twilio.prod.twilio-docs/original_images/header.gif" alt="Python Course" width=230 height=150>
  </a>
  <h2 align="center">Python-SWISE Course</h2>

  <p align="center">
    Bienvenidos! Somos un grupo de 4 jovenes, soñadores, ambiciosos y por los momentos enamorados de python. Este es un taller impartido gracias a SWISE 
    y nuestro tutor Luis Felipe Flores. 
    <br>
    </p>
</p>

<br>

## Tabla de Contenidos
- [Descripción](#descripcion)
- [Sobre SWISE?](#sobre-swise)
- [Sobre Python](#how-to-use-them)
- [Líbrerias que utilizamos](#roadmap)
- [Sobre el Team](#contributors)

<hr>

### Descripción

En este curso estamos aprendiendo el uso de Python, en donde realizaremos 3 proyectos aplicando conocimientos de programación, física y matemáticas.

Hemos realizado los siguientes proyectos:

 - Cinemática 🚀
 - Text Game en nuestro caso un Tetris 🕹

## Instalación
### Clone

- Clona este repo con el siguiente comando desde tu terminal `git clone https://github.com/CrysthelAparicio/PythonProjects-SWISE.git`

### Configuracíon

- Para ver el primer proyecto lo puedes hacer desde jupyter notebook o google colab.

- Cada proyecto estará guardado en una carpeta diferente:

> colocate dentro del proyecto y haz lo siguiente: 

```shell
$ cd PythonProjects-SWISE
$ ls
```
![Git](git1.png)

> entra en una carpeta: 

```shell
$ cd Proyecto2
$ ls
```
![Git](git2.png)

> a correr las versiones de tetris: 

```shell
$ python tetriss.py
$ python tetris.py
```
![Git](gifT.gif)
![Git](gifX.gif)

<hr>

### Sobre SWISE

SWISE es una organización a nivel mundial por sus siglas en inglés Society of Women in the Space Exploration. 
La cede principal está en Estados Unidos y comenzó hace muy poco. Hay alrededor de 45 capítulos (grupos) en diferentes 
<br>
universidades de los Estados Unidos. En otros países hay capítulos en México, India, Australia, Costa Rica y aquí en Honduras.
Somos el segundo país centroamericano en abrir un capítulo.
<br>
Puedes visitar la página para más info ⭐️
  - [SWISE webpage](https://www.swise.org/)

Actividades:
* Actividades Academicas: Por ejemplo la participación en charlas de profesores que se han dedicado a estudiar temas relacionados con exploración espacial, cursos, talleres, etc.

* Actividades de Voluntariado: Estas actividades están orientadas a causar un impacto en la sociedad hondureña, para que todos puedan conocer que estudiar carreras científica es una opción y hay muchísimas oportunidades, de momento se están planeando talleres de astronomía para niños y niñas (es la mejor edad para que enseñarles sobre ciencia).

* Actividades Sociales: Estas son actividades que ayudan a convivencia entre todos los de grupo, que puedan compartir mucho, que buscar apoyo en sus clases, etc.

<hr>

### Sobre Python 🐍

1. Python es un lenguaje de programación de propósito general muy poderoso y flexible, a la vez que sencillo y fácil de aprender.
[Link de Descarga](https://www.python.org/) **Python contiene una gran cantidad de librerías, tipos de datos y funciones incorporadas en el propio lenguaje, que ayudan a realizar muchas tareas comunes sin necesidad de tener que programarlas desde cero**.

2. Utilizamos el administrador de ambientes y paquetes llamado Conda. Éste lo instalamos con su instalación mínima llamada "miniconda" en este sitio: 
🚧 👷‍ ⛏ 👷 🔧️ 🚧
    * [Linux](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html)
    * [Windows](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html)
    * [MacOS](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html)
Si quieres correr nuestros proyectos, te recomendamos instalar la versión 3.7, pero de preferencia la más reciente.

3. Quieres descargar nuestro proyecto? Sientete libre de hacerlo, puedes dirigirte aquí:
:point_down: :point_down:

![Git](Git.png)

4. Quieres dar sugerencias? Sientete libre: Es open source. Pueden ingresar a [Issues](https://github.com/CrysthelAparicio/PythonProjects-SWISE/issues):

<hr>

### Movimiento de proyectiles

El movimiento de proyectiles o tiro parabólico, es un movimiento vectorial descrito por dos componentes, el cual es la composición de dos movimientos, siendo uno un movimiento uniforme(MU) y el otro un movimiento uniformemente acelerado(MUA), lo cual resulta en una trayectoria parabólica, como su nombre lo atribuye, donde la componente en **x** es la que describe un movimiento con velocidad constante, mientras que la componente en **y** describe un movimiento con aceleración constante, donde ésta aceleración es la gravedad, sobre la cual está sujeta el proyectil.
Para el análisis de movimiento de proyectiles, para este proyecto tomó el caso más sencillo donde no existirán fuerzas externas actuando sobre el proyectil, por lo cual se emplearan las ecuaciones del movimiento uniformemente acelerado(MUA), con la única restricción que la componente en **x** su velocidad será constante, teniendo de esa forma una aceleración nula en **x** y que además tendremos que realizar una modificación para de esa forma tener una combinación de ambas ecuaciones esto producto de la presencia de un ángulo inicial y se deberá realizar una representación polar de la posición del cohete; para la programación empleada para este primer proyecto solo es necesario emplear las ecuaciones del MUA y MU, y sus combinaciones, para de esa forma poder resolver los problemas propuestos en los lineamientos.

Las ecuaciones que fueron programadas para la resolución de este proyecto son las siguientes:

**Componente en x**

* $x( t ) = x_0 + v_0*t$

* $v( t ) = v_0$

**Componente en y**

* $y(t) = y_0 + v_0*t + \frac{1}{1} *ay*t^2$

* $v(t) = v_0 + ay*t$

**Representación Polar**

* $v_{0x} = v_0 * \cos \theta$

* $v_{0y} = v_0 * \sin \theta $

* $\theta = \arctan \frac{v0_{y}}{v0_{x}} $

* $v_0 = \sqrt{v_{0x}^{2} + v_{0y}^{2}}$


<hr>

### Tetris 
Es uno de los juegos que más populares, creado en 1985 por el Ingeniero informático Ruso Alexei Pajitnov  mientras trabajaba para el Centro de Computación Dorodnitsyn de la Academia de Ciencias de la Unión Soviética en Moscú, RSFS de Rusia. 
El nombre Tetris deriva del étimo griego tetra, que significa cuatro, y hace referencia a la cantidad de cuadros que componen las piezas del juego. Alexei Pajitnov programó en una sola tarde la primera versión del juego en un Electrónika 60. 
Cada una de las versiones que se han sacado al mercado varían las dimensiones y el área del juego. El jugador no puede impedir esta caída, pero puede decidir la rotación de la pieza (0°, 90°, 180°, 270°) y en qué lugar debe caer. Cuando las piezas
colocadas en la parte inferior de la pantalla forman una línea horizontal completa estas van desapareciendo, dejando espacio para que sea sustituido por nuevas piezas. El juego termina cuando las piezas se amontonan hasta llegar a lo más alto de la interfaz, impidiendo apilar más piezas.
Para esta actividad, decidimos realizar el Tetris, basándonos en las experiencias previas de la programación  del juego en otros lenguajes, sin embargo, también tenemos como bases los requerimientos que el instructor nos ha brindado:

* **Al menos un ente que se pueda sin ambigüedad llamar protagonista**, para este inciso, el protagonista será el usuario, quien tendrá la oportunidad de incrementar su puntaje a medida apila correctamente la mayor cantidad de piezas. 

* **El protagonista evoluciona en los estados** , como sabemos que estamos condenados a perder desde el principio, no sabemos cuánto tardará en aparecer la secuencia fatal, existen explicaciones con fundamento matemático que dice que el fracaso se debe en gran parte al mecanismo aleatorio de las piezas lanzadas que son imposibles de encajar creando huecos que nunca podrás llegar a cubrir.    Principalmente las piezas con forma se "S" y "Z" tienden a arruinar el trabajo hecho hasta el momento.

* **Debe existir un objetivo claro a alcanzar**, como se explica en el inciso anterior, él usuario no podrá ganar, sin embargo, su objetivo será acumular la mayor cantidad de puntos.

* **Se debe utilizar programación orientada a objetos**,  principalmente, basados es:
    * Al menos tres clases distintas: Para el juego se implementaron las clases:
        * Class Cuadrado, en el cual se utiliza el método  \__ **init**\__
        * Class EmptySquare, con el método \__ **str**\__
        * Class Forma,con el método \__ **str**\__
    * Al menos una clase que herede de otra clase y adicione dos métodos distintos sobre los de su clase padre. 
    * Al menos un caso de sobrecarga de operadores.
    
    
* **Totalmente basado en texto**, sin importar paquetes adicionales a: Pandas, Geopandas, Numpy y los incluidos en la base de Python (y paquetes de estética como pprint). El desarrollo del juego está únicamente orientado a objetos, mediante clases, métodos y herencias, así como arreglos. De igual forma se puede observar al ejecutar que las piezas están formadas por símbolos como “x” .

# Descripción del juego de Star Wars---Proyecto Final Pygame

El juego de distaparos (shooter), está basado en la librería **Pygame**, en el cual utilizamos distintas herramientas para lograr correr el juego y crear un entorno llamativo para el usuario, mediante una serie de imáneges.png.
El escenario del juego, consta de un fondo, simula el espacio exterior, en el cual una nave será la encargada de disparar a los meteoritos (enemigos) y acumular la mayor cantidad de puntos. Cabe destacar que si la nave recibe cuatro golpes de los asteroides, el juego se reiniciará. Por lo que es conveniente el detectar las coliciones mediante *spritcolide*. 

Para lograr que la nave dispare a los meteoros, se programa una función para crear una bala cada vez que se presione la barra de espacio.Así mismo el marcador del puntaje, para que el usuario observe su progreso en el juego, . Para dar un dramatismo al juego, se pueden incluir las imágenes necesarias para que la explosión del enemigo sea más llamtiva. Se agregó sonido al juego para que se reproduzca a medida éste vaya eliminando los meteoritos, esto mediante un ciclo *For*. 

Debemos tomar en cuenta que para el juego funciones, debe tener tener instalado las siguientes librerias:

* **Pyflakes:** La cual es una herramienta de análisis de código Python,puede detectar potenciales problemas como:

    * Módulos importados sin usar.
    * Variables sin usar.
Para instalarlo, colocar en la terminal: *pip install pyflakes*


* **Pygame:** Es un módulo del lenguaje de programación Python que permiten la creación de videojuegos en dos dimensiones de una manera sencilla. Mediante PyGame podemos utilizar sprites (objetos), cargar y mostrar imágenes en diferentes formatos, sonidos, etc. Además, al ser un módulo destinado a la programación de videojuegos se puede monitorizar el teclado o joystick de una manera bastante sencilla.

Para instalarlo, colocar en la terminal: *pip install pygame*


<hr>

### Líbrerias que utilizamos
  📚 📌 📦
- [x] numpy
- [x] math
- [x] matplotlib.pyplot 
- [x] itertools
- [x] scipy.stats
- [x] random
- [x] Curses
- [x] time
- [x] copy

<hr>

### Contributors 👥👥

<a href="https://github.com/CrysthelAparicio/PythonProjects-SWISE/graphs/contributors">
    <img src="colab.png" />   
</a>

- **[@CrysthelAparicio](https://github.com/CrysthelAparicio)** 👩🏻‍💻
- **[@alcantaraoscar](https://github.com/alcantaraoscar)** 🧑🏻‍💻 
- **[@dacosta16](https://github.com/dacosta16)** 👨🏻‍💻
- **[@Adriana-Elizabeth-Salgado](https://github.com/Adriana-Elizabeth-Salgado)** 👩🏻‍💻

Hecho con :heart: y Python.