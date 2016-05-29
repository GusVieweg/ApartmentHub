from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

from custombuttons import ImageButton

class FeelingsScreenUI(FloatLayout):
    def __init__(self, **kwargs):
        #make sure we aren't overriding any important functionality
        super(FeelingsScreenUI, self).__init__(**kwargs)
        
        g = GridLayout(cols=4, row_force_default=True, row_default_height=100,
                       size_hint_y=0.2, size_hint_x=0.6, pos_hint={'x': 0.2, 'y': 0.4})

        sadFace = ImageButton(source='images/sad.jpg')
        stressedFace = ImageButton(source='images/stressed.jpg')
        happyFace = ImageButton(source='images/happy.jpg')
        overjoyedFace = ImageButton(source='images/overjoyed.jpg')

        g.add_widget(stressedFace)
        g.add_widget(sadFace)
        g.add_widget(happyFace)
        g.add_widget(overjoyedFace)

        stressedLabel =  Label( text="Stressed",  font_size=25, color=[1,1,1,1] )
        sadLabel =       Label( text="Sad",       font_size=25, color=[1,1,1,1] )
        happyLabel =     Label( text="Happy",     font_size=25, color=[1,1,1,1] )
        overjoyedLabel = Label( text="Overjoyed", font_size=25, color=[1,1,1,1] )

        g.add_widget(stressedLabel)
        g.add_widget(sadLabel)
        g.add_widget(happyLabel)
        g.add_widget(overjoyedLabel)
        
        feelings_label = Label( text="How are you feeling today?",
                                font_size=100,
                                color=[1,0,1,1],
                                pos_hint={'x': 0, 'y':0.3} )
        self.add_widget(feelings_label)
        self.add_widget(g)