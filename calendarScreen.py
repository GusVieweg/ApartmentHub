from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen 

import mycalendar

class AnotherScreen(Screen):
    def __init__(self, **kwargs):
        super(AnotherScreen, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(None, self)
        self._keyboard.bind(on_key_down=self.on_keyboard_down)

        r = RelativeLayout()

        calendar = mycalendar.myCalendar()
        r.add_widget(calendar)

        r.color=[(16.0/255.0), (23.0/255.0), (22.0/255.0), 1] #warm gray, converted to Kivy
        self.add_widget(r)

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'left':
            self.manager.transition.direction='right'
            self.manager.current='welcome'
        else:
            return False
        return True
