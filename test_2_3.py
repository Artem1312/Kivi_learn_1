from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout


class BoxApp(App):
    def build(self):
        al = AnchorLayout()
        # bl = BoxLayout(orientation = 'vertical', size_hint=[.4,.4])
        bl = BoxLayout(orientation = 'vertical', size_hint=[None, None], size=[300, 150])

        bl.add_widget(TextInput())
        bl.add_widget(TextInput())
        bl.add_widget(Button(text='input', size_hint=[.52, .52]))

        al.add_widget(bl)
        return al


if __name__ == "__main__":
    BoxApp().run();
