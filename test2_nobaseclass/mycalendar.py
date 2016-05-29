from kivy.KivyCalendar import CalendarWidget
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

import const

const.POPUP_HEIGHT=300
const.BUTTON_HEIGHT=50
const.TEXTINPUT_HEIGHT=(const.POPUP_HEIGHT-const.BUTTON_HEIGHT-65)

class myCalendar(CalendarWidget):
    def __init__(self, **kwargs):
        super(myCalendar, self).__init__(**kwargs)
        self.popup = Popup( title='default title' )

    def set_popup(self):
        month = self.month_names[self.active_date[1] - 1]
        day = self.active_date[0]
        year = self.active_date[2]
        date = month + " " + str(day) + " " + str(year)
        
        g1 = GridLayout(rows=2)
        g2 = GridLayout(cols=2, 
                        row_force_default=True, 
                        row_default_height=const.BUTTON_HEIGHT)

        g2.add_widget(Button(text="Exit",
                             on_press=self.close_popup) )
        g2.add_widget(Button(text="Submit"))

        g1.add_widget(TextInput(size_hint_y=None, 
                                height=const.TEXTINPUT_HEIGHT))
        g1.add_widget(g2)

        self.popup = Popup( title=date,
                            content=g1,
                            size_hint=(None, None),
                            size=(400, const.POPUP_HEIGHT) )

    def close_popup(self, inst):
        self.popup.dismiss()

    def get_btn_value(self, inst):
        super(myCalendar, self).get_btn_value(inst)
        self.set_popup()
        self.popup.open()
