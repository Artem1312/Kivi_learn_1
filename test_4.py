from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import (Color, Ellipse, Rectangle, Line)


class PainterWidget(Widget):
    def __init__(self, **kwargs):
        super(PainterWidget, self).__init__(**kwargs)

        with self.canvas:
            Color(0, 1, 0, 1)
            Ellipse(pos=(100, 100), size=(50, 50))
            Rectangle(pos=(100, 200), size=(50, 50))
            Line(points=(100, 350, 150, 350, 150, 300), close=True, width=3)

            self.line = Line(points=(), width=10, joint='miter', cap='square')

    def on_touch_down(self, touch):
        self.line.points += (touch.x, touch.y)

class PaintApp(App):
    def build(self):
        return PainterWidget()


if __name__ == "__main__":
    PaintApp().run()
