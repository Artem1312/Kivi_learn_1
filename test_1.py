from kivy.app import App
from kivy.uix.bubble import Button


# https://kivy.org/doc/stable/gettingstarted/installation.html#install-pip
# https://kivy.org/doc/stable/api-index.html

class MyApp(App):
    def build(self):
        return Button(text='My first button',
                      font_size=30,
                      on_press=self.btn_press,
                      background_color=[1, 0, 0, 1],
                      background_normal='')

    def btn_press(self, instance):
        print("Button on press")
        instance.text = "i am pressed"


if __name__ == "__main__":
    MyApp().run()
