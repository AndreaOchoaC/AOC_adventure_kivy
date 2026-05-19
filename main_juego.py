# Clase 14 mayo 2026
# Aplicación con varias pantallas y botones para navegar entre ellas
# usaremos un archivo .kv para definir la interfaz gráfica

from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.button import Button

class Pantalla1(Screen):
    pass

class Pantalla2(Screen):
    pass

class Pantalla3(Screen):
    pass

class Pantalla4(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("main_juego.kv")

class AppJuego(App):
    #Window.clearcolor = (.5, 1, .2, 1)  # Establecer el color de fondo de la ventana
    Window.size = (600, 400)  # Establecer el tamaño de la ventana
    
    def build(self):
        return kv
    
    def saludar(self):
        print("Hola, bienvenido")

if __name__ == "__main__":
    AppJuego().run()