from kivy.app import App 
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout 
from kivy.graphics import Color, Rectangle
from kivy.animation import Animation, AnimationTransition
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.clock import Clock 

from custombuttons import SwitchButton 
import const

const.GUS_COLOR = [(238.0/255.0), (132.0/255.0), (52.0/255.0), 1]
const.CHRIS_COLOR = [(201.0/255.0), (93.0/255.0), (99.0/255.0), 1]
const.PATTY_COLOR = [(174.0/255.0), (135.0/255.0), (153.0/255.0), 1]

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        #make sure we aren't overriding any important functionality
        super(WelcomeScreen, self).__init__(**kwargs)

        self.f = FloatLayout()
        self.f.color=[(16.0/255.0), (23.0/255.0), (22.0/255.0), 1] #warm gray, converted to Kivy

        self.displayGreeting()
        Clock.schedule_once(self.displayNames, 5)

        self.add_widget(self.f)

    def displayGreeting(self):
        greeting_label = Label( text="Welcome!  Who's home?",
                                font_size=100,
                                color=[1,1,1,0],
                                pos=(self.f.x/2, (self.f.y/2 - 100)) )
        self.f.add_widget(greeting_label)

        colorAnim = Animation( color=[1.0, 1.0, 1.0, 1.0], 
                               transition=AnimationTransition.in_out_quad ) 
        moveAnim =  Animation( pos=(self.f.x/2, self.f.y/2),
                               transition=AnimationTransition.in_out_quad )
        colorAnim.start(greeting_label)
        moveAnim.start(greeting_label)

    def displayNames(self, dt):
        nameLayout = GridLayout( cols=3,
                                 row_force_default=True,
                                 row_default_height=100,
                                 size_hint_x=0.6, size_hint_y=0.2,
                                 pos_hint={'x': 0.2, 'y': 0.2} )
        gusButton = Button( text="Gus", color=[0,0,0,0],
                            background_color=[0,0,0,0] )
        chrisButton = Button( text="Chris", color=[0,0,0,0],
                              background_color=[0,0,0,0] )
        pattyButton = Button( text="Patty", color=[0,0,0,0],
                              background_color=[0,0,0,0] )
        
        gusButtonAnim = Animation( background_color=const.GUS_COLOR, color=[1,1,1,1], 
                                   transition=AnimationTransition.in_out_quad )
        chrisButtonAnim = Animation( background_color=const.CHRIS_COLOR, color=[1,1,1,1],
                                     transition=AnimationTransition.in_out_quad )
        pattyButtonAnim = Animation( background_color=const.PATTY_COLOR, color=[1,1,1,1],
                                     transition=AnimationTransition.in_out_quad )
        gusButtonAnim.start(gusButton)
        chrisButtonAnim.start(chrisButton)
        pattyButtonAnim.start(pattyButton)

        nameLayout.add_widget(gusButton)
        nameLayout.add_widget(chrisButton)
        nameLayout.add_widget(pattyButton)
        self.f.add_widget(nameLayout)

    def on_pre_enter(self):
        self.sb = SwitchButton(self.manager, 'right', 'calendar')
        self.sb2 = SwitchButton(self.manager, 'left', 'feelings')
        self.f.add_widget(self.sb)
        self.f.add_widget(self.sb2)