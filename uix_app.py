from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior


class Mode(object):
    def __init__(self) -> None:
        self.mode = 0
    
    def set_mode(self, choice):
        self.mode = choice

option = Mode()

class Logio(App):
    def build(self):
        layout = AnchorLayout(anchor_y = "top")
        bttn1 = Button(
            text= "Logio",
            size_hint = (.2, .2),
            background_color =(0.0, 25.86, 1.0),
            color = (0, 0, 0, 1)
        )
        bttn1.bind(on_press = self.callback)
        layout.add_widget(bttn1)
        return layout

    def callback(self, event):
        option.set_mode(1)
        print(option.mode)
        

def run_uix():
    Logio().run()
            

