# Juego de misiones: Aplicación con varias pantallas y botones para navegar entre ellas
# Versión AOC - Tema: Star Wars?
# usaremos un archivo .kv para definir la interfaz gráfica

from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.button import Button

# ----- definir una paleta de colores para el juego -----
from kivy.utils import get_color_from_hex
# uso en KV: background_color: utils.get_color_from_hex('#3498db')

turquesa = get_color_from_hex("#26D4E0")
azul = get_color_from_hex("#2B7ED1")
morado = get_color_from_hex("#3D0EAA")
cafe = get_color_from_hex("#6A3A0A")
verde = get_color_from_hex("#217D32")
arena = get_color_from_hex("#A8742A")

# En la clase de cada pantalla creamos las funciones que controlen cada "misión" del juego
# y en el archivo .kv definimos los botones que llamarán a esas funciones para avanzar en la historia

class Pantalla_prueba(Screen):
    pass

class Pantalla1(Screen):
    pass

class Pantalla2(Screen):
    pass

class Pantalla3(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("Juego_aoc.kv")

class AppJuego(App):
    Window.clearcolor = verde  # Establecer el color de fondo de la ventana
    Window.size = (600, 400)  # Establecer el tamaño de la ventana
    
    def build(self):
        return kv

if __name__ == "__main__":
    AppJuego().run()