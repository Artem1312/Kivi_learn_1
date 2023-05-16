from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.uix.anchorlayout import AnchorLayout


class BoxApp(App):
    def build(self):
        #bl = BoxLayout()
        #gl = GridLayout(cols=10, padding=[10], spacing=3)
        al = AnchorLayout(anchor_x='left', anchor_y='top')

        al.add_widget(Button(text='Button 1', size_hint = [.52, .52]))

        return al


if __name__ == "__main__":
    BoxApp().run();
