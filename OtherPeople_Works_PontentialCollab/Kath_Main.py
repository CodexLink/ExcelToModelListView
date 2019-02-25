import kivy
kivy.require('1.1.0')

from kivy import Config
Config.set('graphics','multisamples','0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.image import Image
class SampGridLayout(GridLayout):
	pass

class SampleApp(App):
	def build(self):
		Builder.load_file('Kath_Kivy.kv')
		return SampGridLayout()

sample_app = SampleApp()
sample_app.run()