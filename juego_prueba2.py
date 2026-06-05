# Versión de prueba con solo 5 pantallas y misiones simples
# musica distinta en cada pantalla

import random

from kivy.lang import Builder
from kivy.app import App
from kivy.properties import NumericProperty, BooleanProperty, StringProperty

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.factory import Factory

from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.uix.video import Video
from kivy.uix.videoplayer import VideoPlayer

from kivy.core.text import LabelBase
from kivy.utils import get_color_from_hex

LabelBase.register(
    name="MiFuente",
    #fn_regular="C:/Users/Dell/Documents/GitHub/AOC_adventure_kivy/mifuente.otf")
    fn_regular="mifuente.otf")

class InventarioPopUp(Popup):
    # definir lógica en Python y apariencia en KV
    num = NumericProperty(5)
    num_objetos_texto = f"Llevas {num} objetos coleccionados"
    num_objetos = StringProperty(num_objetos_texto)
    # FALTA: Contador de cuántos objetos se han seleccionado
    # puede ser contando cuántas imágenes tienen la fuente "missing"/blocked


class Pantalla1(Screen):

    def play_sound(self, filename):
        sound = SoundLoader.load(filename)
        if sound:
            sound.play()

    def animate_it(self, widget):
        # Crear animación: mover a x=150 y cambiar opacidad a 0.5, dura 2 segundos
        anim = Animation(x=150, y=100, opacity=0.5, duration=2, t='out_bounce')
        anim.start(widget)

class Pantalla2(Screen):

    i =0
    limite = False

    def clicks(self):
        self.i += 1
        print(self.i) 
        if self.i == 5:
            print("Llegaste al límite de clicks")
            limite = True
            self.manager.current = "pantalla3"
            self.manager.transition.direction = "right"
            i=0 # reiniciar para la siguiente vez que entremos a la pantalla
    
class Pantalla3(Screen):
    pass


class Pantalla_password(Screen):
    intentos = NumericProperty(1)

    def check_password(self,label_password, input_password):
        
        self.password = input_password.text
        label_password.text = "Ingresa la contraseña: "

        if self.password == "12345":
            self.intentos = 3 #reinicia el texto y num de intentos para el siguiente usuario
            input_password.text = ""
            print("Contraseña correcta")
            self.manager.current = 'pantalla2'
        else:
            print(f'Error. Intento {self.intentos}/3')
            label_password.text = f'Error. Intento {self.intentos}/3'
            input_password.text = ""
            self.intentos += 1
            if self.intentos > 3:
                self.manager.current = 'pantalla_error'

class MediaScreen(Screen):
    def play_sound(self, filename):
        sound = SoundLoader.load(filename)
        if sound:
            sound.play()

class GameScreen(Screen):

    def recolectar(self, widget, touch, *args):
        if widget.collide_point(*touch.pos) and widget.opacity == 1:
            app = App.get_running_app()
            app.puntos +=1 # el puntaje se guarda en todas las ventanas
            print("Puntos:", self.puntos)
            self.root.ids.score_label = f'Puntos: {self.puntos}'
            widget.opacity = 0 # esconde el objeto después de encontrarlo


class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("juego_prueba2.kv")

class AppJuego(App):
    #Window.clearcolor = (.5, 1, .2, 1)  # Establecer el color de fondo de la ventana
    Window.size = (600, 400)  # Establecer el tamaño de la ventana

    def build(self):
        return kv

    def _play_sound(self,dt):
        if self.sound:
            self.sound.play()
    
    def on_stop(self):
        if self.sound:
            self.sound.stop()  # Detener la música al cerrar la aplicación  

    # función para recolectar los objetos

    puntos = 0
    lista_trinkets = ["MEDIA/trinkets/trinket1.png",
                    "MEDIA/trinkets/trinket2.png",
                    "MEDIA/trinkets/trinket3.png",
                    "MEDIA/trinkets/trinket4.png",
                    "MEDIA/trinkets/trinket5.png"]

    def colocar_trinkets(self):
        import random
        from kivy.uix.image import Image

        estado_trinket = False # esto cambiará si encontraste el objeto
        if not estado_trinket:
            ruta= "MEDIA/trinkets/missing.png"
        else:
            i= random.randint(len(self.lista_trinkets)) # cambiar esto
            ruta = self.lista_trinkets[i] # elegir uno de los trinkets de la lista
            
        trinket = Image(source=ruta)

if __name__ == "__main__":
    AppJuego().run()