from kivy.app import App 
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.animation import Animation, AnimationTransition
from kivy.uix.screenmanager import ScreenManager, Screen 

from datetime import datetime

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        #make sure we aren't overriding any important functionality
        super(WelcomeScreen, self).__init__(**kwargs)

        self._keyboard = Window.request_keyboard(None, self)
        self._keyboard.bind(on_key_down=self.on_keyboard_down)

        f = FloatLayout()
        greeting_label = Label( text="Welcome home!",
                                font_size=100,
                                color=[1,1,1,0],
                                pos=(f.x/2, (f.y/2 - 100)) )
        f.add_widget(greeting_label)

        colorAnim = Animation( color=[1.0, 1.0, 1.0, 1.0], 
                               transition=AnimationTransition.in_out_quad ) 
        moveAnim =  Animation( pos=(f.x/2, f.y/2),
                               transition=AnimationTransition.in_out_quad )
        colorAnim.start(greeting_label)
        moveAnim.start(greeting_label)

        f.color=[(16.0/255.0), (23.0/255.0), (22.0/255.0), 1] #warm gray, converted to Kivy
        self.add_widget(f)

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
            if keycode[1] == 'right':
                self.manager.transition.direction='left'
                self.manager.current='calendar'
            else:
                return False
            return True