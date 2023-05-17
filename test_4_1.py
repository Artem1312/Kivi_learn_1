# https://youtu.be/5krP5IvKj5Q?t=650

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import (Color, Ellipse, Rectangle, Line)


class PainterWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(0,1,0,1)
            Ellipse()


class PaintApp(App):
    def build(self):
        return PainterWidget()


if __name__ == "__main__":
    PaintApp().run()
