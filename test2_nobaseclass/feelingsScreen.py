from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen 

from custombuttons import SwitchButton
from feelingsscreenui import FeelingsScreenUI

class FeelingsScreen(Screen):
    def __init__(self, **kwargs):
        #make sure we aren't overriding any important functionality
        super(FeelingsScreen, self).__init__(**kwargs)

        self.f = FloatLayout()
        
        fsui = FeelingsScreenUI()

        self.f.add_widget(fsui)
        self.f.color=[(16.0/255.0), (23.0/255.0), (22.0/255.0), 1] #warm gray, converted to Kivy
        self.add_widget(self.f)

    def on_pre_enter(self):
        self.sb = SwitchButton(self.manager, 'right', 'welcome')
        self.f.add_widget(self.sb)