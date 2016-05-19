from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen 

import mycalendar
from switchbutton import SwitchButton 

class CalendarScreen(Screen):
    def __init__(self, **kwargs):
        super(CalendarScreen, self).__init__(**kwargs)

        self.r = RelativeLayout()

        calendar = mycalendar.myCalendar()
        self.r.add_widget(calendar)

        self.r.color=[(16.0/255.0), (23.0/255.0), (22.0/255.0), 1] #warm gray, converted to Kivy
        self.add_widget(self.r)

    def on_pre_enter(self):
        self.sb = SwitchButton(self.manager, 'left', 'welcome')
        self.r.add_widget(self.sb)
