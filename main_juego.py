# Clase 14 mayo 2026
# Aplicación con varias pantallas y botones para navegar entre ellas
# usaremos un archivo .kv para definir la interfaz gráfica

from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.properties import NumericProperty

class Fade(Screen):
    opacidad = 1

    def fade(self, btn):
        for i in range(0,1):
            self.opacidad -= 0.1
            print("Opacidad=", self.opacidad)
            btn.background_color = 0.5, 0.5, 0.5, self.opacidad

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