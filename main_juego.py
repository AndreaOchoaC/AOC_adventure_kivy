# Clase 14 mayo 2026
# Aplicación con varias pantallas y botones para navegar entre ellas
# usaremos un archivo .kv para definir la interfaz gráfica

from kivy.lang import Builder
from kivy.app import App
from kivy.properties import NumericProperty, BooleanProperty

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.window import Window

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

class Pantalla1(Screen):

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

class VideoScreen(Screen):
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

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("main_juego.kv")

class AppJuego(App):
    #Window.clearcolor = (.5, 1, .2, 1)  # Establecer el color de fondo de la ventana
    Window.size = (600, 400)  # Establecer el tamaño de la ventana
    
    def build(self):
        # Nota: Si pongo las opciones de música aquí, se reproducirá en todas las ventanas

        self.sound = SoundLoader.load("MEDIA/musica_lofi_cinematic.mp3")
        self.paused = BooleanProperty(False)  # Variable para controlar el estado de pausa
        self.sound_pos = 0 # Variable para almacenar la posición de reproducción (manual tracking)
        self.is_paused = False  # Estado de la música
        self.play_start_time = 0  # Tiempo cuando comenzó la reproducción
        self.update_event = None  # Event para actualizar la posición

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

        return kv
    
    def saludar(self):
        print("Hola, bienvenido")

if __name__ == "__main__":
    AppJuego().run()