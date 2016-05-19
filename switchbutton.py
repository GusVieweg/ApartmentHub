from kivy.uix.button import Button 

class SwitchButton(Button):
    def __init__(self, manager, direction, screen, **kwargs):
        super(SwitchButton, self).__init__(**kwargs)
        self.manager = manager
        self.screen = screen
        self.size_hint_y = 0.2
        self.size_hint_x = 0.2

        if( direction == 'left'):
            self.text = "<<"
            self.pos_hint = {'x': 0.0, 'y': 0.4}
            self.direction = 'right'
        elif( direction == 'right' ):
            self.text = ">>"
            self.pos_hint = {'x': 0.8, 'y': 0.4}
            self.direction = 'left'

    def on_press(self):
        self.manager.transition.direction = self.direction
        self.manager.current = self.screen