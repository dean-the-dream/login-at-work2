from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

class Logio(App):
    def build(self):
        layout = AnchorLayout(anchor_y = "top")
        bttn1 = Button(
            text= "Logio",
            size_hint = (.2, .2),
            background_color =(0.0, 25.86, 1.0),
            color = (0, 0, 0, 1)
        )
        layout.add_widget(bttn1)
        return layout

Logio().run()
            