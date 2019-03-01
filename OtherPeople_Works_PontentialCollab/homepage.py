import kivy
kivy.require('1.1.0')

from kivy import Config
Config.set('graphics','multisamples','0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class homepageWindow(BoxLayout):
	pass
		
class homepageApp(App):
	def build(self):
		return homepageWindow()
		
		
if __name__ == "__main__":
	home = homepageApp()
	home.run()


