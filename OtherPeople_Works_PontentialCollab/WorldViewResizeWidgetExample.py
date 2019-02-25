from kivy.app import App
from kivy.graphics import *
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class WorldviewWidget(Widget):
    def __init__(self, **kwargs):
        super(WorldviewWidget, self).__init__(**kwargs)

        self.canvas.clear()
        print (self.size, self.pos)

        with self.canvas:
            Color(1, 0, 0, 1, mode='rgba')
            # *changed* ##############################################
            self.rect = Rectangle(size=self.size, pos=self.pos)    

    # *new* ##########################################################
    def update_size(self, instance, new_size):
        print ("UPDATING SIZE"), instance, new_size
        self.size[0] = new_size[0] * 0.4
        self.size[1] = new_size[1] * 0.4
        self.rect.size = self.size
        self.pos[0] = self.parent.size[0] * 0.2
        self.pos[1] = self.parent.size[1] * 0.2
        self.rect.pos = self.pos

class JFROCS_App(App):

    def build(self):
        Window.clearcolor = [1,1,1,1]
        parent = FloatLayout(size=Window.size)

        # *changed* ##################################################
        worldview = WorldviewWidget(size=(0.4*parent.size[0], 0.4*parent.size[1]),
                                    pos=(0.2*parent.size[0], 0.2*parent.size[1]))
        # makes sure that the widget gets updated when parent's size changes:
        parent.bind(size=worldview.update_size)
        parent.add_widget(worldview)


        start_btn = Button(text='Start', size_hint=(0.1, 0.1), pos_hint={'x':.02, 'y':.7}, background_color=[0,1,0,1])
        start_btn.bind(on_release=self.start_simulation)
        parent.add_widget(start_btn)

        pause_btn = Button(text='Pause', size_hint=(0.1,0.1), pos_hint={'x':.02, 'y':.6}, background_color=[1,1,0,1])
        pause_btn.bind(on_release=self.pause_simulation)
        parent.add_widget(pause_btn)

        stop_btn = Button(text='Stop', size_hint=(0.1,0.1), pos_hint={'x':.02, 'y':.5}, background_color=[1,0,0,1])
        stop_btn.bind(on_release=self.stop_simulation)
        parent.add_widget(stop_btn)

        return parent

    def start_simulation(self, obj):
        print ("You pushed the start button!")
    def pause_simulation(self, obj):
        print ("You pushed the pause button!")
    def stop_simulation(self, obj):
        print ("You pushed the stop button!")

if __name__ == '__main__':
    JFROCS_App().run()