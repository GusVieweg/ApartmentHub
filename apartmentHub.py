from kivy.app import App 
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.animation import Animation, AnimationTransition
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.lang import Builder

from welcomeScreen import WelcomeScreen
from anotherScreen import AnotherScreen

#kivy.require("1.9.2")
Window.fullscreen = 'auto'

sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='welcome'))
sm.add_widget(AnotherScreen(name='another'))

class MainscreenApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    MainscreenApp().run()
