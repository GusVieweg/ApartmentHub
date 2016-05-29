from kivy.app import App 
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.animation import Animation, AnimationTransition
from kivy.uix.screenmanager import ScreenManager, Screen 

from custombuttons import SwitchButton 
from datetime import datetime

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        #make sure we aren't overriding any important functionality
        super(WelcomeScreen, self).__init__(**kwargs)

        self.f = FloatLayout()

        greeting_label = Label( text="Welcome home!",
                                font_size=100,
                                color=[1,1,1,1],
                                pos=(self.f.x/2, (self.f.y/2 - 100)) )
        self.f.add_widget(greeting_label)

        colorAnim = Animation( color=[1.0, 1.0, 1.0, 1.0], 
                               transition=AnimationTransition.in_out_quad ) 
        moveAnim =  Animation( pos=(self.f.x/2, self.f.y/2),
                               transition=AnimationTransition.in_out_quad )
        colorAnim.start(greeting_label)
        moveAnim.start(greeting_label)

        self.f.color=[(16.0/255.0), (23.0/255.0), (22.0/255.0), 1] #warm gray, converted to Kivy
        self.add_widget(self.f)

    def on_pre_enter(self):
        self.sb = SwitchButton(self.manager, 'right', 'calendar')
        self.sb2 = SwitchButton(self.manager, 'left', 'feelings')
        self.f.add_widget(self.sb)
        self.f.add_widget(self.sb2)