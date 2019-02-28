from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string("""
<ButtonsApp>:
    orientation: "vertical"
    Button:
        StackLayout:
            pos: self.parent.pos
            size: self.parent.size
            orientation: 'lr-tb'
            Image:
                source: 'LayerTriangleVector3.jpg'
                size_hint_x: None
                width: 74
            Label:
                size_hint_x: None
                width: 100
                text: "The text"
    Label:
        text: "A label"
""")

class ButtonsApp(App, BoxLayout):
    def build(self):
        return self

if __name__ == "__main__":
    ButtonsApp().run()