from kivy.app import App
from kivy.uix.bubble import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer

# https://kivy.org/doc/stable/gettingstarted/installation.html#install-pip
# https://kivy.org/doc/stable/api-index.html
# https://www.youtube.com/watch?v=VIy3hktYKwE

from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')


from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter


class MyApp(App):
    def build(self):
        # return CodeInput(lexer=HtmlLexer())
        s = Scatter()
        fl = FloatLayout(size=(300,300))
        s.add_widget(fl)
        fl.add_widget(Button(text='My first button',
                             font_size=30,
                             on_press=self.btn_press,
                             background_color=[1, 0, 0, 1],
                             background_normal='',
                             size_hint=(.5, .25),
                             pos=(640 / 2 / 2, 480 / 2 - (480 * .25 / 2))));

        #return fl
        return s

    def btn_press(self, instance):
        print("Button on press")
        instance.text = "i am pressed"


if __name__ == "__main__":
    MyApp().run()
