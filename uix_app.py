from kivy.app import App
from kivy.uix.gridlayout import GridLayout
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
        layout = GridLayout(rows=3)
        bttn1 = Button(
            text= "Login",
            size_hint = (.2, .2),
            background_color =(0.0, 25.86, 1.0),
            color = (0, 0, 0, 1)
        )
        bttn2 = Button(
            text= "Lunch",
            size_hint = (.2, .2),
            background_color =(0.0, 25.86, 1.0),
            color = (0, 0, 0, 1)
        )
        bttn3 = Button(
            text= "Logout",
            size_hint = (.2, .2),
            background_color =(0.0, 25.86, 1.0),
            color = (0, 0, 0, 1)
        )
        
        bttn1.bind(on_press = self.login)
        bttn2.bind(on_press = self.lunch)
        bttn3.bind(on_press = self.logout)
        layout.add_widget(bttn1)
        layout.add_widget(bttn2)
        layout.add_widget(bttn3)
        return layout

    def login(self, event):
        option.set_mode(1)
        print(option.mode)
    def lunch(self, event):
        option.set_mode(2)
        print(option.mode)
    def logout(self, event):
        option.set_mode(3)
        print(option.mode)


def run_uix():
    Logio().run()
            
