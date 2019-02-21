#!python
from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.anchorlayout import AnchorLayout # Added
from kivy.uix.widget import Widget # Added

class DataView(BoxLayout):

   item_template = StringProperty('DataViewItem')

   items = ListProperty([])

   def on_items(self, *args):
       self.clear_widgets()
       for item in self.items:
           w = Builder.template(self.item_template, **item)
           self.add_widget(w)