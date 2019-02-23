from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder


kv = '''
<RootWidget>:
    cols: 3
    rows: 2
    Button:
        text: "S1 S1"
        size_hint_x: None
        width: 300
    Button:
        text: "S1 S2"
    Button:
        text: "S1 S3"
    Button:
        text: "S2 S1"
        size_hint_x: None
        width: 300
    Button:
        text: "S2 S2"
    Button:
        text: "S2 S3"
'''
#class RootWidget(GridLayout):
#    pass

class izgaraApp(App):
    def build(self):
        return Builder.load_string(kv)


if __name__ == "__main__":
    izgaraApp().run()

