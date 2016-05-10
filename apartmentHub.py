from kivy.app import App 
from kivy.core.window import Window
from kivy.uix.label import Label 
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.animation import Animation, AnimationTransition


Window.fullscreen = 'auto'


class RootWidget(FloatLayout):

	def __init__(self, **kwargs):
		#make sure we aren't overriding any important functionality
		super(RootWidget, self).__init__(**kwargs)

		#adding the widget
		greeting_label = Label( text="Welcome home!", 
								font_size=100,
								color=[1,1,1,0],
								pos=(self.x/2, (self.y/2 - 100)) )
		
		#greeting_label.text = greeting_label.text + " " + name

		self.add_widget(greeting_label)
		
		anim =  Animation(color=[1.0, 1.0, 1.0, 1.0], 
						  pos=(self.x/2, self.y/2),
						  transition = AnimationTransition.in_out_quad) 
		anim.start(greeting_label)


class mainScreenApp(App):
	def build(self):
		self.root = root = RootWidget()
		root.bind(pos=self.update_rect, size=self.update_rect)

		with root.canvas.before:
			Color((16.0/255.0), (23.0/255.0), (22.0/255.0), 1) #warm gray, converted to Kivy
			self.rect = Rectangle( size=root.size, pos=root.pos )
		return root

	def update_rect(self, instance, value):
		self.rect.pos = instance.pos
		self.rect.size = instance.size

if __name__ == '__main__':
	mainScreenApp().run()
