from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

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
    sound=SoundLoader.load("MEDIA/musica_bounty_hunter.mp3")
    if sound:
        sound.volume = 1
        sound.loop = True
        sound.play()
    
    on_pre_leave = sound.stop()


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

class AppPrueba(App):

    col_fondo = get_color_from_hex("#58A75C")
    Window.clearcolor = col_fondo  # Establecer el color de fondo de la ventana
    Window.size = (600, 500)  # Establecer el tamaño de la ventana
    
    # Nota: Si pongo las opciones de música aquí, se reproducirá en todas las ventanas
    
    def play_sound(self, filename):
        sound = SoundLoader.load(filename)
        if sound:
            sound.play()

    def build(self):
        self.sound = SoundLoader.load("MEDIA/musica_lofi_cinematic.mp3")
        self.paused = BooleanProperty(False)  # Variable para controlar el estado de pausa
        self.sound_pos = 0 # Variable para almacenar la posición de reproducción (manual tracking)
        self.is_paused = False  # Estado de la música
        self.play_start_time = 0  # Tiempo cuando comenzó la reproducción
        self.update_event = None  # Event para actualizar la posición
        #self.sound.play()

        if self.sound:
            self.sound.volume = 1
            self.sound.loop = False  # Desactivar loop para que seek funcione correctamente
            # Retrasar la reproducción para asegurar que el sonido esté inicializado
            Clock.schedule_once(self._play_sound, 0.1)

        return kv
    
    def _play_sound(self,dt):
        if self.sound:
            self.sound.play()
            self.play_start_time = Clock.get_time()  # Guardar tiempo de inicio
            self.sound_pos = 0  # Reset posición al iniciar

            # Iniciar actualizaciones periódicas de posición
            if self.update_event:
                self.update_event.cancel()
            self.update_event = Clock.schedule_interval(self._update_position, 0.1)
            print("Música iniciada")
    
    def _update_position(self,dt):
        # obtener la posición de la música
        if self.sound and self.sound.state == 'play':
            elapsed = Clock.get_time() - self.play_start_time
            self.sound_pos = elapsed + self.sound_pos  # Acumular el tiempo transcurrido
        return True
    
    def on_stop(self):
        if self.sound:
            self.sound.stop()  # Detener la música al cerrar la aplicación  

    # OPCIONAL: Crear botón para pausar/reanudar la música

    def toggle_musica(self):
        if self.sound:
            if self.sound.state == 'play':
                # si se está reproduciendo, pausar y guardar posición
                self.sound_pos = self.sound.get_pos()
                self.sound.stop()
                self.is_paused = True
                self.paused = True
                print(f"Se pausó la música en la posición: {self.sound_pos}")
            else:
                # Reproducir primero
                self.sound.play()
                # Reanudar desde la posición guardada con pequeño retraso
                Clock.schedule_once(self.resume_seek, 0.05)
                self.is_paused = False
                self.paused = False
                print(f"Se reanudó la música desde la posición: {self.sound_pos}")
    
    def resume_seek(self,dt):
        if self.sound and self.sound.state == 'play' and self.sound_pos > 0:
            try:
                self.sound.seek(self.sound_pos)
                print(f"Buscando posición: {self.sound_pos}")
            except Exception as e:
                print(f"Error al buscar posición: {e}")

    def get_music_status(self):
        """Debug method to check current music status"""
        if self.sound:
            print(f"Estado: {self.sound.state}, Posición: {self.sound.get_pos()}, Guardada: {self.sound_pos}, Pausado: {self.is_paused}")
        else:
            print("No hay sonido cargado")

if __name__ == "__main__":
    AppPrueba().run()
