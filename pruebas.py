from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex

from kivy.core.text import LabelBase
LabelBase.register(
    name="MiFuente",
    fn_regular="C:/Users/Dell/Documents/GitHub/AOC_adventure_kivy/mifuente.otf")

class Pantalla_prueba(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("pruebas.kv")

class AppPrueba(App):

    col_fondo = get_color_from_hex("#046609")
    Window.clearcolor = col_fondo  # Establecer el color de fondo de la ventana
    Window.size = (600, 400)  # Establecer el tamaño de la ventana
    
    def build(self):
        return kv
    
    def saludar(self):
        print("Hola, bienvenido")

if __name__ == "__main__":
    AppPrueba().run()
