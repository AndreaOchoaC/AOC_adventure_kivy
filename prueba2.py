from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.button import Button

from kivy.properties import BooleanProperty
from kivy.core.audio import SoundLoader
from kivy.clock import Clock

from kivy.uix.video import Video
from kivy.uix.videoplayer import VideoPlayer
# para que reproduzca los videos correctamente:
# pip install ffpyplayer

from kivy.core.text import LabelBase
from kivy.utils import get_color_from_hex

LabelBase.register(
    name="MiFuente",
    #fn_regular="C:/Users/Dell/Documents/GitHub/AOC_adventure_kivy/mifuente.otf")
    fn_regular="mifuente.otf")

class Pantalla_prueba(Screen):
    pass

class MenuScreen(Screen):
    app = App.get_running_app()
    app.play_sound("MEDIA/musica_bounty_hunter.mp3")

class MediaScreen(Screen):
    pass

class VideoScreen(Screen):
    pass

# si quisiéramos definir el video en la clase VideoScreen:
'''
class VideoScreen(Screen):
    #video = Video(source="MEDIA/video_patos.mp4", state="play")
    #video = VideoPlayer(source="MEDIA/video_patos.mp4", state="play")
    return video
'''

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("pruebas.kv")

class SoundButton(Button):
    def play_sound(self, filename):
        sound = SoundLoader.load(filename)
        sound.volume = 1
        sound.loop = 1
        if sound:
            sound.play()

class AppPrueba(App):

    col_fondo = get_color_from_hex("#58A75C")
    Window.clearcolor = col_fondo  # Establecer el color de fondo de la ventana
    Window.size = (600, 500)  # Establecer el tamaño de la ventana
    
    # Nota: Si pongo las opciones de música aquí, se reproducirá en todas las ventanas
    
    def play_sound(self, filename):
        sound = SoundLoader.load(filename)
        sound.volume = 1
        sound.loop = 1
        if sound:
            sound.play()

    def build(self):

        return kv
    
    def on_stop(self):
        if self.sound:
            self.sound.stop()  # Detener la música al cerrar la aplicación  

    def get_music_status(self):
        """Debug method to check current music status"""
        if self.sound:
            print(f"Estado: {self.sound.state}, Posición: {self.sound.get_pos()}, Guardada: {self.sound_pos}, Pausado: {self.is_paused}")
        else:
            print("No hay sonido cargado")

if __name__ == "__main__":
    AppPrueba().run()
