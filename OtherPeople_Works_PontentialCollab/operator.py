import kivy
kivy.require('1.10.1')

from kivy import Config
Config.set('graphics','multisamples','0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class OperatorWindow(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

class OperatorApp(App):
	def build(self):
		return OperatorWindow()
		
if __name__ == "__main__":
	oapp = OperatorApp()
	oapp.run()
