from kivy.app import App 
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.animation import Animation, AnimationTransition
from kivy.uix.screenmanager import ScreenManager, Screen 

from datetime import datetime
from switchbutton import SwitchButton

class FeelingsScreen(Screen):
    def __init__(self, **kwargs):
        #make sure we aren't overriding any important functionality
        super(FeelingsScreen, self).__init__(**kwargs)

        self.f = FloatLayout()
        greeting_label = Label( text="Feelings screen!",
                                font_size=100,
                                color=[1,0,1,1],
                                pos=(self.f.x/2, (self.f.y/2)) )
        self.f.add_widget(greeting_label)

        self.f.color=[(16.0/255.0), (23.0/255.0), (22.0/255.0), 1] #warm gray, converted to Kivy
        self.add_widget(self.f)

    def on_pre_enter(self):
        self.sb = SwitchButton(self.manager, 'right', 'welcome')
        self.f.add_widget(self.sb)