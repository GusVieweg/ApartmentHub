from kivy.app import App 
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.animation import Animation, AnimationTransition
from kivy.uix.screenmanager import ScreenManager, Screen 

class AnotherScreen(Screen):
    def __init__(self, **kwargs):
        #make sure we aren't overriding any important functionality
        super(AnotherScreen, self).__init__(**kwargs)
        f = FloatLayout()

        greeting_label = Label( text="Hey Aaron!",
                                font_size=100,
                                color=[1,1,1,1],
                                pos=(f.x/2, f.y/2) )
        f.add_widget(greeting_label)

        def changeScreen(instance):
          self.manager.transition.direction='right'
          self.manager.current='welcome'

        next_button = Button( text="<<",
                              font_size=50,
                              color=[1,1,1,1],
                              size_hint=(0.1, 0.2),
                              pos_hint={'x': 0.0, 'y': 0.4} )
        next_button.bind(on_press=changeScreen)

        f.add_widget(next_button)

        f.color=[(16.0/255.0), (23.0/255.0), (22.0/255.0), 1] #warm gray, converted to Kivy
        #f.rect = Rectangle( size=f.size, pos=f.pos )
        self.add_widget(f)
