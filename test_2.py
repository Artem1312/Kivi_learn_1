from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class BoxApp(App):
    def build(self):
        #bl = BoxLayout()
        bl = BoxLayout(orientation='vertical',
                       padding=[50, 25],
                       spacing=10)
        bl.add_widget(Button(text='Button 1'))
        bl.add_widget(Button(text='Button 2'))
        bl.add_widget(Button(text='Button 3'))
        return bl


if __name__ == "__main__":
    BoxApp().run();
