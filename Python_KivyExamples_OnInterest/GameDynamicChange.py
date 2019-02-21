from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock


KV = '''

<MyPopup>:
    title: "Game over"
    score_label: score_label
    id: popup
    content: bl
    BoxLayout:
        id: bl
        Label:
            id: score_label
            text:"Your score is"
            font_size:20
        Button:
            text:"Close this!!"
            on_release: popup.dismiss()


MyLayout:

    orientation: "vertical"
    Label:
        text: "Type in score"
    TextInput:
        id: score_inp
    Button:
        text: "Open gameover popup"
        on_release:
            root.gameover_popup.open()
            root.gameover_popup.gameover(score_inp.text)

'''


class MyPopup(Popup):

    def gameover(self,score):
        self.iterations = int(score)
        self.score = 0
        self.event = Clock.schedule_interval(self.set_label,0.1)

    def set_label(self,dt):
        self.score += 1
        self.score_label.text = str(self.score)
        if self.score >= self.iterations:
            self.event.cancel()



class MyLayout(BoxLayout):

    def __init__(self,**kwargs):
        super(MyLayout,self).__init__(**kwargs) 
        self.gameover_popup = MyPopup()



class MyApp(App):

    def build(self):
        return Builder.load_string(KV)


MyApp().run()