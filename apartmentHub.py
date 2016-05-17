from kivy.app import App 
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.animation import Animation, AnimationTransition
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.lang import Builder
from kivy.config import Config

from welcomeScreen import WelcomeScreen
from calendarScreen import CalendarScreen
from feelingsScreen import FeelingsScreen

#kivy.require("1.9.2")
Window.fullscreen = 'auto'
Config.set('input','mouse','mouse,disable_multitouch')

class MainscreenApp(App):
    def build(self):
    	sm = ScreenManager()
    	sm.add_widget(WelcomeScreen(name='welcome'))
    	sm.add_widget(CalendarScreen(name='calendar'))
    	sm.add_widget(FeelingsScreen(name='feelings'))
        return sm

if __name__ == '__main__':
    MainscreenApp().run()
